# 주제: 트리 순회 — 반복(스택) 방식 (전위/중위/후위)
# Time: O(n) — 각 노드를 정확히 1번 방문
# Space: O(h) — 명시적 스택 크기 = 트리 높이

from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# ── 반복 순회 ──────────────────────────────────────────────────────────────

def preorder_iterative(root: TreeNode | None) -> list[int]:
    """반복 전위 순회: 현재 → 왼쪽 → 오른쪽.

    핵심 아이디어:
      - 스택에 루트를 넣고 시작
      - pop → 방문 → 오른쪽 push → 왼쪽 push
      - 왼쪽을 나중에 push해야 먼저 처리됨 (LIFO)

    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # 오른쪽을 먼저 push → 왼쪽이 먼저 pop됨
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """반복 중위 순회: 왼쪽 → 현재 → 오른쪽.

    핵심 아이디어:
      - curr 포인터로 왼쪽 끝까지 이동하며 스택에 push
      - 왼쪽 끝 도달 → pop → 방문 → curr = curr.right
      - 오른쪽 서브트리에 대해 반복

    Time:  O(n)
    Space: O(h)
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    curr: TreeNode | None = root

    while curr or stack:
        # 왼쪽 끝까지 이동
        while curr:
            stack.append(curr)
            curr = curr.left

        # 방문 및 오른쪽 이동
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

    return result


def postorder_iterative(root: TreeNode | None) -> list[int]:
    """반복 후위 순회: 왼쪽 → 오른쪽 → 현재.

    핵심 아이디어 (역순 활용):
      - 전위 순회(현재→오른쪽→왼쪽)의 결과를 뒤집으면 후위
      - 즉, 스택에서 pop → 결과에 추가 → 왼쪽 push → 오른쪽 push
      - 마지막에 result 역순

    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)   # 현재 방문 (역순이므로 마지막에 reverse)

        if node.left:             # 왼쪽 먼저 push (오른쪽이 먼저 pop됨)
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    result.reverse()              # 현재→오른쪽→왼쪽 → 뒤집기 → 왼쪽→오른쪽→현재
    return result


def postorder_two_stack(root: TreeNode | None) -> list[int]:
    """두 스택을 이용한 후위 순회 (교육 목적).

    Time:  O(n)
    Space: O(n) — 두 번째 스택이 최대 n개 저장
    """
    if root is None:
        return []

    stack1: list[TreeNode] = [root]
    stack2: list[int] = []

    while stack1:
        node = stack1.pop()
        stack2.append(node.val)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    return stack2[::-1]


# ── 헬퍼: 리스트로 트리 생성 ──────────────────────────────────────────────

def build(values: list[int | None]) -> TreeNode | None:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q: deque[TreeNode] = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = build([1, 2, 3, 4, 5, 6, 7])

    print("=== 반복(스택) 순회 결과 ===")
    print(f"전위 (Pre-order):   {preorder_iterative(root)}")
    print(f"중위 (In-order):    {inorder_iterative(root)}")
    print(f"후위 (Post-order):  {postorder_iterative(root)}")
    print(f"후위 (두 스택):     {postorder_two_stack(root)}")

    print("\n=== 재귀 vs 반복 결과 비교 ===")
    from src.02_recursive_traversal import preorder, inorder, postorder  # noqa

    # 직접 비교 (동일해야 함)
    assert preorder_iterative(root) == [1, 2, 4, 5, 3, 6, 7]
    assert inorder_iterative(root) == [4, 2, 5, 1, 6, 3, 7]
    assert postorder_iterative(root) == [4, 5, 2, 6, 7, 3, 1]
    print("모든 결과 일치 ✓")

    # 편향 트리 (왼쪽으로만)
    print("\n=== 편향 트리 ===")
    #  1
    #   \
    #    2
    #     \
    #      3
    skewed = build([1, None, 2, None, None, None, 3])
    # 직접 구성
    skewed = TreeNode(1)
    skewed.right = TreeNode(2)
    skewed.right.right = TreeNode(3)
    print(f"중위 (편향 오른쪽): {inorder_iterative(skewed)}")
