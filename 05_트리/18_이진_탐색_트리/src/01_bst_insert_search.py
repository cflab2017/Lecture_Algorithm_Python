# 주제: BST 삽입, 탐색, 중위 순회
# Time: O(log n) 평균, O(n) 최악 (편향 트리)
# Space: O(n) 저장, O(h) 재귀 스택

from __future__ import annotations


class BSTNode:
    """이진 탐색 트리 노드."""

    def __init__(self, val: int) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None

    def __repr__(self) -> str:
        return f"BSTNode({self.val})"


class BST:
    """이진 탐색 트리 구현."""

    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, val: int) -> None:
        """값 삽입.

        Time:  O(h) — h = 트리 높이
        Space: O(h) — 재귀 스택
        """
        self.root = self._insert(self.root, val)

    def _insert(self, node: BSTNode | None, val: int) -> BSTNode:
        if node is None:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        # val == node.val: 중복 무시
        return node

    def search(self, val: int) -> bool:
        """값 탐색.

        Time:  O(h)
        Space: O(1) — 반복
        """
        return self._search_iterative(self.root, val)

    def _search_iterative(self, root: BSTNode | None, val: int) -> bool:
        curr = root
        while curr:
            if val == curr.val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def search_node(self, val: int) -> BSTNode | None:
        """노드 자체 반환 (None이면 없음).

        Time:  O(h)
        Space: O(1)
        """
        curr = self.root
        while curr:
            if val == curr.val:
                return curr
            curr = curr.left if val < curr.val else curr.right
        return None

    def inorder(self) -> list[int]:
        """중위 순회 — 항상 정렬된 순서.

        Time:  O(n)
        Space: O(n) 결과 + O(h) 스택
        """
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: BSTNode | None, result: list[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)

    def minimum(self) -> int | None:
        """최솟값 (가장 왼쪽 노드).

        Time:  O(h)
        Space: O(1)
        """
        if self.root is None:
            return None
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def maximum(self) -> int | None:
        """최댓값 (가장 오른쪽 노드).

        Time:  O(h)
        Space: O(1)
        """
        if self.root is None:
            return None
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def height(self) -> int:
        """트리 높이.

        Time:  O(n)
        Space: O(h)
        """
        return self._height(self.root)

    def _height(self, node: BSTNode | None) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    bst = BST()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    print("=== 삽입 ===")
    for v in values:
        bst.insert(v)
        print(f"  insert({v})")

    print("\n=== 중위 순회 (정렬 결과) ===")
    print(f"  {bst.inorder()}")

    print("\n=== 탐색 ===")
    for v in [6, 13, 99]:
        found = bst.search(v)
        print(f"  search({v:2d}) → {found}")

    print("\n=== 최솟값 / 최댓값 ===")
    print(f"  최솟값: {bst.minimum()}")
    print(f"  최댓값: {bst.maximum()}")
    print(f"  트리 높이: {bst.height()}")

    # 정렬된 순서 삽입 → 편향 트리
    print("\n=== 편향 트리 (정렬 순서 삽입) ===")
    skewed = BST()
    for v in [1, 2, 3, 4, 5]:
        skewed.insert(v)
    print(f"  높이: {skewed.height()} (편향: n-1 = {5-1})")
    print(f"  중위: {skewed.inorder()}")
