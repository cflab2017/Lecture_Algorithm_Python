# 백준 10808 -- 알파벳 개수
# Time : O(n) -- 문자열 길이 n
# Space: O(1) -- 크기 26 배열 (알파벳 수 고정)
#
# 풀이: 크기 26인 배열에 각 알파벳의 등장 횟수를 누적한다.
# ord(c) - ord('a') 로 a=0, b=1, ..., z=25 인덱스로 변환.

import sys

input = sys.stdin.readline


def solve() -> None:
    s = input().strip()
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord("a")] += 1
    print(*count)


solve()
