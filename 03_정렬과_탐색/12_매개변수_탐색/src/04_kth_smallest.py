"""
Topic  : 곱셈 테이블에서 k번째 작은 수 (매개변수 탐색)
Time   : O(m log(m*n))   m*n = 테이블 크기
Space  : O(1)

문제: m×n 곱셈 테이블에서 k번째 작은 수는?
곱셈 테이블[i][j] = i*j (1 ≤ i ≤ m, 1 ≤ j ≤ n)

결정 함수: "x 이하인 수가 k개 이상 있는가?"
x 이하인 수의 개수 = sum(min(x//i, n) for i in range(1, m+1))
"""

import math


# ── 결정 함수 ─────────────────────────────────────────────────────────────────

def count_leq(m: int, n: int, x: int) -> int:
    """m×n 곱셈 테이블에서 x 이하인 수의 개수.

    i행에서 i*j ≤ x 를 만족하는 j의 수 = min(x//i, n)
    """
    count = 0
    for i in range(1, m + 1):
        count += min(x // i, n)
    return count


def find_kth_in_multiplication_table(m: int, n: int, k: int) -> int:
    """m×n 곱셈 테이블에서 k번째 작은 수.

    탐색 범위: [1, m*n]
    """
    lo, hi = 1, m * n
    while lo < hi:
        mid = (lo + hi) // 2
        if count_leq(m, n, mid) >= k:
            hi = mid          # mid 이하로 k개가 있으면 hi를 줄임
        else:
            lo = mid + 1
    return lo


# ── 브루트포스 검증 ───────────────────────────────────────────────────────────

def brute_force_kth(m: int, n: int, k: int) -> int:
    """O(mn log mn) 브루트포스 정답 계산."""
    table = sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))
    return table[k - 1]


# ── 시각화 ───────────────────────────────────────────────────────────────────

def print_multiplication_table(m: int, n: int) -> None:
    """곱셈 테이블 출력."""
    print(f"\n  {m}×{n} 곱셈 테이블:")
    header = "   " + "  ".join(f"{j:3d}" for j in range(1, n + 1))
    print(header)
    for i in range(1, m + 1):
        row = f"{i:2d} |" + "  ".join(f"{i*j:3d}" for j in range(1, n + 1))
        print(row)


def visualize_kth_search(m: int, n: int, k: int) -> None:
    """탐색 과정 시각화."""
    lo, hi = 1, m * n
    print(f"\n{'lo':>5} {'mid':>5} {'hi':>5} {'count_leq':>10} {'방향':>6}")
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = count_leq(m, n, mid)
        direction = "hi=mid" if cnt >= k else "lo=mid+1"
        print(f"{lo:>5} {mid:>5} {hi:>5} {cnt:>10} {direction}")
        if cnt >= k:
            hi = mid
        else:
            lo = mid + 1
    print(f"→ k번째 = {lo}")


# ── 공유기 설치 (최솟값의 최댓값) ────────────────────────────────────────────

def max_min_distance(houses: list[int], c: int) -> int:
    """C개 공유기를 설치할 때 인접 공유기 거리의 최솟값 최대화.

    백준 2110 스타일.
    결정 함수: 최소 거리 d 이상 유지하며 C개 설치 가능?
    """
    houses_sorted = sorted(houses)

    def feasible(d: int) -> bool:
        count = 1
        last = houses_sorted[0]
        for h in houses_sorted[1:]:
            if h - last >= d:
                count += 1
                last = h
                if count >= c:
                    return True
        return count >= c

    lo, hi = 1, houses_sorted[-1] - houses_sorted[0]
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer


def demo_router() -> None:
    """공유기 설치 데모."""
    houses = [1, 2, 8, 4, 9]
    c = 3
    result = max_min_distance(houses, c)
    print(f"\n=== 공유기 설치 (백준 2110 스타일) ===")
    print(f"집 위치: {sorted(houses)}")
    print(f"공유기 수 C={c}")
    print(f"최솟값의 최댓값: {result}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    m, n = 3, 3
    print_multiplication_table(m, n)

    print(f"\n=== {m}×{n} 테이블에서 k번째 작은 수 ===")
    for k in range(1, m * n + 1):
        fast = find_kth_in_multiplication_table(m, n, k)
        brute = brute_force_kth(m, n, k)
        status = "✓" if fast == brute else "✗"
        print(f"  k={k:2d}: {fast:>4} {status}")

    print()
    m2, n2 = 5, 5
    print_multiplication_table(m2, n2)
    k2 = 10
    print(f"\n{m2}×{n2} 테이블에서 {k2}번째 작은 수:")
    visualize_kth_search(m2, n2, k2)

    # 대규모 검증
    large_result = find_kth_in_multiplication_table(100, 100, 5000)
    print(f"\n100×100 테이블 5000번째: {large_result}")

    demo_router()

    # 정확성 검증
    assert find_kth_in_multiplication_table(3, 3, 5) == 4
    assert max_min_distance([1, 2, 8, 4, 9], 3) == 3
    print("\n정확성 검증: PASS")
