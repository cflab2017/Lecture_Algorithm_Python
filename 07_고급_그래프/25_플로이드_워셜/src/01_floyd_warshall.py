"""
단원 25 — 플로이드-워셜: 기본 구현
Topic : Floyd-Warshall All-Pairs Shortest Path
Time  : O(V³)
Space : O(V²)

설명:
    모든 쌍 최단 경로를 DP로 계산한다.
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    k(경유 노드)가 가장 바깥 루프임에 주의.
"""

import sys

INF = float("inf")


def floyd_warshall(
    n: int,
    edges: list[tuple[int, int, int]],
    directed: bool = True,
) -> list[list[float]]:
    """
    플로이드-워셜로 모든 쌍 최단 거리를 반환한다.

    Args:
        n       : 노드 수 (0-indexed: 0 ~ n-1)
        edges   : (u, v, w) 간선 목록
        directed: True 이면 방향 그래프

    Returns:
        dist[i][j]: i → j 최단 거리 (도달 불가면 float('inf'))

    Time : O(V³)
    Space: O(V²)
    """
    # 초기화: INF, 자기 자신은 0
    dist: list[list[float]] = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0.0

    # 간선 입력
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], float(w))
        if not directed:
            dist[v][u] = min(dist[v][u], float(w))

    # 메인 루프 — k(경유 노드)가 가장 바깥!
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:   # 조기 종료 최적화
                continue
            for j in range(n):
                via_k = dist[i][k] + dist[k][j]
                if via_k < dist[i][j]:
                    dist[i][j] = via_k

    return dist


def print_dist_matrix(dist: list[list[float]], labels: list[str]) -> None:
    """거리 행렬을 보기 좋게 출력한다."""
    n = len(labels)
    header = "     " + "".join(f"{lb:>8}" for lb in labels)
    print(header)
    print("     " + "-" * (8 * n))
    for i, row in enumerate(dist):
        cells = []
        for d in row:
            cells.append("INF" if d == INF else f"{int(d)}")
        print(f"  {labels[i]} |" + "".join(f"{c:>8}" for c in cells))


def main() -> None:
    # ── 예제 1: 강의 본문 그래프 ──
    print("=" * 60)
    print("예제 1: 방향 그래프 (0~3)")
    print("=" * 60)
    edges1 = [
        (0, 1, 3),
        (0, 2, 2),
        (0, 3, 7),
        (1, 2, 1),
        (2, 3, 1),
    ]
    dist1 = floyd_warshall(4, edges1, directed=True)
    print_dist_matrix(dist1, ["0", "1", "2", "3"])

    print()
    print("직접 확인 (0→3 최단):", int(dist1[0][3]))

    # ── 예제 2: 음수 간선 포함 ──
    print()
    print("=" * 60)
    print("예제 2: 음수 간선 포함 (사이클 없음)")
    print("=" * 60)
    edges2 = [
        (0, 1, 5),
        (1, 2, -3),
        (0, 2, 4),
        (2, 3, 2),
    ]
    dist2 = floyd_warshall(4, edges2, directed=True)
    print_dist_matrix(dist2, ["A", "B", "C", "D"])

    print()
    print("A→C 최단:", int(dist2[0][2]), "(5 + (-3) = 2 vs 직행 4 → 2 선택)")

    # ── 예제 3: 무방향 그래프 ──
    print()
    print("=" * 60)
    print("예제 3: 무방향 그래프")
    print("=" * 60)
    edges3 = [
        (0, 1, 1),
        (1, 2, 3),
        (0, 2, 10),
        (2, 3, 2),
    ]
    dist3 = floyd_warshall(4, edges3, directed=False)
    print_dist_matrix(dist3, ["P", "Q", "R", "S"])
    print()
    print("P→S 최단:", int(dist3[0][3]), "(P→Q→R→S = 1+3+2 = 6)")

    # ── 복잡도 정리 ──
    print()
    print("=" * 60)
    print("복잡도 요약")
    print("=" * 60)
    for v in [10, 100, 500, 1000]:
        ops = v ** 3
        print(f"  V={v:>5}: O(V³) = {ops:>12,} 연산"
              f"  {'OK' if ops <= 1e8 else 'TLE 위험'}")


if __name__ == "__main__":
    main()
