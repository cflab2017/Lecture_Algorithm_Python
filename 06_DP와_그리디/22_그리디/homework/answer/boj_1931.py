# 백준 1931 — 회의실 배정
# https://www.acmicpc.net/problem/1931
# Time: O(n log n)  Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]

    # 종료 시간 기준, 같으면 시작 시간 기준 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end = 0

    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end

    print(count)


solve()
