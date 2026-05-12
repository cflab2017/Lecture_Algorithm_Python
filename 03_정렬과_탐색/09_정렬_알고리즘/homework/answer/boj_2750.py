"""
백준 2750 – 수 정렬하기
https://www.acmicpc.net/problem/2750
Time  : O(n²)   (버블 정렬)
Space : O(1)    (in-place)

제한: N ≤ 1,000 → O(n²) 충분
"""

import sys
input = sys.stdin.readline


def bubble_sort(arr: list[int]) -> None:
    """버블 정렬 (in-place)."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def main() -> None:
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    bubble_sort(arr)
    print('\n'.join(map(str, arr)))


if __name__ == "__main__":
    main()
