# 백준 1764 -- 듣보잡
# Time : O(N + M + K log K) -- K = 교집합 크기
# Space: O(N) -- 첫 번째 목록을 set에 저장
#
# 풀이: 첫 번째 목록을 set에 저장한 뒤,
# 두 번째 목록 순회 시 set에 있으면 결과에 추가. 사전순 정렬.

import sys

input = sys.stdin.readline


def solve() -> None:
    n, m = map(int, input().split())
    not_heard: set[str] = set()

    for _ in range(n):
        not_heard.add(input().strip())

    result = []
    for _ in range(m):
        name = input().strip()
        if name in not_heard:
            result.append(name)

    result.sort()
    print(len(result))
    print("\n".join(result))


solve()
