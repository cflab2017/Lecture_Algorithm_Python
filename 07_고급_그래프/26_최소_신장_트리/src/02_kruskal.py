"""
단원 26 — MST: 크루스칼 알고리즘 (Kruskal)
Topic : Kruskal's MST Algorithm
Time  : O(E log E)
Space : O(V + E)

설명:
    간선을 가중치 오름차순으로 정렬 후,
    사이클을 형성하지 않는 간선을 선택하여 MST를 구성.
    Union-Find로 사이클 여부를 O(α(V)) 에 판단.
"""


class UnionFind:
    """경로 압축 + 랭크 합치기 유니온-파인드. Time O(α(n)) per op."""

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
    """
    크루스칼 알고리즘으로 MST를 계산한다.

    Args:
        n    : 정점 수 (0-indexed: 0 ~ n-1)
        edges: (u, v, weight) 무방향 간선 목록

    Returns:
        (total_weight, mst_edges)
        total_weight : MST 총 가중치
        mst_edges    : MST에 포함된 간선 목록

    Time : O(E log E)
    Space: O(V + E)
    """
    # 1. 간선 가중치 오름차순 정렬
    sorted_edges = sorted(edges, key=lambda e: e[2])

    uf = UnionFind(n)
    total = 0
    mst_edges: list[tuple[int, int, int]] = []

    # 2. 각 간선 검사
    for u, v, w in sorted_edges:
        if uf.union(u, v):          # 사이클 없음 → MST에 추가
            total += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == n - 1:  # V-1 개 선택 완료
                break

    return total, mst_edges


def main() -> None:
    # ── 예제 1: 강의 본문 그래프 ──
    print("=" * 55)
    print("예제 1: 6개 정점 무방향 그래프")
    print("=" * 55)

    edges1 = [
        (0, 1, 4),   # 1-2
        (0, 2, 3),   # 1-3
        (1, 2, 1),   # 2-3
        (1, 3, 2),   # 2-4
        (1, 4, 3),   # 2-5
        (2, 4, 5),   # 3-5
        (3, 4, 6),   # 4-5
        (4, 5, 7),   # 5-6
        (3, 5, 4),   # 4-6
    ]
    total1, mst1 = kruskal(6, edges1)
    print(f"MST 총 가중치: {total1}")
    print("MST 간선:")
    for u, v, w in mst1:
        print(f"  {u+1} -- {v+1}  (가중치 {w})")

    # ── 예제 2: 완전 그래프 (5개 노드) ──
    print()
    print("=" * 55)
    print("예제 2: 완전 그래프 K5")
    print("=" * 55)
    import itertools
    import random
    random.seed(42)
    n2 = 5
    edges2 = []
    for i, j in itertools.combinations(range(n2), 2):
        w = random.randint(1, 20)
        edges2.append((i, j, w))

    print("간선 목록:")
    for u, v, w in edges2:
        print(f"  {u}-{v}: {w}")

    total2, mst2 = kruskal(n2, edges2)
    print(f"\nMST 총 가중치: {total2}")
    print("MST 간선:")
    for u, v, w in mst2:
        print(f"  {u}-{v}: {w}")

    # ── 예제 3: 연결 불가 (비연결 그래프) ──
    print()
    print("=" * 55)
    print("예제 3: 비연결 그래프 — MSF (최소 신장 포레스트)")
    print("=" * 55)
    edges3 = [(0, 1, 5), (1, 2, 3), (3, 4, 2)]  # 0-1-2 와 3-4 는 분리
    total3, mst3 = kruskal(5, edges3)
    print(f"MSF 총 가중치: {total3}")
    print(f"선택된 간선 수: {len(mst3)} (V-1={4} 미만 → 비연결)")
    for u, v, w in mst3:
        print(f"  {u}-{v}: {w}")

    # ── 복잡도 정리 ──
    print()
    print("=" * 55)
    print("크루스칼 복잡도")
    print("=" * 55)
    print("  간선 정렬  : O(E log E)")
    print("  Union-Find: O(E α(V)) ≈ O(E)")
    print("  전체      : O(E log E)")
    print("  공간      : O(V + E)")


if __name__ == "__main__":
    main()
