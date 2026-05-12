"""
Topic  : 책 페이지 분배 — 최댓값의 최솟값 (Minimize Maximum)
Time   : O(N log(sum))
Space  : O(N)

문제: N개 챕터를 K명의 독자에게 나눌 때,
     한 명이 읽어야 하는 최대 페이지 수를 최소화.
     (챕터 순서 유지, 연속된 구간만 가능)
"""


# ── 결정 함수 ─────────────────────────────────────────────────────────────────

def can_distribute(chapters: list[int], k: int, max_pages: int) -> bool:
    """max_pages 제한으로 K명 이하에게 나눌 수 있는가?

    각 독자는 연속된 챕터를 읽어야 함.
    """
    readers = 1
    current = 0
    for pages in chapters:
        if pages > max_pages:
            return False           # 단일 챕터가 제한 초과
        if current + pages > max_pages:
            readers += 1
            current = pages
            if readers > k:
                return False
        else:
            current += pages
    return True


# ── 매개변수 탐색 ─────────────────────────────────────────────────────────────

def min_max_pages(chapters: list[int], k: int) -> int:
    """K명에게 나눌 때 최대 페이지 수의 최솟값.

    탐색 범위:
      lo = max(chapters)  : K=N일 때 한 챕터씩 담당
      hi = sum(chapters)  : K=1일 때 전부 담당
    """
    lo = max(chapters)
    hi = sum(chapters)
    answer = hi

    while lo <= hi:
        mid = (lo + hi) // 2
        if can_distribute(chapters, k, mid):
            answer = mid
            hi = mid - 1    # 더 작은 값 시도
        else:
            lo = mid + 1    # 늘려야 함

    return answer


# ── 시각화 ───────────────────────────────────────────────────────────────────

def visualize_distribution(
    chapters: list[int], k: int, max_pages: int
) -> None:
    """max_pages 제한으로 K명에게 나누는 방법 출력."""
    readers: list[list[int]] = [[]]
    current = 0
    for ch in chapters:
        if current + ch > max_pages:
            readers.append([])
            current = 0
        readers[-1].append(ch)
        current += ch

    print(f"\n  max_pages={max_pages} 로 {len(readers)}명에게 배분:")
    for i, r in enumerate(readers):
        print(f"    독자{i+1}: {r}  (합={sum(r)})")
    print(f"  → {'가능 ✅' if len(readers) <= k else '불가 ❌'}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    chapters = [100, 200, 300, 400, 500, 600, 700]
    k = 3

    print("=" * 55)
    print("책 페이지 분배 — K명 최대 페이지 최소화")
    print("=" * 55)
    print(f"챕터 페이지: {chapters}")
    print(f"독자 수 K  : {k}")
    print(f"lo         : {max(chapters)} (한 챕터씩 담당 시 최소)")
    print(f"hi         : {sum(chapters)} (혼자 전부 읽을 때 최대)")

    # 단조성 확인
    lo, hi = max(chapters), sum(chapters)
    sample_points = range(lo, hi + 1, (hi - lo) // 20 or 1)
    print(f"\n{'max_pages':>10}  {'readers':>8}  {'가능?':>6}")
    for mp in sample_points:
        readers_needed = 1
        cur = 0
        for ch in chapters:
            if cur + ch > mp:
                readers_needed += 1
                cur = ch
            else:
                cur += ch
        ok = readers_needed <= k
        print(f"{mp:>10}  {readers_needed:>8}  {'✅' if ok else '❌'}")

    answer = min_max_pages(chapters, k)
    print(f"\n→ 최솟값 = {answer}페이지")
    visualize_distribution(chapters, k, answer)

    # 다양한 k 값 테스트
    print("\n=== K별 최대 페이지 최솟값 ===")
    for ki in range(1, len(chapters) + 1):
        result = min_max_pages(chapters, ki)
        print(f"  K={ki}: {result}")

    # 정확성 검증
    assert min_max_pages([1, 2, 3, 4, 5], 2) == 9   # [1,2,3] [4,5]
    assert min_max_pages([1, 2, 3, 4, 5], 5) == 5   # 각자 하나
    assert min_max_pages([1, 2, 3, 4, 5], 1) == 15  # 한 명이 전부
    print("\n정확성 검증: PASS")
