"""
단원 27 — 실전 패턴: 비트마스킹 (Bitmask)
Topic : Bitmask — Subset Enumeration, Visited State DP, TSP
Time  : 부분집합 열거 O(2ⁿ), TSP O(2ⁿ * n²)
Space : O(2ⁿ * n)

설명:
    1. 비트 연산 기본 (ON/OFF/CHECK/COUNT)
    2. 부분집합 열거 O(2ⁿ)
    3. 방문 상태 DP — 비트마스크로 방문 집합 표현
    4. TSP (외판원 순회) 비트마스크 DP
"""

import sys

INF = sys.maxsize


# ──────────────────────────────────────────────
# 1. 비트 연산 유틸리티
# ──────────────────────────────────────────────

def bit_on(mask: int, i: int) -> int:
    """i번째 비트를 1로 설정. Time O(1)."""
    return mask | (1 << i)


def bit_off(mask: int, i: int) -> int:
    """i번째 비트를 0으로 설정. Time O(1)."""
    return mask & ~(1 << i)


def bit_check(mask: int, i: int) -> bool:
    """i번째 비트가 1인지 확인. Time O(1)."""
    return bool(mask >> i & 1)


def bit_count(mask: int) -> int:
    """비트 1의 개수 (popcount). Time O(1) (내장 bin 사용)."""
    return bin(mask).count("1")


def lowest_bit(mask: int) -> int:
    """가장 낮은 1비트만 남김. Time O(1)."""
    return mask & (-mask)


# ──────────────────────────────────────────────
# 2. 부분집합 열거
# ──────────────────────────────────────────────

def enumerate_subsets(items: list) -> list[list]:
    """
    items의 모든 부분집합을 반환 (공집합 포함).

    Time : O(2ⁿ * n)
    Space: O(2ⁿ * n)
    """
    n = len(items)
    result = []
    for mask in range(1 << n):
        subset = [items[i] for i in range(n) if bit_check(mask, i)]
        result.append(subset)
    return result


def enumerate_subsets_of_mask(mask: int) -> list[int]:
    """
    주어진 mask의 모든 부분 비트마스크를 열거.
    (비어 있는 경우 포함)

    Time : O(2^k)  k = popcount(mask)
    """
    sub = mask
    result = []
    while sub:
        result.append(sub)
        sub = (sub - 1) & mask
    result.append(0)  # 공집합
    return result


# ──────────────────────────────────────────────
# 3. 방문 상태 DP — 비트마스크로 방문 집합 표현
# ──────────────────────────────────────────────

def min_cost_visit_all(
    dist: list[list[int]],
    start: int,
) -> int:
    """
    모든 노드를 정확히 한 번씩 방문하고 start로 돌아오는 최소 비용.
    (소규모 TSP)

    dp[mask][v] = mask 집합을 방문하고 현재 위치가 v일 때 최소 비용.

    Time : O(2ⁿ * n²)
    Space: O(2ⁿ * n)
    """
    n = len(dist)
    full = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1 << start][start] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not bit_check(mask, u):
                continue
            for v in range(n):
                if bit_check(mask, v):
                    continue   # 이미 방문
                if dist[u][v] == INF:
                    continue
                new_mask = bit_on(mask, v)
                cost = dp[mask][u] + dist[u][v]
                if cost < dp[new_mask][v]:
                    dp[new_mask][v] = cost

    # 모든 노드 방문 후 start로 귀환
    best = INF
    for v in range(n):
        if v == start:
            continue
        if dp[full][v] != INF and dist[v][start] != INF:
            best = min(best, dp[full][v] + dist[v][start])

    return best


def main() -> None:
    # ── 1. 비트 연산 기본 ──
    print("=" * 55)
    print("1. 비트 연산 기본")
    print("=" * 55)
    mask = 0b1010   # 1, 3번 비트 ON
    print(f"  초기 mask: {bin(mask)} ({mask})")
    print(f"  0번 비트 ON : {bin(bit_on(mask, 0))}")
    print(f"  1번 비트 OFF: {bin(bit_off(mask, 1))}")
    print(f"  3번 비트 확인: {bit_check(mask, 3)}")
    print(f"  비트 개수   : {bit_count(mask)}")
    print(f"  최하위 비트 : {bin(lowest_bit(mask))}")

    # ── 2. 부분집합 열거 ──
    print()
    print("=" * 55)
    print("2. 부분집합 열거 (n=3)")
    print("=" * 55)
    items = ["A", "B", "C"]
    subsets = enumerate_subsets(items)
    for i, s in enumerate(subsets):
        print(f"  mask={bin(i):>5}: {s if s else '공집합'}")

    print()
    print(f"  총 {len(subsets)}개 (2^{len(items)})")

    # ── 2b. 특정 mask의 부분 마스크 ──
    print()
    print("=" * 55)
    print("2b. mask=0b1011의 부분 마스크 열거")
    print("=" * 55)
    m = 0b1011
    subs = enumerate_subsets_of_mask(m)
    print(f"  mask={bin(m)}: 부분마스크 {len(subs)}개")
    for s in subs:
        print(f"    {bin(s)}")

    # ── 3. TSP (4개 도시) ──
    print()
    print("=" * 55)
    print("3. TSP — 4개 도시 최소 순회 비용 (비트마스크 DP)")
    print("=" * 55)
    dist_matrix = [
        [0,   10,  15,  20],
        [10,  0,   35,  25],
        [15,  35,  0,   30],
        [20,  25,  30,  0 ],
    ]
    print("  거리 행렬:")
    for i, row in enumerate(dist_matrix):
        print(f"    {row}")

    min_cost = min_cost_visit_all(dist_matrix, start=0)
    print(f"\n  최소 순회 비용: {min_cost}")
    print("  (0→1→3→2→0: 10+25+30+15=80)")

    # ── 복잡도 요약 ──
    print()
    print("=" * 55)
    print("비트마스크 복잡도 요약")
    print("=" * 55)
    print("  비트 연산       : O(1)")
    print("  부분집합 열거   : O(2ⁿ * n)")
    print("  부분마스크 열거  : O(2^k), k=popcount")
    print("  TSP DP          : O(2ⁿ * n²)")
    for n_val in [10, 15, 20]:
        ops = (2 ** n_val) * n_val ** 2
        print(f"    n={n_val}: {ops:>12,}  "
              f"{'OK' if ops <= 1e8 else 'TLE 위험'}")


if __name__ == "__main__":
    main()
