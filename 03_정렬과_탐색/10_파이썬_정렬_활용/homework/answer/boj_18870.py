"""
백준 18870 – 좌표 압축
https://www.acmicpc.net/problem/18870
Time  : O(n log n)
Space : O(n)

전략: 중복 제거 → 정렬 → 순위 딕셔너리로 O(1) 변환
"""

import sys
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    # 중복 제거 + 정렬 → 순위 매핑
    sorted_unique = sorted(set(arr))
    rank = {v: i for i, v in enumerate(sorted_unique)}

    print(' '.join(str(rank[v]) for v in arr))


if __name__ == "__main__":
    main()
