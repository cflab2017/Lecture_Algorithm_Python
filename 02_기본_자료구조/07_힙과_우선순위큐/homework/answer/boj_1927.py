# 백준 1927 -- 최소 힙
# Time : O(N log N) -- N번 push/pop
# Space: O(N) -- 힙 크기
#
# 풀이: Python heapq는 기본이 min-heap.
# x == 0 이면 pop (빈 힙이면 0 출력), 아니면 push.

import sys
import heapq

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    h: list[int] = []
    output: list[str] = []

    for _ in range(n):
        x = int(input())
        if x == 0:
            output.append(str(heapq.heappop(h)) if h else "0")
        else:
            heapq.heappush(h, x)

    print("\n".join(output))


solve()
