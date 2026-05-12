"""
단원 26 — MST: 유니온-파인드 (Union-Find / Disjoint Set Union)
Topic : Union-Find with Path Compression and Union by Rank
Time  : O(α(V)) per operation  ≈ O(1) amortized
Space : O(V)

설명:
    경로 압축(Path Compression): find 시 모든 노드의 부모를 루트로 직접 연결.
    랭크 합치기(Union by Rank): 랭크 낮은 트리를 랭크 높은 트리 아래로 합침.
    두 최적화를 함께 쓰면 상각 복잡도 O(α(V)) ≈ O(1).
"""


class UnionFind:
    """
    경로 압축 + 랭크 합치기 유니온-파인드.

    Time : find/union O(α(n)) amortized
    Space: O(n)
    """

    def __init__(self, n: int) -> None:
        """
        n개 원소 초기화. 각 원소는 자기 자신이 루트.

        Time : O(n)
        Space: O(n)
        """
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n   # 집합 크기 (보너스)
        self.num_components = n

    def find(self, x: int) -> int:
        """
        x가 속한 집합의 루트(대표 원소)를 반환한다.
        경로 압축 적용: 루트를 찾으면서 모든 노드의 부모를 루트로 갱신.

        Time : O(α(n)) amortized
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        x와 y가 속한 집합을 합친다.

        Returns:
            True  이면 두 집합이 합쳐짐 (서로 다른 집합이었음)
            False 이면 이미 같은 집합 (사이클 형성)

        Time : O(α(n)) amortized
        """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False   # 이미 같은 집합

        # 랭크 합치기: 낮은 랭크를 높은 랭크 아래로
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx   # rx가 항상 더 높은 랭크
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        self.num_components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """x와 y가 같은 집합인지 확인. Time O(α(n))."""
        return self.find(x) == self.find(y)

    def component_size(self, x: int) -> int:
        """x가 속한 집합의 크기 반환. Time O(α(n))."""
        return self.size[self.find(x)]


def main() -> None:
    print("=" * 55)
    print("유니온-파인드 기본 연산 테스트")
    print("=" * 55)

    uf = UnionFind(7)   # 노드 0~6
    print(f"초기 집합 수: {uf.num_components}")

    # union 연산
    ops = [(0, 1), (1, 2), (3, 4), (5, 6), (2, 3)]
    for u, v in ops:
        merged = uf.union(u, v)
        print(f"  union({u}, {v}): {'합침' if merged else '이미 같은 집합'}"
              f"  → 집합 수={uf.num_components}")

    print()
    print("연결 여부:")
    pairs = [(0, 4), (0, 5), (5, 6)]
    for u, v in pairs:
        print(f"  connected({u}, {v}): {uf.connected(u, v)}")

    print()
    print("집합 크기:")
    for i in range(7):
        print(f"  node {i}: root={uf.find(i)}, 집합크기={uf.component_size(i)}")

    # ── 경로 압축 시각화 ──
    print()
    print("=" * 55)
    print("경로 압축 예시 (깊은 체인 → 1단계로 압축)")
    print("=" * 55)

    uf2 = UnionFind(6)
    # 0→1→2→3→4→5 체인
    for i in range(5):
        uf2.parent[i + 1] = i  # 일부러 rank 우회하여 체인 생성
    uf2.parent[0] = 0

    print(f"압축 전 parent: {uf2.parent}")
    root = uf2.find(5)   # 경로 압축 발생
    print(f"find(5) = {root}")
    print(f"압축 후 parent: {uf2.parent}")
    print("(모든 노드가 루트를 직접 가리킴)")

    # ── 사이클 탐지 응용 ──
    print()
    print("=" * 55)
    print("사이클 탐지 응용")
    print("=" * 55)

    uf3 = UnionFind(4)
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]  # 마지막 간선이 사이클
    for u, v in edges:
        result = uf3.union(u, v)
        label = "추가" if result else "사이클 탐지!"
        print(f"  간선 ({u}-{v}): {label}")


if __name__ == "__main__":
    main()
