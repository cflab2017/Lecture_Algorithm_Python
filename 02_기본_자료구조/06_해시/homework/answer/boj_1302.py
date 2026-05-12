# 백준 1302 -- 베스트셀러
# Time : O(N log N) -- Counter 생성 O(N), max O(N), 동점 처리용 정렬
# Space: O(N) -- Counter 크기
#
# 풀이: Counter로 각 책의 판매 횟수를 센다.
# 최대 판매 횟수를 구한 뒤, 그 횟수를 가진 책들 중 사전순 첫 번째를 출력.

import sys
from collections import Counter

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    cnt: Counter[str] = Counter()

    for _ in range(n):
        book = input().strip()
        cnt[book] += 1

    max_count = max(cnt.values())
    # 최대 판매 책들 중 사전순 최솟값
    best = min(book for book, c in cnt.items() if c == max_count)
    print(best)


solve()
