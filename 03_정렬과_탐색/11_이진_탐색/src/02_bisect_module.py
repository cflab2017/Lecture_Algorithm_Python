"""
Topic  : bisect 모듈 — bisect_left, bisect_right, insort
Time   : O(log n) 탐색, O(n) 삽입 (insort)
Space  : O(1)
"""

from bisect import bisect_left, bisect_right, insort_left, insort_right


# ── bisect_left vs bisect_right ───────────────────────────────────────────────

def demo_bisect_basics() -> None:
    """bisect_left와 bisect_right의 차이."""
    arr = [1, 3, 3, 3, 5, 7]
    print("=== bisect 기초 ===")
    print(f"배열: {arr}")
    print(f"인덱스: {list(range(len(arr)))}")
    print()

    for target in [0, 1, 2, 3, 4, 5, 7, 8]:
        bl = bisect_left(arr, target)
        br = bisect_right(arr, target)
        print(f"  target={target}: bisect_left={bl}, bisect_right={br}")

    print()
    print("bisect_left(arr, x)  = x 이상인 첫 번째 위치 (lower bound)")
    print("bisect_right(arr, x) = x 초과하는 첫 번째 위치 (upper bound)")


# ── 값 존재 여부 확인 ─────────────────────────────────────────────────────────

def contains(arr: list[int], target: int) -> bool:
    """bisect_left로 값 존재 여부 O(log n) 확인."""
    idx = bisect_left(arr, target)
    return idx < len(arr) and arr[idx] == target


def demo_contains() -> None:
    """값 존재 여부 확인."""
    arr = sorted([5, 2, 8, 1, 9, 3, 7])
    print(f"\n=== 값 존재 여부 ===")
    print(f"배열: {arr}")
    for target in [1, 4, 7, 10]:
        print(f"  {target} 존재? {contains(arr, target)}")


# ── 원소 개수 세기 ────────────────────────────────────────────────────────────

def count_occurrences(arr: list[int], target: int) -> int:
    """정렬된 배열에서 target 개수를 O(log n)에 반환."""
    return bisect_right(arr, target) - bisect_left(arr, target)


def count_in_range(arr: list[int], lo: int, hi: int) -> int:
    """정렬된 배열에서 lo ≤ x ≤ hi 인 원소 수를 O(log n)에 반환."""
    return bisect_right(arr, hi) - bisect_left(arr, lo)


def demo_count() -> None:
    """원소 개수 세기."""
    arr = [1, 2, 3, 3, 3, 4, 5, 5, 6]
    print(f"\n=== 원소 개수 세기 ===")
    print(f"배열: {arr}")
    for t in [1, 3, 5, 7]:
        cnt = count_occurrences(arr, t)
        print(f"  {t}의 개수: {cnt}")
    print(f"[2,5] 범위 내 개수: {count_in_range(arr, 2, 5)}")
    print(f"[3,3] 범위 내 개수: {count_in_range(arr, 3, 3)}")


# ── insort: 정렬 유지 삽입 ────────────────────────────────────────────────────

def demo_insort() -> None:
    """insort_left / insort_right 사용."""
    print(f"\n=== insort 정렬 유지 삽입 ===")
    arr: list[int] = []
    values = [5, 3, 8, 1, 3, 7]
    for v in values:
        insort_left(arr, v)
        print(f"  insort({v:2d}) → {arr}")

    print()
    arr2: list[int] = []
    for v in values:
        insort_right(arr2, v)
        print(f"  insort_right({v:2d}) → {arr2}")


# ── 실전 응용: 성적 구간별 인원 ──────────────────────────────────────────────

def demo_grade_count() -> None:
    """성적 분포 구간별 인원 수 계산."""
    scores = sorted([75, 82, 91, 65, 88, 73, 95, 78, 84, 60,
                     92, 71, 87, 68, 79])
    print(f"\n=== 성적 구간별 인원 ===")
    print(f"성적 배열: {scores}")
    grades = [
        ("A (90~100)", 90, 100),
        ("B (80~89)",  80, 89),
        ("C (70~79)",  70, 79),
        ("D (60~69)",  60, 69),
    ]
    for label, lo, hi in grades:
        cnt = count_in_range(scores, lo, hi)
        print(f"  {label}: {cnt}명")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_bisect_basics()
    demo_contains()
    demo_count()
    demo_insort()
    demo_grade_count()

    # 정확성 검증
    arr = sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    assert count_occurrences(arr, 5) == arr.count(5)
    assert count_occurrences(arr, 1) == arr.count(1)
    assert count_in_range(arr, 3, 6) == sum(1 for x in arr if 3 <= x <= 6)
    print("\n정확성 검증: PASS")
