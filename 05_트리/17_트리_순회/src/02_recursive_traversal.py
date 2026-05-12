# 주제: 트리 순회 — 재귀 방식 (전위/중위/후위)
# Time: O(n) — 각 노드를 정확히 1번 방문
# Space: O(h) — 재귀 호출 스택 깊이 = 트리 높이

from __future__ import annotations
import sys

sys.setrecursionlimit(10_000)

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# ── 재귀 순회 ──────────────────────────────────────────────────────────────

def preorder(root: TreeNode | None) -> list[int]:
    """전위 순회: 현재 → 왼쪽 → 오른쪽.

    활용: 트리 복사, 직렬화(serialize), 프린트
    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: TreeNode | None) -> list[int]:
    """중위 순회: 왼쪽 → 현재 → 오른쪽.

    활용: BST에서 오름차순 출력, 수식 트리 평가
    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: TreeNode | None) -> list[int]:
    """후위 순회: 왼쪽 → 오른쪽 → 현재.

    활용: 트리 삭제, 폴더 크기 계산, 수식 계산
    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# ── 인플레이스(결과 리스트 인자 전달) 버전 — 메모리 효율적 ──────────────────

def preorder_inplace(root: TreeNode | None, result: list[int]) -> None:
    """인플레이스 전위 순회 (리스트 새로 생성 안 함).

    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return
    result.append(root.val)
    preorder_inplace(root.left, result)
    preorder_inplace(root.right, result)


def inorder_inplace(root: TreeNode | None, result: list[int]) -> None:
    """인플레이스 중위 순회."""
    if root is None:
        return
    inorder_inplace(root.left, result)
    result.append(root.val)
    inorder_inplace(root.right, result)


def postorder_inplace(root: TreeNode | None, result: list[int]) -> None:
    """인플레이스 후위 순회."""
    if root is None:
        return
    postorder_inplace(root.left, result)
    postorder_inplace(root.right, result)
    result.append(root.val)


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

    print("=== 재귀 순회 결과 ===")
    print(f"전위 (Pre-order):   {preorder(root)}")
    print(f"중위 (In-order):    {inorder(root)}")
    print(f"후위 (Post-order):  {postorder(root)}")

    print("\n=== 인플레이스 순회 ===")
    res_pre: list[int] = []
    res_in: list[int] = []
    res_post: list[int] = []
    preorder_inplace(root, res_pre)
    inorder_inplace(root, res_in)
    postorder_inplace(root, res_post)
    print(f"전위: {res_pre}")
    print(f"중위: {res_in}")
    print(f"후위: {res_post}")

    # BST에서 중위 = 정렬
    print("\n=== BST 중위 순회 = 정렬 ===")
    #      4
    #     / \
    #    2   6
    #   / \ / \
    #  1  3 5  7
    bst = build([4, 2, 6, 1, 3, 5, 7])
    print(f"BST 중위 순회: {inorder(bst)}  ← 오름차순!")
