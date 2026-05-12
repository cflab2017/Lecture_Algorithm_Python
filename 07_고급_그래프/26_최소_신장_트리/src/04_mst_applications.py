"""
단원 26 — MST: 응용 (MST 가중치, 두 번째 MST, 병목 신장 트리)
Topic : MST Applications — Second MST, Bottleneck Spanning Tree
Time  : MST O(E log E), 두 번째 MST O(E * V)
Space : O(V + E)

설명:
    1. MST 총 가중치 계산 (기본)
    2. 두 번째 최소 신장 트리 (Second Minimum Spanning Tree)
       — MST에서 간선 하나를 제거하고 대체 간선을 추가
    3. 병목 신장 트리 (Bottleneck Spanning Tree)
       — 최대 간선 가중치가 최소인 신장 트리 (MST와 동일)
"""


class UnionFind:
    """경로 압축 + 랭크 합치기. Time O(α(n)), Space O(n)."""

    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


def kruskal(
    n: int,
    edges: list[tuple[int, int, int]],
) -> tuple[int, list[tuple[int, int, int]]]:
    """크루스칼 MST. Time O(E log E), Space O(V+E)."""
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    total = 0
    mst_edges: list[tuple[int, int, int]] = []
    for u, v, w in sorted_edges:
        if uf.union(u, v):
            total += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == n - 1:
                break
    return total, mst_edges


# ──────────────────────────────────────────────
# 두 번째 최소 신장 트리
# ──────────────────────────────────────────────

def second_mst(
    n: int,
    edges: list[tuple[int, int, int]],
) -> int:
    """
    두 번째 최소 신장 트리의 가중치를 반환한다.

    알고리즘:
    1. MST를 구한다.
    2. MST의 각 간선 e를 하나씩 제거한다.
    3. 나머지 간선으로 다시 MST를 구한다. (e를 제외하고 크루스칼)
    4. 유효한 신장 트리 중 최소 가중치를 반환한다.

    Time : O(E * (V + E log E))  MST를 E번 반복
    Space: O(V + E)

    참고: 더 효율적인 O(E log E) 알고리즘도 있으나 구현이 복잡합니다.
    """
    _, mst_edges = kruskal(n, edges)
    mst_set = set(map(id, mst_edges))  # 동일 객체 판별 어려우므로 인덱스 사용

    # 실용적 구현: MST 간선 인덱스 추적
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf_init = UnionFind(n)
    mst_idx: list[int] = []
    for idx, (u, v, w) in enumerate(sorted_edges):
        if uf_init.union(u, v):
            mst_idx.append(idx)
            if len(mst_idx) == n - 1:
                break

    best = float("inf")
    # MST 간선 하나씩 제외하고 새 MST 계산
    for skip in mst_idx:
        uf2 = UnionFind(n)
        total2 = 0
        count2 = 0
        for idx, (u, v, w) in enumerate(sorted_edges):
            if idx == skip:
                continue
            if uf2.union(u, v):
                total2 += w
                count2 += 1
                if count2 == n - 1:
                    break
        if count2 == n - 1:
            best = min(best, total2)

    return int(best) if best != float("inf") else -1


# ──────────────────────────────────────────────
# 병목 신장 트리
# ──────────────────────────────────────────────

def bottleneck_mst(
    n: int,
    edges: list[tuple[int, int, int]],
) -> int:
    """
    병목 신장 트리(Bottleneck Spanning Tree)의 최대 간선 가중치를 반환.

    정리: MST는 병목 신장 트리이기도 하다.
    (모든 신장 트리 중 최대 간선이 최소인 것 = MST)

    Time : O(E log E)
    Space: O(V + E)
    """
    _, mst_edges = kruskal(n, edges)
    if len(mst_edges) < n - 1:
        return -1  # 연결 불가
    return max(w for _, _, w in mst_edges)


def main() -> None:
    # ── 공통 예제 그래프 ──
    n = 5
    edges = [
        (0, 1, 1), (0, 2, 3),
        (1, 2, 1), (1, 3, 4), (1, 4, 2),
        (2, 3, 5),
        (3, 4, 7),
    ]

    # 1. MST 가중치
    print("=" * 55)
    print("1. MST 가중치")
    print("=" * 55)
    total, mst = kruskal(n, edges)
    print(f"MST 가중치: {total}")
    print("MST 간선:")
    for u, v, w in mst:
        print(f"  {u}--{v}: {w}")

    # 2. 두 번째 MST
    print()
    print("=" * 55)
    print("2. 두 번째 최소 신장 트리")
    print("=" * 55)
    second = second_mst(n, edges)
    print(f"두 번째 MST 가중치: {second}")
    print(f"(첫 번째 MST와의 차이: {second - total})")

    # 3. 병목 신장 트리
    print()
    print("=" * 55)
    print("3. 병목 신장 트리 최대 간선")
    print("=" * 55)
    bottleneck = bottleneck_mst(n, edges)
    print(f"MST의 최대 간선 가중치 (병목): {bottleneck}")

    # 다른 신장 트리와 비교
    # 비교용: 임의로 모든 간선 포함 신장 트리 중 하나
    other_st = [(0, 1, 1), (1, 2, 1), (1, 4, 2), (1, 3, 4)]
    other_max = max(w for _, _, w in other_st)
    print(f"다른 신장 트리 최대 간선: {other_max}")
    print(f"MST가 병목 최적: {bottleneck <= other_max}")

    # ── 응용 요약 ──
    print()
    print("=" * 55)
    print("MST 응용 패턴 요약")
    print("=" * 55)
    print("  MST 가중치    : kruskal/prim 기본")
    print("  두 번째 MST   : MST 간선 제거 후 재계산")
    print("  병목 신장 트리 : MST = 병목 최소화 트리")
    print("  클러스터링    : k-1개 최대 간선 제거 → k개 클러스터")
    print("  네트워크 비용 : MST = 최소 연결 비용")


if __name__ == "__main__":
    main()
