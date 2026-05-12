# 백준 1406 -- 에디터
# Time : O(N + M) -- 초기 문자열 N, 명령 M
# Space: O(N + M) -- deque 두 개
#
# 풀이: 커서를 기준으로 left deque / right deque 분리.
#   L: left -> right (왼쪽 이동)
#   D: right -> left (오른쪽 이동)
#   B: left에서 pop (커서 왼쪽 삭제)
#   P $: left에 $를 append

import sys
from collections import deque

input = sys.stdin.readline


def solve() -> None:
    s = input().strip()
    left: deque[str]  = deque(s)   # 커서 왼쪽
    right: deque[str] = deque()    # 커서 오른쪽

    m = int(input())
    for _ in range(m):
        cmd = input().split()
        op = cmd[0]

        if op == "L":
            if left:
                right.appendleft(left.pop())
        elif op == "D":
            if right:
                left.append(right.popleft())
        elif op == "B":
            if left:
                left.pop()
        elif op == "P":
            left.append(cmd[1])

    left.extend(right)
    sys.stdout.write("".join(left) + "\n")


solve()
