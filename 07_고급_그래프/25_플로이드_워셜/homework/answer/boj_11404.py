"""
백준 11404 — 플로이드
https://www.acmicpc.net/problem/11404

난이도 : Gold IV
Time  : O(V³)  V ≤ 100
Space : O(V²)

풀이:
    모든 쌍 최단 경로 → 플로이드-워셜.
    같은 (a, b) 버스 여러 개 → 최솟값으로 초기화.
    도달 불가 → 0 출력.
"""

import sys

input = sys.stdin.readline
INF = float("inf")


def solve() -> None:
    n = int(input())
    m = int(input())

    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0.0

    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a][b] = min(dist[a][b], float(c))

    # 플로이드-워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] == INF:
                continue
            for j in range(1, n + 1):
                via = dist[i][k] + dist[k][j]
                if via < dist[i][j]:
                    dist[i][j] = via

    # 출력 (도달 불가 → 0)
    result = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append("0" if dist[i][j] == INF else str(int(dist[i][j])))
        result.append(" ".join(row))
    print("\n".join(result))


if __name__ == "__main__":
    solve()
