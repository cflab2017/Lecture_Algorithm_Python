"""
백준 1922 — 네트워크 연결
https://www.acmicpc.net/problem/1922

난이도 : Gold IV
Time  : O(E log E)
Space : O(V + E)

풀이:
    크루스칼 MST. 백준 1197과 구조 동일.
    N개 컴퓨터를 최소 비용으로 모두 연결.
"""

import sys

input = sys.stdin.readline


def solve() -> None:
    N = int(input())
    M = int(input())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))

    edges.sort()

    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True

    total = 0
    count = 0
    for c, a, b in edges:
        if union(a, b):
            total += c
            count += 1
            if count == N - 1:
                break

    print(total)


if __name__ == "__main__":
    solve()
