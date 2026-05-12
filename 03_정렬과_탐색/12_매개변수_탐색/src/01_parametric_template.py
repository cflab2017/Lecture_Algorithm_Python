"""
Topic  : 매개변수 탐색 범용 템플릿
Time   : O(n log(범위))
Space  : O(1) (결정 함수 제외)
"""

from collections.abc import Callable


# ── 범용 템플릿: 최대화 ───────────────────────────────────────────────────────

def parametric_max(
    lo: int,
    hi: int,
    feasible: Callable[[int], bool],
) -> int:
    """가능한 최댓값 탐색.

    feasible(mid) = True 이면 mid 이하의 모든 값도 가능하다고 가정.
    (단조 감소: ✅✅✅❌❌ 패턴)

    Returns:
        조건을 만족하는 최댓값
    """
    answer = lo - 1     # 아무것도 가능하지 않을 때 기본값
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            answer = mid
            lo = mid + 1    # 더 큰 값 시도
        else:
            hi = mid - 1    # 줄여야 함
    return answer


def parametric_min(
    lo: int,
    hi: int,
    feasible: Callable[[int], bool],
) -> int:
    """가능한 최솟값 탐색.

    feasible(mid) = True 이면 mid 이상의 모든 값도 가능하다고 가정.
    (단조 증가: ❌❌✅✅✅ 패턴)

    Returns:
        조건을 만족하는 최솟값
    """
    answer = hi + 1     # 아무것도 가능하지 않을 때 기본값
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            answer = mid
            hi = mid - 1    # 더 작은 값 시도
        else:
            lo = mid + 1    # 키워야 함
    return answer


# ── 예시 1: 배열에서 목표 합 이상 가능한 원소 수 최대화 ─────────────────────

def demo_array_sum() -> None:
    """처음 k개의 합이 S 이상이 되는 최소 k 찾기."""
    arr = [1, 3, 2, 4, 2, 5, 1, 3]
    S = 10
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1] + x)

    def feasible_min_k(k: int) -> bool:
        # 처음 k개 합이 S 이상?
        return prefix[k] >= S

    min_k = parametric_min(1, len(arr), feasible_min_k)
    print(f"배열: {arr}, 목표 합: {S}")
    print(f"합이 {S} 이상인 최소 k: {min_k}  (합={prefix[min_k]})")


# ── 예시 2: 단조성 시각화 ────────────────────────────────────────────────────

def visualize_monotone() -> None:
    """결정 함수의 단조성을 시각화."""
    trees = [20, 15, 10, 17]
    need = 7

    def feasible_cut(h: int) -> bool:
        return sum(max(0, t - h) for t in trees) >= need

    print(f"\n=== 단조성 시각화 ===")
    print(f"나무 높이: {trees}, 필요량: {need}")
    print(f"{'H':>4}  {'수집량':>6}  {'가능?':>6}")
    for h in range(0, max(trees) + 1):
        collected = sum(max(0, t - h) for t in trees)
        ok = feasible_cut(h)
        print(f"{h:>4}  {collected:>6}  {'✅' if ok else '❌'}")

    answer = parametric_max(0, max(trees), feasible_cut)
    print(f"\n→ 가능한 최대 H = {answer}")


# ── 예시 3: 실수 매개변수 탐색 ───────────────────────────────────────────────

def parametric_float(
    lo: float,
    hi: float,
    feasible: Callable[[float], bool],
    eps: float = 1e-9,
    max_iter: int = 100,
) -> float:
    """실수 매개변수 탐색.

    반복 횟수 제한(max_iter) 또는 eps 이하 수렴 시 종료.
    """
    for _ in range(max_iter):
        if hi - lo < eps:
            break
        mid = (lo + hi) / 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def demo_float_search() -> None:
    """실수 매개변수 탐색: sqrt(2) 찾기."""
    target = 2.0

    def feasible_sqrt(x: float) -> bool:
        return x * x <= target

    result = parametric_float(0.0, 2.0, feasible_sqrt)
    import math
    print(f"\n=== 실수 매개변수 탐색 ===")
    print(f"sqrt(2) 탐색 결과: {result:.10f}")
    print(f"math.sqrt(2)     : {math.sqrt(2):.10f}")
    print(f"오차              : {abs(result - math.sqrt(2)):.2e}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_array_sum()
    visualize_monotone()
    demo_float_search()

    # 간단한 검증: 0~100 범위에서 x*x >= 64 인 최솟값
    result = parametric_min(0, 100, lambda x: x * x >= 64)
    assert result == 8, f"Expected 8, got {result}"
    print(f"\n검증: x² ≥ 64 인 최솟값 = {result}  PASS")
