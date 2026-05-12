"""
Topic  : 백준 스타일 그래프 입력 파싱
Time   : O(V + E)
Space  : O(V + E)

백준 그래프 문제의 전형적인 입력 형식:
첫 줄: N M (노드 수, 간선 수)
다음 M줄: u v [w] (간선 정보)
"""

import sys
from io import StringIO


# ── 전형적인 백준 입력 파싱 ────────────────────────────────────────────────────

def parse_unweighted_graph(data: str, directed: bool = False) -> tuple[int, list[list[int]]]:
    """비가중 그래프 파싱.

    입력 형식:
      첫 줄: N M
      다음 M줄: u v
    """
    tokens = data.split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1

    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return n, graph


def parse_weighted_graph(
    data: str, directed: bool = False
) -> tuple[int, list[list[tuple[int, int]]]]:
    """가중 그래프 파싱.

    입력 형식:
      첫 줄: N M
      다음 M줄: u v w
    """
    tokens = data.split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1

    graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        w = int(tokens[idx]); idx += 1
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))

    return n, graph


# ── 그리드 그래프 파싱 ────────────────────────────────────────────────────────

def parse_grid(data: str) -> list[list[str]]:
    """NxM 그리드 파싱.

    입력 형식:
      첫 줄: N M
      다음 N줄: 각 행 (공백 없는 문자열 또는 공백 구분)
    """
    lines = data.strip().split('\n')
    n, m = map(int, lines[0].split())
    grid = []
    for i in range(1, n + 1):
        row = list(lines[i].strip())
        grid.append(row)
    return grid


def grid_to_graph(
    grid: list[list[str]],
    passable: str = '0',
) -> tuple[int, int, list[list[tuple[int, int]]]]:
    """그리드를 그래프로 변환 (4방향).

    Returns:
        (rows, cols, graph)  graph[(r,c)]로 접근
    """
    rows = len(grid)
    cols = len(grid[0])
    # (r, c) → 노드 번호 : r*cols + c
    total = rows * cols
    graph: list[list[tuple[int, int]]] = [[] for _ in range(total)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != passable:
                continue
            node = r * cols + c
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == passable:
                        nnode = nr * cols + nc
                        graph[node].append((nnode, 1))

    return rows, cols, graph


# ── 데모 ────────────────────────────────────────────────────────────────────

def demo_parse() -> None:
    # 백준 1260 스타일 입력
    input1 = """4 5 1
1 2
1 3
1 4
2 4
3 4"""
    tokens = input1.split()
    n, m, start = int(tokens[0]), int(tokens[1]), int(tokens[2])
    data_for_parse = f"{n} {m}\n" + '\n'.join(
        tokens[3:3 + m * 2][i*2] + ' ' + tokens[3:3 + m * 2][i*2 + 1]
        for i in range(m)
    )

    n2, graph = parse_unweighted_graph(data_for_parse)
    print(f"=== 비가중 그래프 파싱 ===")
    print(f"N={n2}, 시작={start}")
    for i in range(1, n2 + 1):
        print(f"  {i}: {sorted(graph[i])}")

    # 가중 그래프
    input2 = """5 6
1 2 10
1 3 3
2 4 7
3 2 4
3 4 8
4 5 5"""
    n3, wgraph = parse_weighted_graph(input2, directed=True)
    print(f"\n=== 가중 방향 그래프 파싱 ===")
    print(f"N={n3}")
    for i in range(1, n3 + 1):
        if wgraph[i]:
            print(f"  {i}: {wgraph[i]}")

    # 그리드
    input3 = """4 6
101110
101010
111010
000010"""
    grid = parse_grid(input3)
    print(f"\n=== 그리드 파싱 ===")
    for row in grid:
        print(f"  {''.join(row)}")

    rows, cols, ggraph = grid_to_graph(grid, passable='1')
    passable_count = sum(1 for row in grid for c in row if c == '1')
    print(f"  통과 가능 칸: {passable_count}개")


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_parse()

    # 간선 입력 시 일반 패턴 출력
    print("\n=== 백준 그래프 문제 공통 패턴 ===")
    print("""
# 표준 패턴
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 1-indexed

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향이면
""")
