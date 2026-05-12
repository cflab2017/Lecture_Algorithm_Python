"""
Topic  : 격자 DFS — 섬(영역) 탐색, 4방향 이동
Time   : O(R × C)
Space  : O(R × C) 재귀 스택
"""

import sys
sys.setrecursionlimit(200_000)

# 4방향: 상하좌우
DR4 = [-1, 1, 0, 0]
DC4 = [0, 0, -1, 1]

# 8방향: 대각선 포함
DR8 = [-1, -1, -1, 0, 0, 1, 1, 1]
DC8 = [-1, 0, 1, -1, 1, -1, 0, 1]


# ── 섬의 개수 세기 ────────────────────────────────────────────────────────────

def count_islands(grid: list[list[str]]) -> int:
    """'1' 로 표시된 섬의 개수를 반환 (4방향 연결).

    DFS로 섬을 방문하면서 '0' 으로 표시.
    """
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '0'       # 방문 표시
        for i in range(4):
            dfs(r + DR4[i], c + DC4[i])

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count


# ── 섬의 크기 목록 ────────────────────────────────────────────────────────────

def island_sizes(grid: list[list[int]]) -> list[int]:
    """각 섬의 크기(셀 수) 목록 반환.

    grid: 0=바다, 1=육지
    """
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    sizes: list[int] = []

    def dfs(r: int, c: int) -> int:
        visited[r][c] = True
        size = 1
        for i in range(4):
            nr, nc = r + DR4[i], c + DC4[i]
            if (0 <= nr < rows and 0 <= nc < cols
                    and not visited[nr][nc] and grid[nr][nc] == 1):
                size += dfs(nr, nc)
        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                sizes.append(dfs(r, c))

    return sorted(sizes)


# ── 단지 번호 붙이기 (백준 2667 스타일) ──────────────────────────────────────

def label_and_count(grid: list[list[int]]) -> tuple[int, list[int]]:
    """각 단지에 번호를 붙이고 (단지 수, 각 단지 크기 목록) 반환.

    백준 2667 스타일.
    """
    rows = len(grid)
    cols = len(grid[0])
    label = [[0] * cols for _ in range(rows)]
    comp_id = 0
    sizes: list[int] = []

    def dfs(r: int, c: int, cid: int) -> int:
        label[r][c] = cid
        size = 1
        for i in range(4):
            nr, nc = r + DR4[i], c + DC4[i]
            if (0 <= nr < rows and 0 <= nc < cols
                    and label[nr][nc] == 0 and grid[nr][nc] == 1):
                size += dfs(nr, nc, cid)
        return size

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and label[r][c] == 0:
                comp_id += 1
                sizes.append(dfs(r, c, comp_id))

    return comp_id, sorted(sizes)


# ── 출력 ────────────────────────────────────────────────────────────────────

def print_grid(grid: list[list], title: str = "격자") -> None:
    """격자 출력."""
    print(f"\n=== {title} ===")
    for row in grid:
        print("  " + "".join(str(c) for c in row))


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 섬의 개수 세기
    grid1 = [
        list("11010"),
        list("11010"),
        list("00100"),
        list("10001"),
    ]
    print_grid(grid1, "원본 격자 (1=육지, 0=바다)")
    cnt = count_islands([row[:] for row in grid1])  # 복사본 전달
    print(f"섬의 개수: {cnt}")

    # 섬의 크기
    grid2 = [
        [1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1],
    ]
    print_grid(grid2, "섬 크기 격자")
    sizes = island_sizes(grid2)
    print(f"섬 크기 목록 (오름차순): {sizes}")
    print(f"총 섬 수: {len(sizes)}, 가장 큰 섬: {max(sizes)}")

    # 단지 번호 붙이기 (백준 2667 스타일)
    grid3 = [
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0],
    ]
    print_grid(grid3, "단지 격자 (백준 2667 스타일)")
    num_comps, comp_sizes = label_and_count(grid3)
    print(f"단지 수: {num_comps}")
    print(f"단지별 집 수 (오름차순): {comp_sizes}")

    # 정확성 검증
    assert count_islands([list("11010"),
                           list("11010"),
                           list("00100"),
                           list("10001")]) == 3
    print("\n정확성 검증: PASS")
