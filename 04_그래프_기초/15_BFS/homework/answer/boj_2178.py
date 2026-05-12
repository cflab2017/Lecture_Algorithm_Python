"""
백준 2178 – 미로 탐색
https://www.acmicpc.net/problem/2178
Time  : O(N × M)
Space : O(N × M)

전략: BFS 최단 경로 (시작점 포함해서 이동 횟수 셈)
"""

import sys
from collections import deque

input = sys.stdin.readline

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def main() -> None:
    n, m = map(int, input().split())
    maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]

    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1    # 시작점 포함
    queue: deque[tuple[int, int]] = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        if r == n - 1 and c == m - 1:
            break
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    print(dist[n - 1][m - 1])


if __name__ == "__main__":
    main()
