# 주제: 최소 회의실 수 (Minimum Meeting Rooms)
# Time: O(n log n)   Space: O(n)

import heapq


def min_meeting_rooms(intervals: list[tuple[int, int]]) -> int:
    """최소 회의실 수 — 최소 힙 사용.

    아이디어:
      - 시작 시간 정렬
      - 최소 힙에 각 회의의 종료 시간 저장
      - 새 회의가 가장 일찍 끝나는 회의와 겹치지 않으면 재사용

    Time:  O(n log n)
    Space: O(n)
    """
    if not intervals:
        return 0

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    heap: list[int] = []   # 각 회의실의 종료 시간

    for start, end in sorted_intervals:
        if heap and heap[0] <= start:
            # 가장 일찍 끝나는 회의실 재사용
            heapq.heapreplace(heap, end)
        else:
            # 새 회의실 필요
            heapq.heappush(heap, end)

    return len(heap)


def min_meeting_rooms_two_pointer(
    intervals: list[tuple[int, int]]
) -> int:
    """최소 회의실 수 — 두 포인터 방식.

    시작 시간과 종료 시간을 각각 정렬
    → 어느 순간 동시에 진행 중인 회의 수의 최댓값

    Time:  O(n log n)
    Space: O(n)
    """
    if not intervals:
        return 0

    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)

    rooms = 0
    max_rooms = 0
    j = 0   # ends 포인터

    for i in range(len(starts)):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1   # 하나 끝남
            j += 1

    return max_rooms


def meeting_rooms_schedule(
    intervals: list[tuple[int, int]]
) -> list[list[tuple[int, int]]]:
    """각 회의실에 배정된 회의 목록 반환.

    Time:  O(n log n)
    Space: O(n)
    """
    if not intervals:
        return []

    indexed = sorted(enumerate(intervals), key=lambda x: x[1][0])
    # (종료시간, 회의실번호)
    heap: list[tuple[int, int]] = []
    rooms: list[list[tuple[int, int]]] = []

    for orig_idx, (start, end) in indexed:
        if heap and heap[0][0] <= start:
            end_time, room_idx = heapq.heappop(heap)
            rooms[room_idx].append((start, end))
            heapq.heappush(heap, (end, room_idx))
        else:
            room_idx = len(rooms)
            rooms.append([(start, end)])
            heapq.heappush(heap, (end, room_idx))

    return rooms


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    meetings = [
        (0, 30), (5, 10), (15, 20), (2, 12), (11, 25),
    ]

    print("=== 회의 목록 ===")
    print(f"{'회의':>5} | {'시작':>4} | {'종료':>4}")
    print("-" * 18)
    for i, (s, e) in enumerate(meetings):
        print(f"{i:>5} | {s:>4} | {e:>4}")

    min_rooms = min_meeting_rooms(meetings)
    min_rooms_tp = min_meeting_rooms_two_pointer(meetings)
    print(f"\n최소 회의실 수 (힙):       {min_rooms}")
    print(f"최소 회의실 수 (두포인터): {min_rooms_tp}")
    assert min_rooms == min_rooms_tp

    print("\n=== 회의실 배정 ===")
    schedule = meeting_rooms_schedule(meetings)
    for room_idx, room_meetings in enumerate(schedule):
        print(f"  회의실 {room_idx + 1}: {room_meetings}")

    print("\n=== 타임라인 시각화 ===")
    max_time = max(e for _, e in meetings)
    time_header = "시간: " + "".join(f"{t:3d}" for t in range(0, max_time + 1, 3))
    print(f"  {time_header}")
    for i, (s, e) in enumerate(sorted(meetings)):
        bar = "   " * (s // 3) + "━━━" * ((e - s) // 3 + 1)
        print(f"  회의 [{s},{e}]: {bar}")

    print("\n=== 추가 테스트 ===")
    test_cases = [
        [(7, 10), (2, 4)],
        [(0, 30), (5, 10), (15, 20)],
        [(1, 5), (2, 6), (3, 7)],
    ]
    for tc in test_cases:
        r = min_meeting_rooms(tc)
        print(f"  {tc} → {r}개 회의실")
