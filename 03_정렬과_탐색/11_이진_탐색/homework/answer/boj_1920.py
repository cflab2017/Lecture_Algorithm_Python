"""
백준 1920 – 수 찾기
https://www.acmicpc.net/problem/1920
Time  : O((N+M) log N)
Space : O(N)
"""

import sys
from bisect import bisect_left

input = sys.stdin.readline


def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    m = int(input())
    queries = list(map(int, input().split()))

    result = []
    for q in queries:
        idx = bisect_left(arr, q)
        result.append('1' if idx < len(arr) and arr[idx] == q else '0')

    print('\n'.join(result))


if __name__ == "__main__":
    main()
