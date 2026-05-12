# 백준 11286 -- 절댓값 힙
# Time : O(N log N) -- N번 push/pop
# Space: O(N) -- 힙 크기
#
# 풀이: 튜플 (|x|, x) 를 힙에 저장.
# |x|가 같으면 x값이 작은 것(음수)이 먼저 나온다.
# 예: (-1, -1) vs (1, 1) -> (-1, -1)의 두 번째 원소 -1 < 1 -> 음수 먼저

import sys
import heapq

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    h: list[tuple[int, int]] = []
    output: list[str] = []

    for _ in range(n):
        x = int(input())
        if x == 0:
            if h:
                _, val = heapq.heappop(h)
                output.append(str(val))
            else:
                output.append("0")
        else:
            heapq.heappush(h, (abs(x), x))

    print("\n".join(output))


solve()
