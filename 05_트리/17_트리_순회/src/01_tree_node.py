# 주제: 트리 노드 클래스 및 트리 생성
# Time: O(n) — 노드 수 n에 비례
# Space: O(n) — 모든 노드 저장

from __future__ import annotations
from collections import deque


class TreeNode:
    """이진 트리 노드."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def build_tree_from_list(values: list[int | None]) -> TreeNode | None:
    """레벨 순서 리스트로 이진 트리 생성.

    Args:
        values: 레벨 순서 노드 값 리스트 (None = 빈 자리)

    Returns:
        트리의 루트 노드

    Time:  O(n)
    Space: O(n)
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # 왼쪽 자식
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # 오른쪽 자식
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_height(root: TreeNode | None) -> int:
    """트리 높이(루트에서 리프까지 최대 간선 수).

    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return -1  # 빈 트리 높이 = -1
    return 1 + max(tree_height(root.left), tree_height(root.right))


def count_nodes(root: TreeNode | None) -> int:
    """트리의 노드 수.

    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def print_tree(root: TreeNode | None, level: int = 0, prefix: str = "루트: ") -> None:
    """트리를 텍스트 아트로 출력.

    Time:  O(n)
    Space: O(h)
    """
    if root is None:
        return
    print(" " * (level * 4) + prefix + str(root.val))
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L── ")
        else:
            print(" " * ((level + 1) * 4) + "L── (없음)")
        if root.right:
            print_tree(root.right, level + 1, "R── ")
        else:
            print(" " * ((level + 1) * 4) + "R── (없음)")


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    values = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree_from_list(values)

    print("=== 트리 구조 ===")
    print_tree(root)

    print(f"\n트리 높이: {tree_height(root)}")
    print(f"노드 수:   {count_nodes(root)}")

    # 비대칭 트리 테스트
    print("\n=== 비대칭 트리 ===")
    asym = build_tree_from_list([1, 2, 3, None, 4, None, 5])
    print_tree(asym)
    print(f"높이: {tree_height(asym)}, 노드 수: {count_nodes(asym)}")
