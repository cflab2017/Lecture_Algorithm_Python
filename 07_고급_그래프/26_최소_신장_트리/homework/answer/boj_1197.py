"""
백준 1197 — 최소 스패닝 트리
https://www.acmicpc.net/problem/1197

난이도 : Gold IV
Time  : O(E log E)
Space : O(V + E)

풀이:
    크루스칼 MST.
    음수 가중치도 정상 처리됨.
"""

import sys

input = sys.stdin.readline


def solve() -> None:
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))   # (가중치, u, v) 형태로 저장

    edges.sort()

    # Union-Find
    parent = list(range(V + 1))
    rank = [0] * (V + 1)

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
            if count == V - 1:
                break

    print(total)


if __name__ == "__main__":
    solve()
