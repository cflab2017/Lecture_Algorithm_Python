# Topic : 이중 연결 리스트 (Doubly Linked List)
# Time  : insert/delete O(1) at known node, search O(n)
# Space : O(n) -- 노드 수 (각 노드 prev+next 오버헤드)

from __future__ import annotations
from typing import Any


class DNode:
    """이중 연결 리스트 노드 -- prev와 next 포인터 보유."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.prev: DNode | None = None
        self.next: DNode | None = None


class DoublyLinkedList:
    """이중 연결 리스트."""

    def __init__(self) -> None:
        self.head: DNode | None = None
        self.tail: DNode | None = None
        self._size: int = 0

    def append(self, data: Any) -> None:
        """맨 뒤에 추가 -- O(1)."""
        new_node = DNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """맨 앞에 추가 -- O(1)."""
        new_node = DNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def insert_after(self, node: DNode, data: Any) -> None:
        """특정 노드 뒤에 삽입 -- O(1)."""
        new_node = DNode(data)
        new_node.prev = node
        new_node.next = node.next

        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node   # node가 tail이었음

        node.next = new_node
        self._size += 1

    def delete_node(self, node: DNode) -> None:
        """노드 직접 삭제 -- O(1) (노드 참조가 있을 때)."""
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next   # head 삭제

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev   # tail 삭제

        self._size -= 1

    def delete_by_value(self, data: Any) -> bool:
        """값으로 삭제 -- O(n)."""
        cur = self.head
        while cur is not None:
            if cur.data == data:
                self.delete_node(cur)
                return True
            cur = cur.next
        return False

    def display_forward(self) -> str:
        """앞에서 뒤로 출력."""
        parts = []
        cur = self.head
        while cur is not None:
            parts.append(str(cur.data))
            cur = cur.next
        return " <-> ".join(parts)

    def display_backward(self) -> str:
        """뒤에서 앞으로 출력."""
        parts = []
        cur = self.tail
        while cur is not None:
            parts.append(str(cur.data))
            cur = cur.prev
        return " <-> ".join(parts)

    def size(self) -> int:
        return self._size


if __name__ == "__main__":
    print("=" * 55)
    print("이중 연결 리스트 데모")
    print("=" * 55)

    dll = DoublyLinkedList()

    for v in [1, 2, 3, 4, 5]:
        dll.append(v)

    print("초기:", dll.display_forward())
    print("역방향:", dll.display_backward())

    print()
    dll.prepend(0)
    print("prepend(0):", dll.display_forward())

    # 특정 노드 뒤에 삽입
    cur = dll.head
    while cur and cur.data != 3:
        cur = cur.next
    if cur:
        dll.insert_after(cur, 99)
        print("insert_after(3, 99):", dll.display_forward())

    print()
    for v in [0, 3, 99, 5]:
        dll.delete_by_value(v)
        print(f"delete({v}): {dll.display_forward()}")

    print()
    print(f"최종 크기: {dll.size()}")
    print("역방향 확인:", dll.display_backward())
