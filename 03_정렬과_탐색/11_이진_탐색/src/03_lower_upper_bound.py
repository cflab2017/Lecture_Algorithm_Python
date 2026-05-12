"""
Topic  : lower bound / upper bound 직접 구현 및 응용
Time   : O(log n)
Space  : O(1)
"""

from bisect import bisect_left, bisect_right


# ── lower bound 직접 구현 ─────────────────────────────────────────────────────

def lower_bound(arr: list[int], target: int) -> int:
    """target 이상인 첫 번째 인덱스 반환 (bisect_left 동일).

    배열이 정렬되어 있어야 함.
    반환값이 len(arr)이면 모든 원소 < target
    """
    left, right = 0, len(arr)
    while left < right:          # 주의: left < right (right = len)
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr: list[int], target: int) -> int:
    """target 초과하는 첫 번째 인덱스 반환 (bisect_right 동일).

    반환값이 len(arr)이면 모든 원소 <= target
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


# ── 검증 ─────────────────────────────────────────────────────────────────────

def verify_bounds() -> None:
    """직접 구현과 bisect 모듈 비교."""
    import random
    test_arrays = [
        [1, 3, 3, 3, 5, 7],
        [1],
        [],
        [1, 1, 1, 1],
        list(range(0, 20, 2)),   # 짝수만
    ]
    print("=== lower/upper bound 검증 ===")
    for arr in test_arrays:
        targets = set(arr) | {0, -1, max(arr, default=0) + 1}
        for t in sorted(targets):
            lb = lower_bound(arr, t)
            ub = upper_bound(arr, t)
            assert lb == bisect_left(arr, t), f"lower_bound 오류: arr={arr}, t={t}"
            assert ub == bisect_right(arr, t), f"upper_bound 오류: arr={arr}, t={t}"
    print("모든 케이스 PASS")


# ── 응용: 원소 개수 ───────────────────────────────────────────────────────────

def count_equal(arr: list[int], target: int) -> int:
    """정렬 배열에서 target과 같은 원소 수."""
    return upper_bound(arr, target) - lower_bound(arr, target)


def count_less_than(arr: list[int], target: int) -> int:
    """target 미만인 원소 수."""
    return lower_bound(arr, target)


def count_greater_than(arr: list[int], target: int) -> int:
    """target 초과인 원소 수."""
    return len(arr) - upper_bound(arr, target)


def count_range(arr: list[int], lo: int, hi: int) -> int:
    """lo ≤ x ≤ hi 범위의 원소 수."""
    return upper_bound(arr, hi) - lower_bound(arr, lo)


# ── 데모 ─────────────────────────────────────────────────────────────────────

def demo_count_operations() -> None:
    """원소 수 연산 데모."""
    arr = [1, 2, 3, 3, 3, 4, 4, 5, 6]
    print(f"\n=== 원소 수 연산 ===")
    print(f"배열: {arr}")
    print(f"3의 개수               : {count_equal(arr, 3)}")
    print(f"3 미만 원소 수          : {count_less_than(arr, 3)}")
    print(f"3 초과 원소 수          : {count_greater_than(arr, 3)}")
    print(f"[2, 4] 범위 원소 수     : {count_range(arr, 2, 4)}")
    print(f"[3, 5] 범위 원소 수     : {count_range(arr, 3, 5)}")


# ── 응용: 숫자 카드 문제 스타일 ───────────────────────────────────────────────

def solve_card_count(cards: list[int], queries: list[int]) -> list[int]:
    """각 쿼리 값이 cards 배열에 몇 번 나타나는지 O(m log n)에 계산.

    백준 10816 스타일
    """
    cards_sorted = sorted(cards)
    return [count_equal(cards_sorted, q) for q in queries]


def demo_card_count() -> None:
    """카드 개수 세기."""
    cards = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
    queries = [10, 9, -10, 3, 100]
    results = solve_card_count(cards, queries)
    print(f"\n=== 숫자 카드 개수 세기 ===")
    print(f"카드: {sorted(cards)}")
    for q, r in zip(queries, results):
        print(f"  {q:>5} → {r}개")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    verify_bounds()
    demo_count_operations()
    demo_card_count()

    # 추가 검증
    arr = [1, 2, 3, 3, 3, 4, 5]
    assert count_equal(arr, 3) == 3
    assert count_less_than(arr, 3) == 2
    assert count_greater_than(arr, 3) == 2
    assert count_range(arr, 2, 4) == 5
    print("\n추가 정확성 검증: PASS")
