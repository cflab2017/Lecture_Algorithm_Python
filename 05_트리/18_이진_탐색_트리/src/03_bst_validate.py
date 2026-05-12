# 주제: BST 검증, k번째 최솟값
# Time: O(n) — 검증/k번째 모두
# Space: O(h) — 재귀 스택

from __future__ import annotations
import math


class BSTNode:
    def __init__(self, val: int,
                 left: "BSTNode | None" = None,
                 right: "BSTNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: BSTNode | None) -> bool:
    """BST 유효성 검증.

    핵심: 단순히 left.val < node.val < right.val 만 확인하면 틀림!
    각 노드는 [min_bound, max_bound] 범위 내에 있어야 함.

    예: 아래는 local은 맞지만 BST 위반:
           5
          / \\
         1   4
            / \\
           3   6
    (4의 오른쪽 6은 루트 5보다 크므로 위반)

    Time:  O(n)
    Space: O(h)
    """
    def validate(
        node: BSTNode | None,
        min_val: float,
        max_val: float,
    ) -> bool:
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (
            validate(node.left, min_val, node.val)
            and validate(node.right, node.val, max_val)
        )

    return validate(root, -math.inf, math.inf)


def kth_smallest(root: BSTNode | None, k: int) -> int:
    """k번째 최솟값 (1-indexed).

    중위 순회(왼쪽→현재→오른쪽)가 오름차순이므로 k번째 방문 노드가 답.

    Time:  O(h + k) — 최선 O(log n), 최악 O(n)
    Space: O(h)
    """
    count = 0
    result = -1

    def inorder(node: BSTNode | None) -> None:
        nonlocal count, result
        if node is None or count >= k:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result


def kth_smallest_iterative(root: BSTNode | None, k: int) -> int:
    """k번째 최솟값 — 반복(스택) 방식.

    Time:  O(h + k)
    Space: O(h)
    """
    stack: list[BSTNode] = []
    curr: BSTNode | None = root
    count = 0

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val

        curr = curr.right

    return -1  # k > 노드 수


def inorder_successor(root: BSTNode | None, target: int) -> int | None:
    """중위 후계자 (target보다 큰 가장 작은 값).

    Time:  O(h)
    Space: O(1)
    """
    successor: int | None = None
    curr = root

    while curr:
        if target < curr.val:
            successor = curr.val   # 후보 갱신
            curr = curr.left
        else:
            curr = curr.right      # target 이상이면 오른쪽

    return successor


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 유효한 BST
    #       5
    #      / \
    #     3   7
    #    / \ / \
    #   1  4 6  8
    valid_root = BSTNode(5,
        BSTNode(3, BSTNode(1), BSTNode(4)),
        BSTNode(7, BSTNode(6), BSTNode(8))
    )

    # 유효하지 않은 BST (3의 오른쪽이 4이지만 루트 5 아래 왼쪽에서 4 > 3이지만 5 미만 OK,
    # 아래 예시는 명확한 위반)
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    invalid_root = BSTNode(5,
        BSTNode(1),
        BSTNode(4, BSTNode(3), BSTNode(6))
    )

    print("=== BST 유효성 검증 ===")
    print(f"유효한 BST:     {is_valid_bst(valid_root)}")   # True
    print(f"유효하지 않은:  {is_valid_bst(invalid_root)}")  # False

    print("\n=== k번째 최솟값 ===")
    for k in range(1, 8):
        val_r = kth_smallest(valid_root, k)
        val_i = kth_smallest_iterative(valid_root, k)
        print(f"  k={k}: 재귀={val_r}, 반복={val_i}")

    print("\n=== 중위 후계자 ===")
    for target in [3, 5, 7, 8]:
        succ = inorder_successor(valid_root, target)
        print(f"  {target}의 후계자: {succ}")
