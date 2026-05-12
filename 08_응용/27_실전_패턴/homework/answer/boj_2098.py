"""
백준 2098 — 외판원 순회 (TSP)
https://www.acmicpc.net/problem/2098

난이도 : Gold I
Time  : O(2ⁿ * n²)  n ≤ 16
Space : O(2ⁿ * n)

풀이:
    비트마스크 DP (Held-Karp 알고리즘).

    dp[mask][v] = mask 비트 집합(방문한 도시들)에서 현재 v에 있을 때 최소 비용.

    초기: dp[1 << i][i] = 0  (i번 도시에서 출발)
          또는 dp[1][0] = 0  (0번에서 출발, 순환이므로 어디서든 같음)

    전이: for next != v, next not in mask:
            dp[mask | (1<<next)][next] = min(..., dp[mask][v] + W[v][next])

    답: min(dp[(1<<n)-1][v] + W[v][0]) for all v

    W[i][j] = 0 이면 경로 없음.
"""

import sys

input = sys.stdin.readline
INF = sys.maxsize


def solve() -> None:
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]

    FULL = (1 << N) - 1
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1][0] = 0   # 0번 도시에서 출발

    for mask in range(1 << N):
        for u in range(N):
            if dp[mask][u] == INF:
                continue
            if not (mask >> u & 1):
                continue

            for v in range(N):
                if mask >> v & 1:    # 이미 방문
                    continue
                if W[u][v] == 0:     # 경로 없음
                    continue
                new_mask = mask | (1 << v)
                cost = dp[mask][u] + W[u][v]
                if cost < dp[new_mask][v]:
                    dp[new_mask][v] = cost

    # 모든 도시 방문 후 0번으로 귀환
    ans = INF
    for v in range(1, N):
        if dp[FULL][v] != INF and W[v][0] != 0:
            ans = min(ans, dp[FULL][v] + W[v][0])

    print(ans)


if __name__ == "__main__":
    solve()
