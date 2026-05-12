# 주제: BST 응용 — 정렬, 범위 쿼리, floor/ceil
# Time: O(n log n) BST 정렬, O(log n + k) 범위 쿼리
# Space: O(n)

from __future__ import annotations


class BSTNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BST:
    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, val: int) -> None:
        self.root = self._insert(self.root, val)

    def _insert(self, node: BSTNode | None, val: int) -> BSTNode:
        if node is None:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def inorder(self) -> list[int]:
        """중위 순회 = 정렬된 배열.

        Time:  O(n)
        Space: O(n)
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

    def range_query(self, low: int, high: int) -> list[int]:
        """[low, high] 범위 내 값 모두 반환.

        핵심: 현재 값이 low보다 크면 왼쪽 탐색, high보다 작으면 오른쪽 탐색

        Time:  O(log n + k) — k = 결과 수
        Space: O(k + h)
        """
        result: list[int] = []
        self._range_query(self.root, low, high, result)
        return result

    def _range_query(
        self,
        node: BSTNode | None,
        low: int,
        high: int,
        result: list[int],
    ) -> None:
        if node is None:
            return
        if node.val > low:
            self._range_query(node.left, low, high, result)
        if low <= node.val <= high:
            result.append(node.val)
        if node.val < high:
            self._range_query(node.right, low, high, result)

    def floor(self, val: int) -> int | None:
        """floor(val): val 이하의 최댓값.

        Time:  O(h)
        Space: O(1)
        """
        result: int | None = None
        curr = self.root
        while curr:
            if curr.val == val:
                return curr.val
            elif curr.val < val:
                result = curr.val   # 후보
                curr = curr.right
            else:
                curr = curr.left
        return result

    def ceil(self, val: int) -> int | None:
        """ceil(val): val 이상의 최솟값.

        Time:  O(h)
        Space: O(1)
        """
        result: int | None = None
        curr = self.root
        while curr:
            if curr.val == val:
                return curr.val
            elif curr.val > val:
                result = curr.val   # 후보
                curr = curr.left
            else:
                curr = curr.right
        return result

    def count_range(self, low: int, high: int) -> int:
        """[low, high] 범위 내 노드 수 (BST 활용).

        Time:  O(log n + k)
        Space: O(h)
        """
        return len(self.range_query(low, high))


def bst_sort(arr: list[int]) -> list[int]:
    """BST를 이용한 정렬.

    Time:  O(n log n) 평균, O(n²) 최악 (편향 트리)
    Space: O(n)

    참고: 이미 정렬된 배열이면 O(n²) — 실용적으로 heapq/sorted() 선호
    """
    bst = BST()
    for v in arr:
        bst.insert(v)
    return bst.inorder()


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    values = [20, 8, 22, 4, 12, 10, 14]
    bst = BST()
    for v in values:
        bst.insert(v)

    print("=== BST 정렬 ===")
    print(f"입력:  {values}")
    print(f"정렬:  {bst.inorder()}")

    print("\n=== 범위 쿼리 [10, 20] ===")
    print(f"  결과: {bst.range_query(10, 20)}")

    print("\n=== Floor / Ceil ===")
    test_vals = [5, 9, 11, 13, 21, 23]
    print(f"{'값':>5} | {'floor':>8} | {'ceil':>8}")
    print("-" * 28)
    for v in test_vals:
        f = bst.floor(v)
        c = bst.ceil(v)
        print(f"{v:>5} | {str(f):>8} | {str(c):>8}")

    print("\n=== BST Sort (랜덤 배열) ===")
    import random
    arr = random.sample(range(1, 101), 10)
    print(f"입력: {arr}")
    print(f"정렬: {bst_sort(arr)}")

    print("\n=== 범위 내 개수 ===")
    print(f"  [10, 20] 내 노드 수: {bst.count_range(10, 20)}")
    print(f"  [1, 5]   내 노드 수: {bst.count_range(1, 5)}")
