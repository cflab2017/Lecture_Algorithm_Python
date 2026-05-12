# Topic : 연결 리스트 주요 문제 -- 역전, 사이클 감지, 중앙 노드
# Time  : reverse O(n), cycle O(n), middle O(n)
# Space : reverse O(1), cycle O(1), middle O(1)

from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


def build_list(values: list[Any]) -> Node | None:
    """리스트로 연결 리스트 생성 (헬퍼 함수)."""
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head


def to_list(head: Node | None) -> list[Any]:
    """연결 리스트를 Python list로 변환 (헬퍼 함수)."""
    result = []
    cur = head
    while cur is not None:
        result.append(cur.data)
        cur = cur.next
    return result


# ------------------------------------------------------------------
# 1. 연결 리스트 역전 (Reverse)
# ------------------------------------------------------------------
def reverse_iterative(head: Node | None) -> Node | None:
    """반복적 역전 -- Time O(n), Space O(1).

    포인터 3개 사용:
      prev: 이전 노드
      cur : 현재 노드
      nxt : 다음 노드 (임시 저장)
    """
    prev: Node | None = None
    cur = head
    while cur is not None:
        nxt = cur.next      # 1. 다음 노드 저장
        cur.next = prev     # 2. 방향 역전
        prev = cur          # 3. prev 전진
        cur = nxt           # 4. cur 전진
    return prev             # 새 head


def reverse_recursive(head: Node | None) -> Node | None:
    """재귀적 역전 -- Time O(n), Space O(n) 콜스택.

    기저 조건: 노드가 없거나 단일 노드.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head   # 뒤 노드가 현재를 가리킴
    head.next = None        # 현재는 마지막 노드가 됨
    return new_head


# ------------------------------------------------------------------
# 2. 사이클 감지 -- Floyd's Tortoise and Hare
# ------------------------------------------------------------------
def has_cycle(head: Node | None) -> bool:
    """사이클 존재 여부 반환 -- Time O(n), Space O(1).

    느린 포인터(1칸) vs 빠른 포인터(2칸):
    사이클이 있으면 두 포인터가 반드시 만난다.
    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next          # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def find_cycle_start(head: Node | None) -> Node | None:
    """사이클 시작 노드 반환 -- Time O(n), Space O(1).

    Floyd's 알고리즘 2단계:
    1단계: 느린/빠른 포인터로 만남 지점 탐색
    2단계: 한 포인터를 head로 이동 후 동시에 1칸씩 이동
           -> 만나는 지점이 사이클 시작
    """
    slow = head
    fast = head

    # 1단계: 만남 지점 찾기
    while fast is not None and fast.next is not None:
        slow = slow.next          # type: ignore[union-attr]
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None   # 사이클 없음

    # 2단계: head와 만남 지점에서 동시 이동
    slow = head
    while slow is not fast:
        slow = slow.next  # type: ignore[union-attr]
        fast = fast.next  # type: ignore[union-attr]
    return slow


# ------------------------------------------------------------------
# 3. 중앙 노드 찾기 (Fast & Slow Pointer)
# ------------------------------------------------------------------
def find_middle(head: Node | None) -> Node | None:
    """연결 리스트 중앙 노드 반환 -- Time O(n), Space O(1).

    느린(1칸) / 빠른(2칸) 포인터:
    빠른 포인터가 끝에 도달하면 느린 포인터가 중앙.
    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next          # type: ignore[union-attr]
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    print("=" * 55)
    print("연결 리스트 역전")
    print("=" * 55)

    test_cases = [[1, 2, 3, 4, 5], [1], [], [1, 2]]
    for vals in test_cases:
        head = build_list(vals)
        rev_iter = reverse_iterative(build_list(vals))
        rev_rec  = reverse_recursive(build_list(vals))
        print(
            f"{vals} -> "
            f"반복: {to_list(rev_iter)} | "
            f"재귀: {to_list(rev_rec)}"
        )

    print()
    print("=" * 55)
    print("사이클 감지 -- Floyd's 알고리즘")
    print("=" * 55)

    # 사이클 없는 리스트
    head_no_cycle = build_list([1, 2, 3, 4, 5])
    print("사이클 없음:", has_cycle(head_no_cycle))  # False

    # 사이클 있는 리스트 직접 생성
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5
    n5.next = n3   # 사이클: 5 -> 3
    print("사이클 있음:", has_cycle(n1))  # True
    start = find_cycle_start(n1)
    print("사이클 시작 노드:", start.data if start else None)  # 3

    print()
    print("=" * 55)
    print("중앙 노드 찾기")
    print("=" * 55)
    for vals in [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6], [1]]:
        head = build_list(vals)
        mid = find_middle(head)
        print(f"{vals} -> 중앙: {mid.data if mid else None}")
