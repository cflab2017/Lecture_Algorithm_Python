"""
백준 10816 – 숫자 카드 2
https://www.acmicpc.net/problem/10816
Time  : O((N+M) log N)
Space : O(N)

전략: 카드 정렬 후 bisect_right - bisect_left 로 개수 계산
"""

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main() -> None:
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()

    m = int(input())
    queries = list(map(int, input().split()))

    result = [
        bisect_right(cards, q) - bisect_left(cards, q)
        for q in queries
    ]
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
