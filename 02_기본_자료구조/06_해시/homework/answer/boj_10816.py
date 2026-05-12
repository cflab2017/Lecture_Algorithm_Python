# 백준 10816 -- 숫자 카드 2
# Time : O(N + M) -- Counter 생성 O(N), M번 조회 O(M)
# Space: O(N) -- Counter 크기
#
# 풀이: Counter로 상근이 카드의 등장 횟수를 기록한 뒤,
# M개의 숫자에 대해 각각 count를 출력한다.

import sys
from collections import Counter

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    cards = Counter(map(int, input().split()))

    m = int(input())
    queries = map(int, input().split())

    print(*[cards[q] for q in queries])


solve()
