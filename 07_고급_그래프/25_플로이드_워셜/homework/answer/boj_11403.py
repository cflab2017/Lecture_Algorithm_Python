"""
백준 11403 — 경로 찾기
https://www.acmicpc.net/problem/11403

난이도 : Silver I
Time  : O(V³)  V ≤ 100
Space : O(V²)

풀이:
    전이 폐쇄(Transitive Closure) 문제.
    플로이드-워셜 OR 버전: reach[i][j] |= reach[i][k] and reach[k][j]
    i==j 는 입력값 무시, 0 으로 간주 (자기 자신 경로는 문제에서 묻지 않음).

    주의: 자기 자신(i==j)의 초기값도 0이어야 하므로 dist[i][i] = 0 초기화 안 함.
"""

import sys

input = sys.stdin.readline


def solve() -> None:
    N = int(input())
    adj = []
    for _ in range(N):
        row = list(map(int, input().split()))
        adj.append(row)

    # 전이 폐쇄 (0-indexed, i==j 는 0 유지)
    reach = [row[:] for row in adj]   # 직접 연결 복사

    for k in range(N):
        for i in range(N):
            if not reach[i][k]:
                continue
            for j in range(N):
                if reach[k][j]:
                    reach[i][j] = 1

    # 출력
    result = []
    for i in range(N):
        result.append(" ".join(map(str, reach[i])))
    print("\n".join(result))


if __name__ == "__main__":
    solve()
