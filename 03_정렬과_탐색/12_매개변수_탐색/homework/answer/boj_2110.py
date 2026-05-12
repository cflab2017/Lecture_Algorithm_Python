"""
백준 2110 – 공유기 설치
https://www.acmicpc.net/problem/2110
Time  : O(N log N + N log(max_dist))
Space : O(N)

전략: 최솟값의 최댓값 → 매개변수 탐색
결정 함수: 최소 거리 d 이상 유지하며 C개 설치 가능?
"""

import sys
input = sys.stdin.readline


def main() -> None:
    n, c = map(int, input().split())
    houses = sorted(int(input()) for _ in range(n))

    def feasible(d: int) -> bool:
        """최소 거리 d 이상 유지하며 C개 설치 가능?"""
        count = 1
        last = houses[0]
        for h in houses[1:]:
            if h - last >= d:
                count += 1
                last = h
                if count >= c:
                    return True
        return count >= c

    left, right = 1, houses[-1] - houses[0]
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            answer = mid
            left = mid + 1      # 거리를 더 벌려 봄
        else:
            right = mid - 1     # 거리를 줄여야 함

    print(answer)


if __name__ == "__main__":
    main()
