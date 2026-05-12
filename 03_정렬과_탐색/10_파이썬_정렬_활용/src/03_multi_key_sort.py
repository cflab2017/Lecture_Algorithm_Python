"""
Topic  : 다중 기준 정렬 — 이름→나이, 튜플 비교
Time   : O(n log n)
Space  : O(n)
"""


# ── 다중 기준 정렬 패턴 ───────────────────────────────────────────────────────

def demo_multi_key_patterns() -> None:
    """다중 기준 정렬 실전 패턴."""
    print("=== 다중 기준 정렬 패턴 ===\n")

    employees = [
        ("김철수", "개발팀", 5_000_000),
        ("이영희", "마케팅", 4_500_000),
        ("박민준", "개발팀", 4_500_000),
        ("최지수", "마케팅", 5_000_000),
        ("정다은", "개발팀", 6_000_000),
    ]

    # 팀별, 같은 팀이면 급여 내림차순
    by_dept_salary = sorted(
        employees,
        key=lambda e: (e[1], -e[2])
    )
    print("팀별, 팀 내 급여 내림차순:")
    for emp in by_dept_salary:
        print(f"  {emp[1]:10s} | {emp[0]} | {emp[2]:,}원")

    # 급여 내림차순, 같으면 이름 오름차순
    by_salary_name = sorted(
        employees,
        key=lambda e: (-e[2], e[0])
    )
    print("\n급여 내림차순, 이름 오름차순:")
    for emp in by_salary_name:
        print(f"  {emp[0]} | {emp[2]:,}원")


# ── 튜플 비교 원리 ────────────────────────────────────────────────────────────

def demo_tuple_comparison() -> None:
    """파이썬 튜플 비교가 다중 기준 정렬의 기반."""
    print("\n=== 튜플 비교 원리 ===")

    pairs = [(1, 2), (1, 1), (2, 0), (1, 3)]
    print(f"원본         : {pairs}")
    print(f"정렬 후      : {sorted(pairs)}")
    print("  → (1,1) < (1,2) < (1,3) < (2,0)  첫 원소 같으면 두 번째 비교")

    # 코딩 테스트 실전: 시작점 오름차순, 끝점 내림차순
    intervals = [(1, 5), (1, 3), (2, 4), (1, 7)]
    sorted_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
    print(f"\n구간 정렬   : {intervals}")
    print(f"시작↑ 끝↓   : {sorted_intervals}")


# ── 이름 정렬 (백준 스타일) ───────────────────────────────────────────────────

def demo_name_length_sort() -> None:
    """백준 1181 스타일: 길이 오름차순, 같으면 사전순."""
    words = ["zoo", "a", "bc", "ab", "b", "aaa", "z"]
    result = sorted(set(words), key=lambda w: (len(w), w))
    print(f"\n=== 이름 정렬 (백준 1181 스타일) ===")
    print(f"입력: {words}")
    print(f"중복 제거 + 길이↑ 사전↑: {result}")


# ── 좌표 정렬 (백준 스타일) ───────────────────────────────────────────────────

def demo_coordinate_sort() -> None:
    """백준 11650 스타일: x 오름차순, 같으면 y 오름차순."""
    coords = [(3, 4), (1, 1), (1, -1), (2, 2), (3, 3)]
    result = sorted(coords)          # 튜플 기본 비교로 OK
    print(f"\n=== 좌표 정렬 (백준 11650 스타일) ===")
    print(f"입력  : {coords}")
    print(f"정렬  : {result}")

    # 명시적으로 쓰면
    result2 = sorted(coords, key=lambda p: (p[0], p[1]))
    assert result == result2
    print("  ← x→y 순으로 정렬됨")


# ── 안정 정렬을 활용한 다단계 정렬 ───────────────────────────────────────────

def demo_stable_multi_sort() -> None:
    """안정 정렬을 이용한 우선순위별 순차 정렬 (고전 기법)."""
    print("\n=== 안정 정렬 다단계 정렬 ===")

    data = [
        ("Alice", 85, "B반"),
        ("Bob", 92, "A반"),
        ("Charlie", 85, "A반"),
        ("Dave", 78, "A반"),
    ]

    # 목표: A반 → B반, 같은 반이면 점수 내림차순, 같은 점수면 이름 순
    # 방법 1: 복합 key (권장)
    result1 = sorted(data, key=lambda x: (x[2], -x[1], x[0]))
    print("복합 key 정렬:")
    for r in result1:
        print(f"  {r}")

    # 방법 2: 안정 정렬 연속 적용 (낮은 우선순위 → 높은 우선순위 순)
    step1 = sorted(data, key=lambda x: x[0])           # 이름
    step2 = sorted(step1, key=lambda x: -x[1])          # 점수 내림차순
    step3 = sorted(step2, key=lambda x: x[2])           # 반

    print("\n다단계 안정 정렬:")
    for r in step3:
        print(f"  {r}")

    assert result1 == step3, "두 방법의 결과가 다름!"
    print("\n두 방법 결과 일치: ✓")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_multi_key_patterns()
    demo_tuple_comparison()
    demo_name_length_sort()
    demo_coordinate_sort()
    demo_stable_multi_sort()
