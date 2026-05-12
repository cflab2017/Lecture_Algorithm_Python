# Topic : 스택 기초 -- push, pop, peek, 언더플로, DFS 시뮬레이션
# Time  : push O(1), pop O(1), peek O(1)
# Space : O(n) -- 스택에 저장된 원소 수

from __future__ import annotations


class Stack:
    """리스트 기반 스택 구현."""

    def __init__(self) -> None:
        self._data: list[int] = []

    def push(self, val: int) -> None:
        """스택 최상단에 원소 추가 -- O(1) 균상."""
        self._data.append(val)

    def pop(self) -> int:
        """스택 최상단 원소 제거 후 반환 -- O(1).

        Raises:
            IndexError: 스택이 비어있을 때.
        """
        if self.is_empty():
            raise IndexError("스택 언더플로: 빈 스택에서 pop 시도")
        return self._data.pop()

    def peek(self) -> int:
        """제거 없이 최상단 원소 반환 -- O(1)."""
        if self.is_empty():
            raise IndexError("스택이 비어있습니다")
        return self._data[-1]

    def is_empty(self) -> bool:
        """스택이 비어있으면 True -- O(1)."""
        return len(self._data) == 0

    def size(self) -> int:
        """스택 원소 수 반환 -- O(1)."""
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack(bottom->top): {self._data}"


def demo_basic_operations() -> None:
    """스택 기본 연산 데모."""
    print("=" * 50)
    print("스택 기본 연산")
    print("=" * 50)

    s = Stack()
    for val in [1, 3, 5, 7, 9]:
        s.push(val)
        print(f"push({val:2}) -> {s}")

    print()
    while not s.is_empty():
        val = s.pop()
        print(f"pop() -> {val:2}  {s}")

    # 언더플로 처리
    print()
    try:
        s.pop()
    except IndexError as e:
        print(f"언더플로 처리: {e}")


def dfs_iterative(graph: dict[int, list[int]], start: int) -> list[int]:
    """명시적 스택을 이용한 반복적 DFS -- Time O(V+E), Space O(V).

    재귀 대신 스택을 직접 사용하여 DFS를 구현한다.
    """
    visited: list[int] = []
    seen: set[int] = set()
    stack: list[int] = [start]

    while stack:
        node = stack.pop()      # 스택 LIFO -> DFS
        if node in seen:
            continue
        seen.add(node)
        visited.append(node)
        # 이웃 노드를 역순으로 push (방문 순서 일관성)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in seen:
                stack.append(neighbor)

    return visited


def demo_dfs() -> None:
    """그래프 DFS 시뮬레이션."""
    print()
    print("=" * 50)
    print("스택 기반 DFS 시뮬레이션")
    print("=" * 50)

    #   1
    #  / \\
    # 2   3
    # |   |
    # 4   5
    graph = {
        1: [2, 3],
        2: [4],
        3: [5],
        4: [],
        5: [],
    }
    print("그래프:", graph)
    order = dfs_iterative(graph, start=1)
    print("DFS 방문 순서 (시작=1):", order)   # [1, 2, 4, 3, 5]


if __name__ == "__main__":
    demo_basic_operations()
    demo_dfs()
