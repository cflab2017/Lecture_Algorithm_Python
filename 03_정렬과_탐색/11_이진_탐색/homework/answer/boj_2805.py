"""
백준 2805 – 나무 자르기
https://www.acmicpc.net/problem/2805
Time  : O(N log(max_height))
Space : O(N)

전략: 매개변수 탐색 — 높이 H에 대한 이진 탐색
"""

import sys
input = sys.stdin.readline


def can_collect(trees: list[int], height: int, need: int) -> bool:
    """절단 높이 height 로 need 이상 수집 가능한가?"""
    return sum(t - height for t in trees if t > height) >= need


def main() -> None:
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    left, right = 0, max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_collect(trees, mid, m):
            answer = mid          # 가능한 최댓값 갱신
            left = mid + 1        # 더 높이 시도
        else:
            right = mid - 1       # 낮춰야 함

    print(answer)


if __name__ == "__main__":
    main()
