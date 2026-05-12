# Topic : 단순 연결 리스트 (Singly Linked List) 완전 구현
# Time  : append O(1), prepend O(1), delete O(n), search O(n)
# Space : O(n) -- 노드 수

from __future__ import annotations
from typing import Any


class Node:
    """연결 리스트의 노드."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Node | None = None


class SinglyLinkedList:
    """단순 연결 리스트."""

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def append(self, data: Any) -> None:
        """맨 뒤에 노드 추가 -- O(1) (tail 포인터 활용)."""
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """맨 앞에 노드 추가 -- O(1)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def delete(self, data: Any) -> bool:
        """값이 data인 첫 번째 노드 삭제 -- O(n).

        Returns:
            True if deleted, False if not found.
        """
        if self.head is None:
            return False

        # head 노드가 삭제 대상인 경우
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True

        # 중간 또는 끝 노드 탐색
        prev = self.head
        cur  = self.head.next
        while cur is not None:
            if cur.data == data:
                prev.next = cur.next
                if cur.next is None:    # tail 삭제
                    self.tail = prev
                self._size -= 1
                return True
            prev = cur
            cur  = cur.next
        return False

    def search(self, data: Any) -> int:
        """값이 data인 노드의 인덱스 반환 -- O(n). 없으면 -1."""
        idx = 0
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def get(self, index: int) -> Any:
        """인덱스로 값 조회 -- O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError(f"인덱스 {index} 범위 초과 (크기: {self._size})")
        cur = self.head
        for _ in range(index):
            cur = cur.next  # type: ignore[union-attr]
        return cur.data  # type: ignore[union-attr]

    def size(self) -> int:
        """리스트 크기 -- O(1)."""
        return self._size

    def display(self) -> str:
        """리스트를 문자열로 표현."""
        parts = []
        cur = self.head
        while cur is not None:
            parts.append(str(cur.data))
            cur = cur.next
        return " -> ".join(parts) + " -> None"


if __name__ == "__main__":
    print("=" * 55)
    print("단순 연결 리스트 데모")
    print("=" * 55)

    ll = SinglyLinkedList()

    # append
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
        print(f"append({v}): {ll.display()}")

    print()
    # prepend
    ll.prepend(0)
    print(f"prepend(0): {ll.display()}")

    print()
    # search
    for v in [0, 3, 9]:
        idx = ll.search(v)
        print(f"search({v}) -> 인덱스 {idx}")

    print()
    # get
    for i in [0, 3, 5]:
        print(f"get({i}) -> {ll.get(i)}")

    print()
    # delete
    for v in [0, 3, 5, 99]:
        deleted = ll.delete(v)
        print(f"delete({v}) -> {'성공' if deleted else '없음'}: {ll.display()}")

    print()
    print(f"최종 크기: {ll.size()}")
