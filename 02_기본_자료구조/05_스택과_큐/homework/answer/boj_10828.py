# 백준 10828 -- 스택
# Time : O(N) -- 명령 수 N
# Space: O(N) -- 스택 크기
#
# 풀이: Python list 로 스택을 구현하고 명령어에 따라 처리.

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    stack: list[int] = []
    output: list[str] = []

    for _ in range(n):
        cmd = input().split()
        op = cmd[0]

        if op == "push":
            stack.append(int(cmd[1]))
        elif op == "pop":
            output.append(str(stack.pop()) if stack else "-1")
        elif op == "size":
            output.append(str(len(stack)))
        elif op == "empty":
            output.append("1" if not stack else "0")
        elif op == "top":
            output.append(str(stack[-1]) if stack else "-1")

    print("\n".join(output))


solve()
