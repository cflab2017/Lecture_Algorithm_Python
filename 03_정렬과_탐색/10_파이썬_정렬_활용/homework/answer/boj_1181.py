"""
백준 1181 – 단어 정렬
https://www.acmicpc.net/problem/1181
Time  : O(n log n)
Space : O(n)

전략: 중복 제거 후 (길이, 사전순) 다중 기준 정렬
"""

import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    words = {input().rstrip() for _ in range(n)}   # set으로 중복 제거
    result = sorted(words, key=lambda w: (len(w), w))
    print('\n'.join(result))


if __name__ == "__main__":
    main()
