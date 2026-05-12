# 백준 11279 -- 최대 힙
# Time : O(N log N) -- N번 push/pop
# Space: O(N) -- 힙 크기
#
# 풀이: 음수 변환 트릭.
# push 시 -x 로 저장, pop 시 -결과 로 부호 복원.

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
            output.append(str(-heapq.heappop(h)) if h else "0")
        else:
            heapq.heappush(h, -x)   # 음수로 저장 (max-heap 트릭)

    print("\n".join(output))


solve()
