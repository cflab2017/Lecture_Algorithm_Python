# 주제: LIS (Longest Increasing Subsequence)
# O(n²) DP  vs  O(n log n) patience sorting (bisect)

from bisect import bisect_left


def lis_dp(arr: list[int]) -> tuple[int, list[int]]:
    """LIS O(n²) DP.

    dp[i] = arr[i]로 끝나는 LIS 길이
    dp[i] = max(dp[j] + 1) for j < i if arr[j] < arr[i]

    Time:  O(n²)
    Space: O(n)

    Returns:
        (길이, 실제 LIS 수열)
    """
    n = len(arr)
    if n == 0:
        return 0, []

    dp = [1] * n
    parent = [-1] * n   # 역추적용

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    max_len = max(dp)
    last_idx = dp.index(max_len)

    # 역추적
    lis: list[int] = []
    idx = last_idx
    while idx != -1:
        lis.append(arr[idx])
        idx = parent[idx]

    return max_len, list(reversed(lis))


def lis_nlogn(arr: list[int]) -> int:
    """LIS O(n log n) — patience sorting + bisect.

    tails[k] = 길이 k+1인 증가 부분 수열의 가장 작은 마지막 원소

    각 원소에 대해:
      - tails에서 arr[i]보다 크거나 같은 첫 위치 찾기 (bisect_left)
      - 그 위치에 arr[i] 배치 (없으면 append → 길이 1 증가)

    Time:  O(n log n)
    Space: O(n)
    """
    tails: list[int] = []

    for x in arr:
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    return len(tails)


def lis_nlogn_reconstruct(arr: list[int]) -> tuple[int, list[int]]:
    """LIS O(n log n) — 실제 수열 복원 포함.

    Time:  O(n log n)
    Space: O(n)
    """
    n = len(arr)
    if n == 0:
        return 0, []

    tails: list[int] = []
    indices: list[int] = []    # tails에 놓인 원소의 원래 인덱스
    predecessor: list[int] = [-1] * n  # 역추적

    for i, x in enumerate(arr):
        pos = bisect_left(tails, x)
        if pos == len(tails):
            tails.append(x)
            indices.append(i)
        else:
            tails[pos] = x
            indices[pos] = i

        if pos > 0:
            predecessor[i] = indices[pos - 1]

    # 역추적
    lis: list[int] = []
    idx = indices[-1]
    while idx != -1:
        lis.append(arr[idx])
        idx = predecessor[idx]

    return len(tails), list(reversed(lis))


def count_lis(arr: list[int]) -> tuple[int, int]:
    """LIS 길이와 LIS의 개수를 동시에 구하기.

    Time:  O(n²)
    Space: O(n)

    Returns:
        (최대 길이, 그 길이의 LIS 개수)
    """
    n = len(arr)
    if n == 0:
        return 0, 0

    dp = [1] * n      # 길이
    cnt = [1] * n     # 개수

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]

    max_len = max(dp)
    total = sum(cnt[i] for i in range(n) if dp[i] == max_len)
    return max_len, total


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]

    print("=== LIS 결과 비교 ===")
    print(f"배열: {arr}")

    length_dp, seq_dp = lis_dp(arr)
    print(f"O(n²)  DP:    길이={length_dp}, 수열={seq_dp}")

    length_nl = lis_nlogn(arr)
    print(f"O(nlogn):     길이={length_nl}")

    length_rec, seq_rec = lis_nlogn_reconstruct(arr)
    print(f"O(nlogn)+복원: 길이={length_rec}, 수열={seq_rec}")

    print("\n=== patience sorting 과정 시각화 ===")
    tails: list[int] = []
    for x in arr:
        pos = bisect_left(tails, x)
        action = "append" if pos == len(tails) else f"replace[{pos}]"
        before = tails[:]
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x
        print(f"  원소 {x:3d}: {before} → {action}({x}) → {tails}")
    print(f"  LIS 길이: {len(tails)}")

    print("\n=== 다양한 배열 테스트 ===")
    test_arrays = [
        [3, 10, 2, 1, 20],
        [3, 2],
        [50, 3, 10, 7, 40, 80],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]
    for a in test_arrays:
        l_dp, s_dp = lis_dp(a)
        l_nl = lis_nlogn(a)
        length, count = count_lis(a)
        print(f"  {a}: 길이={l_dp}, 수열={s_dp}, 개수={count}")
        assert l_dp == l_nl, f"불일치: {l_dp} vs {l_nl}"
    print("  모든 결과 일치 ✓")
