"""
백준 11650 – 좌표 정렬하기
https://www.acmicpc.net/problem/11650
Time  : O(n log n)
Space : O(n)

전략: 튜플 (x, y) 기본 비교 정렬
"""

import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    coords.sort()      # (x, y) 튜플 기본 비교: x 같으면 y 비교
    out = '\n'.join(f"{x} {y}" for x, y in coords)
    print(out)


if __name__ == "__main__":
    main()
