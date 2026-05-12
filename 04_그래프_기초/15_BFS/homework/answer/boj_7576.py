"""
백준 7576 – 토마토
https://www.acmicpc.net/problem/7576
Time  : O(M × N)
Space : O(M × N)

전략: 다중 시작점 BFS — 모든 익은 토마토에서 동시에 시작
"""

import sys
from collections import deque

input = sys.stdin.readline

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def main() -> None:
    m, n = map(int, input().split())   # m=열 수, n=행 수
    grid = [list(map(int, input().split())) for _ in range(n)]

    dist = [[-1] * m for _ in range(n)]
    queue: deque[tuple[int, int]] = deque()

    # 모든 익은 토마토를 큐에 삽입
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    # 결과 계산
    ans = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 0 and dist[r][c] == -1:
                print(-1)
                return
            if dist[r][c] != -1:
                ans = max(ans, dist[r][c])

    print(ans)


if __name__ == "__main__":
    main()
