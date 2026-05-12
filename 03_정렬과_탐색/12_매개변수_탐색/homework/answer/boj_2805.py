"""
백준 2805 – 나무 자르기
https://www.acmicpc.net/problem/2805
Time  : O(N log(max_height))
Space : O(N)
"""

import sys
input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    def feasible(h: int) -> bool:
        return sum(t - h for t in trees if t > h) >= m

    left, right = 0, max(trees)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


if __name__ == "__main__":
    main()
