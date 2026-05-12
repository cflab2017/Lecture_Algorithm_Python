"""
단원 27 — 실전 패턴: 투 포인터 (Two Pointer)
Topic : Two Pointer Patterns
Time  : O(n) per pattern
Space : O(1) ~ O(n)

설명:
    1. 반대 방향 투 포인터: 정렬 배열에서 두 수의 합
    2. 같은 방향 투 포인터: 부분 합이 target 이상인 최소 구간
    3. 중복 제거: 정렬 배열에서 고유한 원소만 유지
"""


# ──────────────────────────────────────────────
# 1. 반대 방향 투 포인터 — 두 수의 합
# ──────────────────────────────────────────────

def two_sum_sorted(arr: list[int], target: int) -> list[tuple[int, int]]:
    """
    정렬된 배열에서 합이 target인 모든 (i, j) 쌍을 반환 (i < j).

    Time : O(n)
    Space: O(결과 크기)
    """
    result: list[tuple[int, int]] = []
    lo, hi = 0, len(arr) - 1

    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            result.append((arr[lo], arr[hi]))
            lo += 1
            hi -= 1
            # 중복 건너뜀
            while lo < hi and arr[lo] == arr[lo - 1]:
                lo += 1
            while lo < hi and arr[hi] == arr[hi + 1]:
                hi -= 1
        elif s < target:
            lo += 1
        else:
            hi -= 1

    return result


# ──────────────────────────────────────────────
# 2. 같은 방향 투 포인터 — 부분 합 최소 구간
# ──────────────────────────────────────────────

def min_subarray_len(arr: list[int], target: int) -> int:
    """
    합이 target 이상인 가장 짧은 연속 부분 배열의 길이 반환.
    없으면 0 반환.

    Time : O(n)  — lo, hi 각각 최대 n번 이동
    Space: O(1)
    """
    n = len(arr)
    lo = 0
    total = 0
    min_len = n + 1

    for hi in range(n):
        total += arr[hi]

        # 조건 만족 → lo를 최대한 오른쪽으로
        while total >= target:
            min_len = min(min_len, hi - lo + 1)
            total -= arr[lo]
            lo += 1

    return min_len if min_len <= n else 0


# ──────────────────────────────────────────────
# 3. 투 포인터 — 정렬 배열 중복 제거 (in-place)
# ──────────────────────────────────────────────

def remove_duplicates(arr: list[int]) -> int:
    """
    정렬된 배열에서 중복을 제거하고 고유 원소 수를 반환.
    결과는 arr[:result_len] 에 저장됨.

    Time : O(n)
    Space: O(1)
    """
    if not arr:
        return 0

    write = 1   # 다음 쓸 위치

    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1

    return write


# ──────────────────────────────────────────────
# 4. 투 포인터 — 구간 내 부분합 == target 개수
# ──────────────────────────────────────────────

def count_subarray_sum(arr: list[int], target: int) -> int:
    """
    연속 부분 배열 합이 정확히 target인 개수 반환 (양수 배열).

    Time : O(n)
    Space: O(1)

    주의: 음수가 없는 배열에서만 성립.
          음수 있으면 해시맵(누적 합) 사용.
    """
    lo = total = count = 0
    for hi in range(len(arr)):
        total += arr[hi]
        while total > target and lo <= hi:
            total -= arr[lo]
            lo += 1
        if total == target:
            count += 1
    return count


def main() -> None:
    # ── 1. 두 수의 합 ──
    print("=" * 55)
    print("1. 두 수의 합 (정렬 배열, 반대 방향 투 포인터)")
    print("=" * 55)
    arr1 = [-2, -1, 0, 1, 2, 3, 4, 5]
    target1 = 4
    pairs = two_sum_sorted(arr1, target1)
    print(f"  배열: {arr1}")
    print(f"  target: {target1}")
    print(f"  결과: {pairs}")

    # ── 2. 최소 부분 배열 ──
    print()
    print("=" * 55)
    print("2. 합 ≥ target 최소 구간 (같은 방향 투 포인터)")
    print("=" * 55)
    cases = [
        ([2, 3, 1, 2, 4, 3], 7),
        ([1, 4, 4], 4),
        ([1, 1, 1, 1], 10),
    ]
    for arr2, tgt in cases:
        result = min_subarray_len(arr2, tgt)
        print(f"  arr={arr2}, target={tgt} → 최소 길이: {result}")

    # ── 3. 중복 제거 ──
    print()
    print("=" * 55)
    print("3. 정렬 배열 중복 제거 (in-place)")
    print("=" * 55)
    arr3 = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"  원본: {arr3}")
    k = remove_duplicates(arr3)
    print(f"  제거 후 ({k}개): {arr3[:k]}")

    # ── 4. 부분합 == target 개수 ──
    print()
    print("=" * 55)
    print("4. 부분합 == target 개수 (양수 배열)")
    print("=" * 55)
    arr4 = [1, 2, 3, 2, 1, 4]
    target4 = 6
    cnt = count_subarray_sum(arr4, target4)
    print(f"  배열: {arr4}, target: {target4}")
    print(f"  합이 {target4}인 부분 배열 수: {cnt}")

    # ── 복잡도 요약 ──
    print()
    print("=" * 55)
    print("투 포인터 복잡도 요약")
    print("=" * 55)
    print("  반대 방향: O(n), 정렬 배열 필요")
    print("  같은 방향: O(n), 양수 값 배열 필요")
    print("  중복 제거: O(n), in-place O(1) 공간")


if __name__ == "__main__":
    main()
