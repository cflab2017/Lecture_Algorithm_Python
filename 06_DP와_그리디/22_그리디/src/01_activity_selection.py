# 주제: 활동 선택 문제 (회의실 배정) — 그리디
# Time: O(n log n)   Space: O(n)


def activity_selection(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """최대 활동 수 선택 (겹치지 않도록).

    핵심: 종료 시간 기준 오름차순 정렬
    → 일찍 끝나는 활동을 먼저 선택

    Time:  O(n log n) — 정렬 지배
    Space: O(n)
    """
    # 종료 시간으로 정렬
    sorted_activities = sorted(activities, key=lambda x: (x[1], x[0]))

    selected: list[tuple[int, int]] = []
    last_end = -1   # 마지막으로 선택된 활동의 종료 시간

    for start, end in sorted_activities:
        if start >= last_end:   # 겹치지 않음
            selected.append((start, end))
            last_end = end

    return selected


def activity_selection_with_idx(
    activities: list[tuple[int, int]]
) -> tuple[int, list[int]]:
    """최대 활동 수 + 선택된 인덱스 반환.

    Time:  O(n log n)
    Space: O(n)
    """
    indexed = sorted(enumerate(activities), key=lambda x: x[1][1])
    selected_idx: list[int] = []
    last_end = -1

    for idx, (start, end) in indexed:
        if start >= last_end:
            selected_idx.append(idx)
            last_end = end

    return len(selected_idx), selected_idx


def max_non_overlapping(intervals: list[tuple[int, int]]) -> int:
    """LeetCode 스타일: 최대 비겹치는 구간 수.

    Time:  O(n log n)
    Space: O(1)
    """
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    count = 0
    last_end = float("-inf")

    for start, end in sorted_intervals:
        if start >= last_end:
            count += 1
            last_end = end

    return count


def min_removals_for_non_overlap(intervals: list[tuple[int, int]]) -> int:
    """겹치지 않게 하려면 최소 몇 개를 제거해야 하는가.

    Time:  O(n log n)
    Space: O(1)
    """
    total = len(intervals)
    keep = max_non_overlapping(intervals)
    return total - keep


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 백준 1931 유형 데이터
    activities = [
        (1, 4), (3, 5), (0, 6), (5, 7),
        (3, 9), (5, 9), (6, 10), (8, 11),
        (8, 12), (2, 14), (12, 16),
    ]

    print("=== 활동 선택 ===")
    print(f"전체 활동: {len(activities)}개")
    selected = activity_selection(activities)
    print(f"선택된 활동 ({len(selected)}개):")
    for s, e in selected:
        print(f"  [{s:2d}, {e:2d}]")

    print("\n=== 타임라인 시각화 ===")
    selected_set = set(selected)
    print("  시간:  " + "".join(f"{i:2d}" for i in range(17)))
    for s, e in sorted(activities):
        bar = "  " * s + "━━" * (e - s)
        marker = " ✓" if (s, e) in selected_set else "  "
        print(f"{marker}  [{s},{e}]: {bar}")

    print("\n=== 겹치는 구간 최소 제거 ===")
    intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
    print(f"구간: {intervals}")
    print(f"최대 비겹치는 수: {max_non_overlapping(intervals)}")
    print(f"최소 제거 수:     {min_removals_for_non_overlap(intervals)}")

    print("\n=== 정렬 기준 비교 (시작 시간 vs 종료 시간) ===")
    wrong_case = [(0, 10), (1, 2), (3, 4)]
    by_start = sorted(wrong_case, key=lambda x: x[0])
    by_end = sorted(wrong_case, key=lambda x: x[1])

    print(f"  원본: {wrong_case}")
    print(f"  시작시간 정렬: {by_start}")
    print(f"  종료시간 정렬: {by_end}")

    # 시작 시간 기준 그리디 (틀림)
    wrong_result = []
    last = -1
    for s, e in by_start:
        if s >= last:
            wrong_result.append((s, e))
            last = e
    print(f"  시작시간 그리디 결과: {wrong_result} (틀림!)")

    correct = activity_selection(wrong_case)
    print(f"  종료시간 그리디 결과: {correct} (정답)")
