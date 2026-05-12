"""
Topic  : 다중 시작점 BFS — 여러 시작점 동시 탐색
Time   : O(V + E) 또는 O(R × C)
Space  : O(V)
"""

from collections import deque

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


# ── 다중 시작점 BFS (그래프) ─────────────────────────────────────────────────

def multi_source_bfs(
    graph: list[list[int]],
    sources: list[int],
    n: int,
) -> list[int]:
    """여러 시작점에서 동시에 BFS.

    각 노드까지 가장 가까운 시작점으로부터의 거리 반환.
    """
    dist = [-1] * (n + 1)
    queue: deque[int] = deque()

    # 모든 시작점을 초기 큐에 삽입
    for src in sources:
        dist[src] = 0
        queue.append(src)

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                queue.append(nxt)

    return dist


# ── 토마토 문제 스타일 (백준 7576) ──────────────────────────────────────────

def tomato_ripening(grid: list[list[int]]) -> int:
    """익은 토마토(1)에서 인접한 토마토를 하루에 익힘.

    모든 토마토가 익는 데 걸리는 최소 일수.
    0 = 안 익은 토마토, 1 = 익은 토마토, -1 = 빈 칸

    Returns:
        최소 일수 (-1이면 불가능)
    """
    rows = len(grid)
    cols = len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    queue: deque[tuple[int, int]] = deque()

    # 모든 익은 토마토를 큐에 삽입
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0
                    and dist[nr][nc] == -1):
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    # 안 익은 토마토가 남아있으면 -1
    max_days = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and dist[r][c] == -1:
                return -1
            if dist[r][c] != -1:
                max_days = max(max_days, dist[r][c])

    return max_days


# ── 다중 시작점 BFS — 가장 가까운 시작점 색칠 ────────────────────────────────

def color_by_nearest_source(
    grid: list[list[int]],
    sources: list[tuple[int, int]],
) -> list[list[int]]:
    """각 빈 칸을 가장 가까운 시작점 색으로 칠하기.

    Returns:
        color 배열 (각 칸이 몇 번 시작점에서 왔는가, -1=도달 불가)
    """
    rows = len(grid)
    cols = len(grid[0])
    color = [[-1] * cols for _ in range(rows)]
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue: deque[tuple[int, int, int]] = deque()   # (r, c, color_id)

    for i, (r, c) in enumerate(sources):
        color[r][c] = i
        dist[r][c] = 0
        queue.append((r, c, i))

    while queue:
        r, c, cid = queue.popleft()
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0
                    and dist[nr][nc] == float('inf')):
                dist[nr][nc] = dist[r][c] + 1
                color[nr][nc] = cid
                queue.append((nr, nc, cid))

    return color


# ── 시각화 ──────────────────────────────────────────────────────────────────

def print_grid(grid: list[list], title: str) -> None:
    symbols = {0: ".", 1: "T", -1: "□", 2: "2"}
    print(f"\n=== {title} ===")
    for row in grid:
        print("  " + " ".join(
            str(c) if isinstance(c, int) and c >= 0 else ("□" if c == -1 else str(c))
            for c in row
        ))


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 토마토 문제 시뮬레이션
    tomato_grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],   # 오른쪽 아래
    ]
    print("=" * 50)
    print("토마토 문제 (다중 시작점 BFS)")
    print("=" * 50)
    print_grid(tomato_grid, "초기 상태 (T=익은 토마토)")

    days = tomato_ripening([row[:] for row in tomato_grid])
    print(f"모든 토마토 익는 데 필요한 일수: {days}")

    # 여러 시작점
    multi_tomato = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
    ]
    print_grid(multi_tomato, "다중 시작점 토마토 (□=빈 칸)")
    days2 = tomato_ripening([row[:] for row in multi_tomato])
    print(f"모든 토마토 익는 데 필요한 일수: {days2}")

    # 불가능 케이스
    impossible = [
        [1, 0, -1, 0, 0],
    ]
    days3 = tomato_ripening(impossible)
    print(f"불가능 케이스: {days3}  (-1이면 불가)")

    # 그래프 다중 시작점
    print("\n=== 그래프 다중 시작점 BFS ===")
    n = 7
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
    g: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)

    sources = [1, 7]
    dist_multi = multi_source_bfs(g, sources, n)
    print(f"시작점 {sources}, 최단 거리: {dist_multi[1:]}")
    print("  ← 각 노드가 가장 가까운 시작점까지의 거리")

    # 정확성 검증
    assert tomato_ripening([[1, 0, 0], [0, 0, 0]]) == 4
    print("\n정확성 검증: PASS")
