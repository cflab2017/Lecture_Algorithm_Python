# =============================================================================
# 백준 2750번: 수 정렬하기
# 링크: https://www.acmicpc.net/problem/2750
# 방법 1 — 버블 정렬:
#   시간복잡도: O(n²) — 이중 루프
#   공간복잡도: O(1) — 제자리 정렬
# 방법 2 — sorted():
#   시간복잡도: O(n log n) — Timsort 알고리즘
#   공간복잡도: O(n) — 정렬된 결과 배열
#
# 분석: N ≤ 1,000이므로 두 방법 모두 통과합니다.
#       그러나 N = 100,000이라면 버블정렬은 TLE, sorted()는 통과합니다.
# =============================================================================

import sys


# ---------------------------------------------------------------------------
# 방법 1: 버블 정렬 — O(n²)
# ---------------------------------------------------------------------------
def bubble_sort(arr: list) -> list:
    """버블 정렬 구현. 시간복잡도: O(n²), 공간복잡도: O(1)"""
    a = arr[:]          # 원본 보호
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # 인접 원소 교환
    return a


# ---------------------------------------------------------------------------
# 방법 2: sorted() 내장 함수 — O(n log n) (Timsort)
# ---------------------------------------------------------------------------
def builtin_sort(arr: list) -> list:
    """파이썬 내장 정렬. 시간복잡도: O(n log n) (Timsort)"""
    return sorted(arr)


def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    nums = list(map(int, data[1:n + 1]))

    # 두 방법으로 정렬 (결과 동일)
    result_bubble = bubble_sort(nums)
    result_builtin = builtin_sort(nums)

    # 결과 검증
    assert result_bubble == result_builtin, "두 정렬 결과가 다릅니다!"

    # 백준 제출용 출력 (sorted() 결과 사용)
    sys.stdout.write('\n'.join(map(str, result_builtin)) + '\n')


if __name__ == "__main__":
    solve()
