# 백준 2957 — 이진 탐색 트리
# https://www.acmicpc.net/problem/2957
# Time: O(n log n)  Space: O(n)
# 삽입 비교 횟수의 누적 합

import sys
from sortedcontainers import SortedList  # type: ignore

input = sys.stdin.readline


def solve() -> None:
    n = int(input())

    # SortedList: O(log n) 삽입/탐색
    sl: SortedList = SortedList()
    depth: dict[int, int] = {}   # 각 값의 깊이

    # 센티넬: BST 경계
    sl.add(0)
    sl.add(n + 1)
    depth[0] = depth[n + 1] = 0

    total = 0
    output: list[str] = []

    for _ in range(n):
        val = int(input())

        # 삽입 위치 찾기
        idx = sl.bisect_left(val)

        # predecessor = sl[idx - 1], successor = sl[idx]
        pred = sl[idx - 1]
        succ = sl[idx]

        # 더 나중에 삽입된 것(= 더 깊은 것)이 부모
        parent_depth = max(depth[pred], depth[succ])
        depth[val] = parent_depth + 1
        total += parent_depth  # 비교 횟수 = 깊이 (루트 삽입 시 0번 비교)

        sl.add(val)
        output.append(str(total))

    sys.stdout.write("\n".join(output) + "\n")


solve()
