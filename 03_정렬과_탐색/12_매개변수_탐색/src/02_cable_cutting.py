"""
Topic  : 케이블/나무 자르기 — 매개변수 탐색
Time   : O(N log(max_length))
Space  : O(N)

문제: N개의 케이블에서 길이 L인 조각을 최대 몇 개 만들 수 있나?
     (또는) 최소한 K개 만들려면 L의 최댓값은?
"""


# ── 결정 함수 ─────────────────────────────────────────────────────────────────

def count_pieces(cables: list[int], length: int) -> int:
    """길이 length 로 자를 때 얻는 조각 수."""
    return sum(c // length for c in cables)


def can_make_k(cables: list[int], length: int, k: int) -> bool:
    """길이 length로 K개 이상 만들 수 있는가?"""
    return count_pieces(cables, length) >= k


# ── 매개변수 탐색 ─────────────────────────────────────────────────────────────

def max_length_for_k(cables: list[int], k: int) -> int:
    """K개 이상 만들 수 있는 최대 길이.

    Returns:
        최대 길이 (0이면 불가능)
    """
    if not cables:
        return 0
    left, right = 1, max(cables)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_make_k(cables, mid, k):
            answer = mid
            left = mid + 1     # 더 긴 길이 시도
        else:
            right = mid - 1    # 줄여야 함
    return answer


def min_cables_for_k(cables: list[int], k: int) -> int:
    """정확히 k개를 만들 때 각 조각의 최소 개수의 최댓값.
    (= max_length_for_k와 동일 문제)
    """
    return max_length_for_k(cables, k)


# ── 단계 시각화 ───────────────────────────────────────────────────────────────

def visualize_cutting(cables: list[int], k: int) -> None:
    """탐색 과정 시각화."""
    print(f"케이블 길이: {cables}")
    print(f"목표 개수 K: {k}")
    print(f"{'L':>5}  {'얻는 조각 수':>12}  {'가능?':>6}")
    max_len = max(cables)
    for l in range(1, min(max_len + 1, 30)):   # 30 이하만 출력
        pieces = count_pieces(cables, l)
        ok = pieces >= k
        bar = "█" * min(pieces, 30)
        print(f"{l:>5}  {pieces:>12}  {'✅' if ok else '❌'}  {bar}")
    if max_len >= 30:
        print(f"  ... (최대 {max_len}까지)")


# ── 변형: 최소 랜선 개수 (K개로 나누는 최대 길이) ────────────────────────────

def demo_lanline() -> None:
    """백준 1654 (랜선 자르기) 스타일."""
    cables = [802, 743, 457, 539]
    k = 11

    print("=== 랜선 자르기 (백준 1654 스타일) ===")
    answer = max_length_for_k(cables, k)
    pieces = count_pieces(cables, answer)
    print(f"케이블: {cables}")
    print(f"최소 {k}개를 만드는 최대 길이: {answer}cm")
    print(f"실제 얻는 조각 수: {pieces}개")


# ── 변형: 나무 자르기 ─────────────────────────────────────────────────────────

def demo_tree_cutting() -> None:
    """백준 2805 (나무 자르기) 스타일."""
    trees = [20, 15, 10, 17]
    need = 7

    def tree_feasible(h: int) -> bool:
        return sum(max(0, t - h) for t in trees) >= need

    left, right = 0, max(trees)
    answer = 0
    steps = []
    while left <= right:
        mid = (left + right) // 2
        collected = sum(max(0, t - mid) for t in trees)
        ok = tree_feasible(mid)
        steps.append((left, mid, right, collected, ok))
        if ok:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print("\n=== 나무 자르기 (백준 2805 스타일) ===")
    print(f"나무: {trees}, 필요량: {need}")
    print(f"{'left':>5} {'mid':>5} {'right':>6} {'수집':>6} {'가능?':>6}")
    for l, m, r, c, ok in steps:
        print(f"{l:>5} {m:>5} {r:>6} {c:>6} {'✅' if ok else '❌'}")
    print(f"\n→ 절단 높이 H = {answer}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    cables = [10, 15, 20, 25]
    k = 8

    print("=" * 50)
    print("케이블 자르기 단계 시각화")
    print("=" * 50)
    visualize_cutting(cables, k)
    answer = max_length_for_k(cables, k)
    print(f"\n→ 최대 길이 = {answer}, 조각 수 = {count_pieces(cables, answer)}")

    demo_lanline()
    demo_tree_cutting()

    # 검증
    assert max_length_for_k([802, 743, 457, 539], 11) == 200
    assert max_length_for_k([20, 15, 10, 17], 7) == 15  # 나무 자르기 H=15 → 7
    print("\n정확성 검증: PASS")
