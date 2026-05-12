# 주제: 레벨 순회 (BFS), 레벨별 그룹화, 지그재그 순회
# Time: O(n) — 각 노드를 정확히 1번 방문
# Space: O(w) — w = 최대 너비 (완전 이진 트리에서 w ≈ n/2)

from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0,
                 left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[int]:
    """기본 레벨 순회 (BFS).

    Time:  O(n)
    Space: O(w) — 큐 최대 크기 = 최대 너비
    """
    if root is None:
        return []

    result: list[int] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def level_order_by_levels(root: TreeNode | None) -> list[list[int]]:
    """레벨별 그룹화 BFS.

    핵심: 루프 시작 시 len(queue)로 현재 레벨 크기를 고정

    Time:  O(n)
    Space: O(w)
    """
    if root is None:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)   # 현재 레벨 노드 수 (중요!)
        level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def zigzag_level_order(root: TreeNode | None) -> list[list[int]]:
    """지그재그(나선형) 레벨 순회.

    짝수 레벨: 왼쪽 → 오른쪽 (정방향)
    홀수 레벨: 오른쪽 → 왼쪽 (역방향)

    Time:  O(n)
    Space: O(w)
    """
    if root is None:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])
    left_to_right = True   # 첫 레벨은 정방향

    while queue:
        level_size = len(queue)
        level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level.reverse()   # 역방향 레벨은 뒤집기

        result.append(level)
        left_to_right = not left_to_right   # 방향 전환

    return result


def right_side_view(root: TreeNode | None) -> list[int]:
    """오른쪽에서 보이는 노드 (각 레벨의 마지막 노드).

    Time:  O(n)
    Space: O(w)
    """
    if root is None:
        return []

    result: list[int] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:   # 레벨의 마지막 노드
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def max_depth_bfs(root: TreeNode | None) -> int:
    """BFS로 트리 최대 깊이 구하기.

    Time:  O(n)
    Space: O(w)
    """
    if root is None:
        return 0

    depth = 0
    queue: deque[TreeNode] = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


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
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root = build([1, 2, 3, 4, 5, None, 6])

    print("=== 레벨 순회 ===")
    print(f"기본 BFS:         {level_order(root)}")
    print(f"레벨별 그룹화:    {level_order_by_levels(root)}")
    print(f"지그재그 순회:    {zigzag_level_order(root)}")
    print(f"오른쪽 뷰:        {right_side_view(root)}")
    print(f"최대 깊이 (BFS):  {max_depth_bfs(root)}")

    print()
    print("=== 완전 이진 트리 ===")
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    full = build([1, 2, 3, 4, 5, 6, 7])
    levels = level_order_by_levels(full)
    for i, lv in enumerate(levels):
        print(f"  레벨 {i}: {lv}")

    print()
    print("=== 지그재그 시각화 ===")
    #           1          레벨 0: → [1]
    #         /   \
    #        2     3       레벨 1: ← [3, 2]
    #       / \   / \
    #      4   5 6   7     레벨 2: → [4, 5, 6, 7]
    zz = zigzag_level_order(full)
    for i, lv in enumerate(zz):
        direction = "→" if i % 2 == 0 else "←"
        print(f"  레벨 {i} ({direction}): {lv}")
