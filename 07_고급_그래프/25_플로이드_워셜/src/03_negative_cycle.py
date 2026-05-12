"""
단원 25 — 플로이드-워셜: 음수 사이클 탐지
Topic : Negative Cycle Detection via Floyd-Warshall
Time  : O(V³)
Space : O(V²)

설명:
    플로이드-워셜 실행 후 dist[i][i] < 0 인 노드가 존재하면
    해당 노드는 음수 사이클 위에 있다.

    추가로: dist[i][j] = INF 가 아닌데 dist[i][i] < 0 또는
    dist[j][j] < 0 이면 i→j 최단 거리는 -∞ (정의 불가).
"""

INF = float("inf")


def floyd_warshall(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[list[float]]:
    """기본 플로이드-워셜 (방향 그래프). Time O(V³), Space O(V²)."""
    dist: list[list[float]] = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], float(w))

    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                via_k = dist[i][k] + dist[k][j]
                if via_k < dist[i][j]:
                    dist[i][j] = via_k

    return dist


def detect_negative_cycles(dist: list[list[float]]) -> list[int]:
    """
    음수 사이클에 속한 노드 목록을 반환한다.

    원리: 음수 사이클이 있으면 해당 노드 i 에서 dist[i][i] < 0.

    Time : O(V)
    Space: O(V)
    """
    return [i for i in range(len(dist)) if dist[i][i] < 0]


def is_reachable_through_neg_cycle(
    dist: list[list[float]],
    neg_nodes: list[int],
    src: int,
    dst: int,
) -> bool:
    """
    src → dst 경로가 음수 사이클을 통과하는지 확인한다.
    통과하면 최단 거리는 -∞.

    Time : O(V)
    """
    for k in neg_nodes:
        if dist[src][k] < INF and dist[k][dst] < INF:
            return True
    return False


def main() -> None:
    # ── 케이스 1: 음수 사이클 없음 ──
    print("=" * 60)
    print("케이스 1: 음수 간선 있으나 사이클 없음")
    print("  0→1: 2,  1→2: -1,  0→2: 4")
    print("=" * 60)
    edges1 = [(0, 1, 2), (1, 2, -1), (0, 2, 4)]
    dist1 = floyd_warshall(3, edges1)
    neg1 = detect_negative_cycles(dist1)

    for i in range(3):
        print(f"  dist[{i}][{i}] = {dist1[i][i]}")
    print(f"  음수 사이클 노드: {neg1 if neg1 else '없음'}")
    print(f"  0→2 최단: {int(dist1[0][2])} (0→1→2 = 2-1 = 1 < 4)")

    # ── 케이스 2: 음수 사이클 존재 ──
    print()
    print("=" * 60)
    print("케이스 2: 음수 사이클 존재")
    print("  0→1: 1,  1→2: -3,  2→1: 1  (사이클 1→2→1 = -3+1 = -2)")
    print("=" * 60)
    edges2 = [(0, 1, 1), (1, 2, -3), (2, 1, 1), (2, 3, 1)]
    dist2 = floyd_warshall(4, edges2)
    neg2 = detect_negative_cycles(dist2)

    for i in range(4):
        d = dist2[i][i]
        print(f"  dist[{i}][{i}] = {d:.1f}  {'← 음수 사이클!' if d < 0 else ''}")

    print(f"\n  음수 사이클 노드: {neg2}")
    print(f"  0→3 경로가 음수 사이클 통과?: "
          f"{is_reachable_through_neg_cycle(dist2, neg2, 0, 3)}")
    print("  → 0→3 최단 거리는 -∞ (수렴하지 않음)")

    # ── 케이스 3: 실전 활용 — 음수 사이클 유무에 따른 분기 ──
    print()
    print("=" * 60)
    print("케이스 3: 실전 코드 패턴")
    print("=" * 60)
    edges3 = [(0, 1, 3), (1, 2, 2), (2, 0, -4)]  # 0→1→2→0 = 1 (음수 사이클)
    dist3 = floyd_warshall(3, edges3)
    neg3 = detect_negative_cycles(dist3)

    if neg3:
        print(f"  경고: 음수 사이클 탐지 (노드 {neg3})")
        print("  최단 경로 정의 불가 — 벨만-포드 등으로 사이클 처리 필요")
    else:
        print("  음수 사이클 없음 — 플로이드-워셜 결과 신뢰 가능")

    # ── 정리 ──
    print()
    print("=" * 60)
    print("음수 사이클 탐지 규칙 요약")
    print("=" * 60)
    print("  플로이드-워셜 실행 후:")
    print("  dist[i][i] < 0  →  노드 i는 음수 사이클 위")
    print("  i→k와 k→j 경로 모두 존재하고 k가 음수 사이클")
    print("    → i→j 최단 = -∞")


if __name__ == "__main__":
    main()
