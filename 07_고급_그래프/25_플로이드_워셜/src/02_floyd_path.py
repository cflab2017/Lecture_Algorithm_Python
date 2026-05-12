"""
단원 25 — 플로이드-워셜: 경로 복원 (next 행렬)
Topic : Floyd-Warshall with Path Reconstruction
Time  : O(V³)  구축 / O(V) 경로 복원
Space : O(V²)

설명:
    next[i][j] = i→j 최단 경로에서 i 다음에 갈 노드.
    초기: 직접 연결된 간선 (u,v) → next[u][v] = v
    갱신: dist[i][j] 가 갱신될 때 next[i][j] = next[i][k]
    복원: i에서 시작하여 next[cur][j] 를 따라가면 경로가 나온다.
"""

INF = float("inf")


def floyd_warshall_with_path(
    n: int,
    edges: list[tuple[int, int, int]],
    directed: bool = True,
) -> tuple[list[list[float]], list[list[int]]]:
    """
    플로이드-워셜 + 경로 복원 행렬 반환.

    Returns:
        (dist, nxt)
        dist[i][j]: i→j 최단 거리
        nxt[i][j] : i→j 최단 경로에서 i 다음 노드 (-1 이면 없음)

    Time : O(V³)
    Space: O(V²)
    """
    dist: list[list[float]] = [[INF] * n for _ in range(n)]
    nxt: list[list[int]] = [[-1] * n for _ in range(n)]

    # 초기화
    for i in range(n):
        dist[i][i] = 0.0

    for u, v, w in edges:
        if float(w) < dist[u][v]:
            dist[u][v] = float(w)
            nxt[u][v] = v
        if not directed and float(w) < dist[v][u]:
            dist[v][u] = float(w)
            nxt[v][u] = u

    # 메인 루프
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                via_k = dist[i][k] + dist[k][j]
                if via_k < dist[i][j]:
                    dist[i][j] = via_k
                    nxt[i][j] = nxt[i][k]   # ← 경로 갱신

    return dist, nxt


def reconstruct_path(
    nxt: list[list[int]],
    src: int,
    dst: int,
) -> list[int]:
    """
    nxt 행렬로 src → dst 최단 경로를 복원한다.

    Returns:
        경로 노드 목록 (도달 불가이면 빈 리스트)

    Time : O(V)
    Space: O(V)
    """
    if nxt[src][dst] == -1:
        return []
    path = [src]
    cur = src
    while cur != dst:
        cur = nxt[cur][dst]
        if cur == -1:
            return []   # 중간에 끊김 (비정상)
        path.append(cur)
    return path


def main() -> None:
    # ── 예제 그래프 ──
    # 노드: 0=서울, 1=대전, 2=대구, 3=부산
    # 간선 (무방향)
    labels = ["서울", "대전", "대구", "부산"]
    edges = [
        (0, 1, 140),   # 서울-대전
        (1, 2, 120),   # 대전-대구
        (2, 3, 80),    # 대구-부산
        (0, 3, 450),   # 서울-부산 (직행)
        (1, 3, 200),   # 대전-부산
    ]
    n = 4

    dist, nxt = floyd_warshall_with_path(n, edges, directed=False)

    print("=" * 60)
    print("거리 행렬")
    print("=" * 60)
    header = "          " + "".join(f"{lb:>8}" for lb in labels)
    print(header)
    for i, row in enumerate(dist):
        cells = ["INF" if d == INF else str(int(d)) for d in row]
        print(f"  {labels[i]:>4} |" + "".join(f"{c:>8}" for c in cells))

    print()
    print("=" * 60)
    print("경로 복원")
    print("=" * 60)
    for src in range(n):
        for dst in range(n):
            if src == dst:
                continue
            path = reconstruct_path(nxt, src, dst)
            if path:
                p_str = " → ".join(labels[p] for p in path)
                print(f"  {labels[src]} → {labels[dst]}: "
                      f"거리={int(dist[src][dst])}km  경로={p_str}")

    print()
    print("=" * 60)
    print("서울 → 부산 상세")
    print("=" * 60)
    path_sb = reconstruct_path(nxt, 0, 3)
    p_str = " → ".join(labels[p] for p in path_sb)
    print(f"  경로: {p_str}")
    print(f"  거리: {int(dist[0][3])} km")
    print(f"  직행(450) vs 경유({int(dist[0][3])}) → "
          f"{'경유가 유리' if dist[0][3] < 450 else '직행이 유리'}")


if __name__ == "__main__":
    main()
