# Topic : 원형 연결 리스트 (Circular Linked List)
# Time  : append O(1), delete O(n), traverse O(n)
# Space : O(n) -- 노드 수

from __future__ import annotations
from typing import Any


class CNode:
    """원형 연결 리스트 노드."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: CNode | None = None


class CircularLinkedList:
    """원형 단순 연결 리스트.

    마지막 노드의 next가 head를 가리킨다.

    구조:
      head
       |
      [1] -> [2] -> [3] -> [4]
       ^                    |
       +--------------------+
    """

    def __init__(self) -> None:
        self.head: CNode | None = None
        self._size: int = 0

    def append(self, data: Any) -> None:
        """맨 뒤에 노드 추가 -- O(n) (tail 없이 head에서 순회)."""
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head   # 자기 자신을 가리킴
        else:
            # 마지막 노드 찾기
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next  # type: ignore[assignment]
            tail.next = new_node
            new_node.next = self.head
        self._size += 1

    def prepend(self, data: Any) -> None:
        """맨 앞에 노드 추가 -- O(n) (tail을 업데이트해야 하므로 순회 필요)."""
        new_node = CNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next  # type: ignore[assignment]
            new_node.next = self.head
            tail.next = new_node
            self.head = new_node
        self._size += 1

    def delete(self, data: Any) -> bool:
        """값이 data인 첫 번째 노드 삭제 -- O(n)."""
        if self.head is None:
            return False

        # head 삭제 특수 처리
        if self.head.data == data:
            if self._size == 1:
                self.head = None
            else:
                # tail의 next를 새 head로
                tail = self.head
                while tail.next is not self.head:
                    tail = tail.next  # type: ignore[assignment]
                tail.next = self.head.next
                self.head = self.head.next
            self._size -= 1
            return True

        prev = self.head
        cur  = self.head.next
        while cur is not self.head:
            if cur.data == data:  # type: ignore[union-attr]
                prev.next = cur.next  # type: ignore[union-attr]
                self._size -= 1
                return True
            prev = cur  # type: ignore[assignment]
            cur  = cur.next  # type: ignore[union-attr]
        return False

    def display(self, max_steps: int = 20) -> str:
        """리스트를 문자열로 표현 (최대 max_steps개)."""
        if self.head is None:
            return "Empty"
        parts = []
        cur = self.head
        steps = 0
        while steps < max_steps:
            parts.append(str(cur.data))
            cur = cur.next  # type: ignore[assignment]
            steps += 1
            if cur is self.head:
                break
        return " -> ".join(parts) + " -> (head)"

    def josephus(self, k: int) -> list[Any]:
        """요세푸스 문제: k번째마다 제거하는 순서 반환 -- O(n*k)."""
        if self.head is None:
            return []
        order = []
        cur = self.head
        while self._size > 0:
            for _ in range(k - 1):
                cur = cur.next  # type: ignore[assignment]
            order.append(cur.data)
            next_cur = cur.next
            self.delete(cur.data)
            cur = next_cur if self.head else None
        return order

    def size(self) -> int:
        return self._size


if __name__ == "__main__":
    print("=" * 55)
    print("원형 연결 리스트 데모")
    print("=" * 55)

    cll = CircularLinkedList()

    for v in [1, 2, 3, 4, 5]:
        cll.append(v)
        print(f"append({v}): {cll.display()}")

    print()
    cll.prepend(0)
    print(f"prepend(0): {cll.display()}")

    print()
    for v in [0, 3, 5]:
        deleted = cll.delete(v)
        print(f"delete({v}) -> {'성공' if deleted else '없음'}: {cll.display()}")

    print()
    print("=" * 55)
    print("요세푸스 문제 (n=6, k=2)")
    print("=" * 55)
    cll2 = CircularLinkedList()
    for v in range(1, 7):
        cll2.append(v)
    order = cll2.josephus(2)
    print("제거 순서:", order)
