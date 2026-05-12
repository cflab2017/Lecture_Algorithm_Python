# 백준 10845 -- 큐
# Time : O(N) -- 명령 수 N
# Space: O(N) -- 큐 크기
#
# 풀이: collections.deque 로 큐를 구현하고 명령어에 따라 처리.

import sys
from collections import deque

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    queue: deque[int] = deque()
    output: list[str] = []

    for _ in range(n):
        cmd = input().split()
        op = cmd[0]

        if op == "push":
            queue.append(int(cmd[1]))
        elif op == "pop":
            output.append(str(queue.popleft()) if queue else "-1")
        elif op == "size":
            output.append(str(len(queue)))
        elif op == "empty":
            output.append("1" if not queue else "0")
        elif op == "front":
            output.append(str(queue[0]) if queue else "-1")
        elif op == "back":
            output.append(str(queue[-1]) if queue else "-1")

    print("\n".join(output))


solve()
