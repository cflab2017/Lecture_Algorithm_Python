# 백준 9012 -- 괄호
# Time : O(N * K) -- 테스트케이스 N개, 각 문자열 길이 K
# Space: O(K)    -- 스택 크기
#
# 풀이: '(' 는 push, ')' 는 pop (스택이 비면 NO).
# 전체 처리 후 스택이 비어있으면 YES.

import sys

input = sys.stdin.readline


def is_vps(s: str) -> str:
    stack: list[str] = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:  # ch == ')'
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"


def solve() -> None:
    t = int(input())
    results = []
    for _ in range(t):
        s = input().strip()
        results.append(is_vps(s))
    print("\n".join(results))


solve()
