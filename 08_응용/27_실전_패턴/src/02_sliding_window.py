"""
단원 27 — 실전 패턴: 슬라이딩 윈도우 (Sliding Window)
Topic : Sliding Window — Fixed/Variable + Deque Min/Max
Time  : O(n)
Space : O(k) or O(n)

설명:
    1. 고정 크기 창: 길이 k 구간의 최대 합
    2. 가변 크기 창: 합이 target 이상인 최소 구간 (양수)
    3. deque로 O(n) 창 최솟값: 백준 11003 스타일
    4. 가변 창 최대 고유 문자 수 (문자열)
"""

from collections import deque


# ──────────────────────────────────────────────
# 1. 고정 크기 창 — 최대 합
# ──────────────────────────────────────────────

def max_sum_fixed_window(arr: list[int], k: int) -> int:
    """
    길이 k인 연속 부분 배열 중 최대 합을 반환.

    Time : O(n)
    Space: O(1)
    """
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # 오른쪽 추가, 왼쪽 제거
        max_sum = max(max_sum, window_sum)

    return max_sum


# ──────────────────────────────────────────────
# 2. 가변 크기 창 — 합 ≥ target 최소 구간
# ──────────────────────────────────────────────

def min_window_sum(arr: list[int], target: int) -> int:
    """
    합이 target 이상인 가장 짧은 구간 길이 반환 (양수 배열).

    Time : O(n)
    Space: O(1)
    """
    n = len(arr)
    lo = total = 0
    min_len = n + 1

    for hi in range(n):
        total += arr[hi]
        while total >= target:
            min_len = min(min_len, hi - lo + 1)
            total -= arr[lo]
            lo += 1

    return min_len if min_len <= n else 0


# ──────────────────────────────────────────────
# 3. deque 슬라이딩 윈도우 — 구간 최솟값 O(n)
# ──────────────────────────────────────────────

def sliding_window_minimum(arr: list[int], k: int) -> list[int]:
    """
    크기 k인 슬라이딩 창의 최솟값 목록을 반환.

    원리: 단조 증가 덱 — 덱의 앞은 현재 창의 최솟값 인덱스.
    새 원소보다 큰 인덱스를 덱 뒤에서 제거(필요 없으므로).

    Time : O(n)  — 각 원소는 덱에 1번 들어가고 1번 나옴
    Space: O(k)
    """
    result: list[int] = []
    dq: deque[int] = deque()   # 인덱스 저장

    for i, val in enumerate(arr):
        # 현재 값보다 크거나 같은 덱 뒤 원소 제거 (단조 증가 유지)
        while dq and arr[dq[-1]] >= val:
            dq.pop()
        dq.append(i)

        # 창 밖으로 나간 인덱스 제거
        if dq[0] <= i - k:
            dq.popleft()

        # 창이 완성된 시점부터 결과 저장
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# ──────────────────────────────────────────────
# 4. 가변 창 — 최대 고유 문자 k개 이하 부분 문자열 최대 길이
# ──────────────────────────────────────────────

def max_len_at_most_k_distinct(s: str, k: int) -> int:
    """
    서로 다른 문자가 최대 k개인 가장 긴 부분 문자열 길이 반환.

    Time : O(n)
    Space: O(k)  (문자 종류 최대 k개)
    """
    freq: dict[str, int] = {}
    lo = max_len = 0

    for hi, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1

        while len(freq) > k:
            left_ch = s[lo]
            freq[left_ch] -= 1
            if freq[left_ch] == 0:
                del freq[left_ch]
            lo += 1

        max_len = max(max_len, hi - lo + 1)

    return max_len


def main() -> None:
    # ── 1. 고정 창 최대 합 ──
    print("=" * 55)
    print("1. 고정 크기 창 최대 합")
    print("=" * 55)
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    result1 = max_sum_fixed_window(arr1, k1)
    print(f"  배열: {arr1}, k={k1}")
    print(f"  최대 합: {result1}  (5+1+3=9 또는 2+1+5=8 → {result1})")

    # 모든 창 합 확인
    print("  창별 합:", [sum(arr1[i:i+k1]) for i in range(len(arr1)-k1+1)])

    # ── 2. 가변 창 최소 구간 ──
    print()
    print("=" * 55)
    print("2. 합 ≥ target 최소 구간")
    print("=" * 55)
    cases2 = [
        ([2, 3, 1, 2, 4, 3], 7),
        ([1, 4, 4], 4),
    ]
    for arr2, tgt in cases2:
        r = min_window_sum(arr2, tgt)
        print(f"  arr={arr2}, target={tgt} → {r}")

    # ── 3. 슬라이딩 윈도우 최솟값 (deque) ──
    print()
    print("=" * 55)
    print("3. 슬라이딩 창 최솟값 (deque, O(n))")
    print("=" * 55)
    arr3 = [1, 3, -1, -3, 5, 3, 6, 7]
    k3 = 3
    mins = sliding_window_minimum(arr3, k3)
    print(f"  배열: {arr3}")
    print(f"  k={k3} 창 최솟값: {mins}")
    print(f"  기댓값:          [-1, -3, -3, -3, 3, 3]")

    # ── 4. 고유 문자 k개 이하 최장 부분 문자열 ──
    print()
    print("=" * 55)
    print("4. 서로 다른 문자 ≤ k 최장 부분 문자열")
    print("=" * 55)
    test_cases = [("eceba", 2), ("aa", 1), ("aabacbebebe", 3)]
    for s, k in test_cases:
        r = max_len_at_most_k_distinct(s, k)
        print(f"  s={s!r}, k={k} → {r}")

    # ── 복잡도 요약 ──
    print()
    print("=" * 55)
    print("슬라이딩 윈도우 복잡도 요약")
    print("=" * 55)
    print("  고정 창 합/평균 : O(n),  O(1)")
    print("  가변 창 합     : O(n),  O(1)")
    print("  deque 최솟값   : O(n),  O(k)")
    print("  가변 창 해시맵  : O(n),  O(k)")


if __name__ == "__main__":
    main()
