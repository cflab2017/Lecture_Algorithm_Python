"""
백준 1012 – 유기농 배추
https://www.acmicpc.net/problem/1012
Time  : O(M × N)
Space : O(M × N)
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def main() -> None:
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        grid = [[0] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            grid[y][x] = 1    # 주의: x=열, y=행

        visited = [[False] * m for _ in range(n)]

        def dfs(r: int, c: int) -> None:
            visited[r][c] = True
            for i in range(4):
                nr, nc = r + DR[i], c + DC[i]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc)

        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1 and not visited[r][c]:
                    dfs(r, c)
                    count += 1

        print(count)


if __name__ == "__main__":
    main()
