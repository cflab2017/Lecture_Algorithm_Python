# 주제: BST 삭제 — 리프, 자식 1개, 자식 2개 (후계자)
# Time: O(h) — h = 트리 높이 (평균 O(log n), 최악 O(n))
# Space: O(h) — 재귀 스택

from __future__ import annotations


class BSTNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BST:
    def __init__(self) -> None:
        self.root: BSTNode | None = None

    # ── 삽입 (이전 강의와 동일) ────────────────────────────────────────────
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

    # ── 삭제 ──────────────────────────────────────────────────────────────
    def delete(self, val: int) -> None:
        """BST에서 값 삭제.

        3가지 경우:
          1) 리프: 그냥 제거
          2) 자식 1개: 자식으로 대체
          3) 자식 2개: 후계자(오른쪽 서브트리 최솟값)로 대체

        Time:  O(h)
        Space: O(h)
        """
        self.root = self._delete(self.root, val)

    def _delete(self, node: BSTNode | None, val: int) -> BSTNode | None:
        if node is None:
            return None  # 값 없음

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # 삭제 대상 노드 발견
            if node.left is None:
                # 경우 1 & 2a: 왼쪽 없음 → 오른쪽으로 대체 (리프 포함)
                return node.right
            elif node.right is None:
                # 경우 2b: 오른쪽 없음 → 왼쪽으로 대체
                return node.left
            else:
                # 경우 3: 자식 2개 → 후계자(오른쪽 최솟값)로 대체
                successor_val = self._find_min(node.right)
                node.val = successor_val
                # 후계자 노드를 오른쪽 서브트리에서 삭제
                node.right = self._delete(node.right, successor_val)

        return node

    def _find_min(self, node: BSTNode) -> int:
        """서브트리의 최솟값 (가장 왼쪽).

        Time:  O(h)
        Space: O(1)
        """
        curr = node
        while curr.left:
            curr = curr.left
        return curr.val

    def _find_max(self, node: BSTNode) -> int:
        """서브트리의 최댓값 (가장 오른쪽).

        Time:  O(h)
        Space: O(1)
        """
        curr = node
        while curr.right:
            curr = curr.right
        return curr.val

    def inorder(self) -> list[int]:
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: BSTNode | None, result: list[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    def make_bst(values: list[int]) -> BST:
        bst = BST()
        for v in values:
            bst.insert(v)
        return bst

    print("=== 경우 1: 리프 노드 삭제 ===")
    #       8
    #      / \
    #     3   10
    #    / \
    #   1   6
    bst = make_bst([8, 3, 10, 1, 6])
    print(f"삭제 전: {bst.inorder()}")
    bst.delete(1)   # 리프 삭제
    print(f"delete(1): {bst.inorder()}")
    bst.delete(6)   # 리프 삭제
    print(f"delete(6): {bst.inorder()}")

    print("\n=== 경우 2: 자식 1개 노드 삭제 ===")
    #       8
    #      / \
    #     3   10
    #          \
    #           14
    bst2 = make_bst([8, 3, 10, 14])
    print(f"삭제 전: {bst2.inorder()}")
    bst2.delete(10)  # 오른쪽 자식만 있는 노드
    print(f"delete(10): {bst2.inorder()}")

    print("\n=== 경우 3: 자식 2개 노드 삭제 ===")
    #           8
    #          / \
    #         3   10
    #        / \    \
    #       1   6    14
    #          / \   /
    #         4   7 13
    bst3 = make_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
    print(f"삭제 전:  {bst3.inorder()}")

    bst3.delete(3)   # 자식 2개 (후계자 = 4)
    print(f"delete(3): {bst3.inorder()}")

    bst3.delete(8)   # 루트 삭제 (후계자 = 10)
    print(f"delete(8): {bst3.inorder()}")

    print("\n=== 없는 값 삭제 (에러 없어야 함) ===")
    bst3.delete(999)
    print(f"delete(999): {bst3.inorder()}")
