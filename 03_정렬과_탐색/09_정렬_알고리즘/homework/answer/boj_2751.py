"""
백준 2751 – 수 정렬하기 2
https://www.acmicpc.net/problem/2751
Time  : O(n log n)   (Timsort / 병합 정렬)
Space : O(n)

제한: N ≤ 1,000,000 → O(n²) 시간 초과, O(n log n) 필요
     빠른 입출력(sys.stdin) 필수
"""

import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()                          # Timsort O(n log n)
    sys.stdout.write('\n'.join(map(str, arr)) + '\n')


if __name__ == "__main__":
    main()
