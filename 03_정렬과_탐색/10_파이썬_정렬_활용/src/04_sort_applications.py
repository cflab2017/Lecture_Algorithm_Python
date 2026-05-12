"""
Topic  : 정렬 응용 — 좌표 압축, 중복 제거, Top-K
Time   : O(n log n) 정렬, O(n) 압축/중복 제거
Space  : O(n)
"""


# ── 좌표 압축 ─────────────────────────────────────────────────────────────────

def coordinate_compression(arr: list[int]) -> list[int]:
    """좌표 압축 (Coordinate Compression).

    값의 범위가 매우 클 때 (예: 0~10⁹) 인덱스(0~n-1)로 변환.
    백준 18870 참고.

    Args:
        arr: 압축할 원래 배열
    Returns:
        압축된 0-indexed 배열
    """
    # 중복 제거 후 정렬 → 순위 매핑
    rank = {v: i for i, v in enumerate(sorted(set(arr)))}
    return [rank[v] for v in arr]


def demo_coordinate_compression() -> None:
    """좌표 압축 예시."""
    print("=== 좌표 압축 ===")
    examples = [
        [5, 4, 2, 3, 1],
        [100, 50, 200, 50, 100],
        [1_000_000, 1, 500_000, 1, 1_000_000],
    ]
    for arr in examples:
        compressed = coordinate_compression(arr)
        print(f"원본: {arr}")
        print(f"압축: {compressed}")
        print()


# ── 정렬 기반 중복 제거 ───────────────────────────────────────────────────────

def deduplicate_sorted(arr: list[int]) -> list[int]:
    """정렬 후 인접 비교로 중복 제거 (O(n log n))."""
    if not arr:
        return []
    a = sorted(arr)
    result = [a[0]]
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            result.append(a[i])
    return result


def demo_deduplication() -> None:
    """중복 제거 방법 비교."""
    print("=== 중복 제거 ===")
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    # 방법 1: set (순서 무관)
    by_set = sorted(set(data))

    # 방법 2: 정렬 후 인접 비교 (순서 보존 필요 없을 때)
    by_sort = deduplicate_sorted(data)

    # 방법 3: 순서 보존 중복 제거
    seen: set[int] = set()
    order_preserved = [x for x in data if not (seen.add(x) or x in seen)]  # type: ignore

    print(f"원본       : {data}")
    print(f"set 사용   : {by_set}")
    print(f"정렬 비교  : {by_sort}")
    assert by_set == by_sort


# ── Top-K 원소 ────────────────────────────────────────────────────────────────

def top_k_sort(arr: list[int], k: int) -> list[int]:
    """정렬로 Top-K 추출 O(n log n)."""
    return sorted(arr, reverse=True)[:k]


def top_k_heap(arr: list[int], k: int) -> list[int]:
    """heapq.nlargest 로 Top-K 추출 O(n log k)."""
    import heapq
    return heapq.nlargest(k, arr)


def demo_top_k() -> None:
    """Top-K 추출 비교."""
    print("\n=== Top-K 추출 ===")
    scores = [85, 92, 78, 96, 88, 74, 100, 65, 91, 83]
    k = 3

    by_sort = top_k_sort(scores, k)
    by_heap = top_k_heap(scores, k)

    print(f"점수: {scores}")
    print(f"Top-{k} (정렬): {by_sort}")
    print(f"Top-{k} (힙) : {by_heap}")

    # 상위 K개 인덱스
    indexed = sorted(enumerate(scores), key=lambda x: -x[1])[:k]
    print(f"Top-{k} 인덱스: {[i for i, _ in indexed]}")


# ── 정렬 기반 그리디 알고리즘 ────────────────────────────────────────────────

def interval_scheduling(intervals: list[tuple[int, int]]) -> int:
    """활동 선택 문제 (끝 시간 오름차순 정렬 그리디).

    서로 겹치지 않는 최대 활동 수 반환.
    """
    # 끝 시간 오름차순 정렬
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    count = 0
    last_end = -1
    for start, end in sorted_intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count


def demo_greedy() -> None:
    """정렬 기반 그리디 예시."""
    print("\n=== 정렬 기반 그리디 (활동 선택) ===")
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
                  (5, 9), (6, 10), (8, 11), (8, 12), (2, 14)]
    max_activities = interval_scheduling(activities)
    print(f"활동 목록: {activities}")
    print(f"겹치지 않는 최대 활동 수: {max_activities}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_coordinate_compression()
    demo_deduplication()
    demo_top_k()
    demo_greedy()

    # 정확성 검증
    assert coordinate_compression([5, 4, 2, 3, 1]) == [4, 3, 1, 2, 0]
    assert coordinate_compression([100, 50, 200, 50, 100]) == [1, 0, 2, 0, 1]
    print("\n좌표 압축 정확성 검증: PASS")
