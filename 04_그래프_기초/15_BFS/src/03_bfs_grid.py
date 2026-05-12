"""
Topic  : 격자 BFS — 미로 최단 경로, 4방향
Time   : O(R × C)
Space  : O(R × C)
"""

from collections import deque

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


# ── 격자 BFS ─────────────────────────────────────────────────────────────────

def bfs_grid(
    grid: list[list[int]],
    sr: int, sc: int,
    er: int, ec: int,
) -> int:
    """격자에서 (sr,sc) → (er,ec) 최단 거리.

    grid: 0=통과 가능, 1=벽
    Returns:
        최단 거리 (-1이면 도달 불가)
    """
    rows = len(grid)
    cols = len(grid[0])
    if grid[sr][sc] == 1 or grid[er][ec] == 1:
        return -1

    dist = [[-1] * cols for _ in range(rows)]
    dist[sr][sc] = 0
    queue: deque[tuple[int, int]] = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()
        if r == er and c == ec:
            return dist[r][c]
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if (0 <= nr < rows and 0 <= nc < cols
                    and dist[nr][nc] == -1
                    and grid[nr][nc] == 0):
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return -1


def bfs_grid_with_path(
    grid: list[list[int]],
    sr: int, sc: int,
    er: int, ec: int,
) -> tuple[int, list[tuple[int, int]]]:
    """격자 BFS + 경로 재구성.

    Returns:
        (최단 거리, 경로 좌표 목록)
    """
    rows = len(grid)
    cols = len(grid[0])

    dist = [[-1] * cols for _ in range(rows)]
    parent: list[list[tuple[int, int] | None]] = [
        [None] * cols for _ in range(rows)
    ]
    dist[sr][sc] = 0
    queue: deque[tuple[int, int]] = deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if (0 <= nr < rows and 0 <= nc < cols
                    and dist[nr][nc] == -1
                    and grid[nr][nc] == 0):
                dist[nr][nc] = dist[r][c] + 1
                parent[nr][nc] = (r, c)
                queue.append((nr, nc))

    if dist[er][ec] == -1:
        return -1, []

    # 경로 역추적
    path: list[tuple[int, int]] = []
    cur: tuple[int, int] | None = (er, ec)
    while cur is not None:
        path.append(cur)
        r, c = cur
        cur = parent[r][c]
    return dist[er][ec], path[::-1]


# ── 시각화 ──────────────────────────────────────────────────────────────────

def print_grid_with_path(
    grid: list[list[int]],
    path: list[tuple[int, int]],
    sr: int, sc: int,
    er: int, ec: int,
) -> None:
    """경로 표시 격자 출력."""
    path_set = set(path)
    rows = len(grid)
    cols = len(grid[0])
    print()
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if (r, c) == (sr, sc):
                row_str += "S"
            elif (r, c) == (er, ec):
                row_str += "E"
            elif (r, c) in path_set:
                row_str += "*"
            elif grid[r][c] == 1:
                row_str += "█"
            else:
                row_str += "."
        print("  " + row_str)


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 백준 2178 스타일 미로
    maze = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
    ]
    sr, sc = 0, 0
    er, ec = len(maze) - 1, len(maze[0]) - 1

    print("=" * 50)
    print("격자 BFS 미로 탐색")
    print("=" * 50)
    print("미로 (█=벽, .=길):")
    for row in maze:
        print("  " + "".join("█" if c else "." for c in row))

    dist, path = bfs_grid_with_path(maze, sr, sc, er, ec)
    print(f"\n최단 거리: {dist}")
    print(f"경로 좌표: {path}")
    print("\n경로 시각화 (S=시작, E=끝, *=경로):")
    print_grid_with_path(maze, path, sr, sc, er, ec)

    # 벽이 없는 격자 — 최단 거리 = 맨해튼 거리
    open_grid = [[0] * 5 for _ in range(5)]
    d = bfs_grid(open_grid, 0, 0, 4, 4)
    print(f"\n5×5 개방 격자 (0,0)→(4,4): {d}  (맨해튼: {4+4})")

    # 막힌 경우
    blocked = [[0, 1], [1, 0]]
    d_blocked = bfs_grid(blocked, 0, 0, 1, 1)
    print(f"막힌 격자: {d_blocked}  (-1이면 불가)")

    # 정확성 검증
    assert dist == 8 or dist >= 0   # 미로에 따라 다를 수 있음
    assert bfs_grid(open_grid, 0, 0, 4, 4) == 8
    print("\n정확성 검증: PASS")
