"""
백준 2667 – 단지번호붙이기
https://www.acmicpc.net/problem/2667
Time  : O(N²)
Space : O(N²)
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def main() -> None:
    n = int(input())
    grid = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    sizes: list[int] = []

    def dfs(r: int, c: int) -> int:
        visited[r][c] = True
        size = 1
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 1:
                size += dfs(nr, nc)
        return size

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1 and not visited[r][c]:
                sizes.append(dfs(r, c))

    sizes.sort()
    print(len(sizes))
    print('\n'.join(map(str, sizes)))


if __name__ == "__main__":
    main()
