# 백준 5397 -- 키로거
# Time : O(N) -- 각 입력 문자열 길이 N 처리
# Space: O(N) -- deque 두 개
#
# 풀이: 커서를 기준으로 left / right deque 분리.
#   '<': left -> right (왼쪽 이동)
#   '>': right -> left (오른쪽 이동)
#   '-': left에서 pop (커서 왼쪽 삭제)
#   나머지: left에 append (문자 삽입)

import sys
from collections import deque

input = sys.stdin.readline


def keylogger(s: str) -> str:
    """키로거 시뮬레이션."""
    left: deque[str]  = deque()
    right: deque[str] = deque()

    for ch in s:
        if ch == "<":
            if left:
                right.appendleft(left.pop())
        elif ch == ">":
            if right:
                left.append(right.popleft())
        elif ch == "-":
            if left:
                left.pop()
        else:
            left.append(ch)

    left.extend(right)
    return "".join(left)


def solve() -> None:
    t = int(input())
    output = []
    for _ in range(t):
        s = input().strip()
        output.append(keylogger(s))
    print("\n".join(output))


solve()
