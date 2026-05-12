"""
백준 1389 — 케빈 베이컨의 6단계 법칙
https://www.acmicpc.net/problem/1389

난이도 : Silver I
Time  : O(V³)  V ≤ 100
Space : O(V²)

풀이:
    무방향 그래프 플로이드-워셜.
    각 사람 i 의 케빈 베이컨 수 = sum(dist[i][j] for j != i).
    가장 작은 케빈 베이컨 수를 가진 사람 번호 출력 (동점이면 번호 작은 것).
"""

import sys

input = sys.stdin.readline
INF = float("inf")


def solve() -> None:
    N, M = map(int, input().split())

    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0.0

    for _ in range(M):
        a, b = map(int, input().split())
        dist[a][b] = 1.0
        dist[b][a] = 1.0

    # 플로이드-워셜
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if dist[i][k] == INF:
                continue
            for j in range(1, N + 1):
                via = dist[i][k] + dist[k][j]
                if via < dist[i][j]:
                    dist[i][j] = via

    # 케빈 베이컨 수 계산
    best_person = 1
    best_score = sum(dist[1][j] for j in range(1, N + 1) if j != 1)

    for i in range(2, N + 1):
        score = sum(dist[i][j] for j in range(1, N + 1) if j != i)
        if score < best_score:
            best_score = score
            best_person = i

    print(best_person)


if __name__ == "__main__":
    solve()
