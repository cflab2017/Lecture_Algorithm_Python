"""
백준 9205 – 맥주 마시면서 걸어가기
https://www.acmicpc.net/problem/9205
Time  : O(T × (N+2)²)   T = 테스트 케이스
Space : O(N²)

전략: 맨해튼 거리 ≤ 1000 이면 이동 가능
     BFS/DFS로 집(0) → 페스티벌(N+1) 도달 가능 여부 판별
"""

import sys
from collections import deque

input = sys.stdin.readline


def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        home = list(map(int, input().split()))
        stores = [list(map(int, input().split())) for _ in range(n)]
        festival = list(map(int, input().split()))

        # 집(0), 편의점(1~n), 페스티벌(n+1) 노드
        nodes = [home] + stores + [festival]
        total = n + 2

        def can_move(i: int, j: int) -> bool:
            return (abs(nodes[i][0] - nodes[j][0]) +
                    abs(nodes[i][1] - nodes[j][1])) <= 1000

        # BFS
        visited = [False] * total
        queue: deque[int] = deque([0])
        visited[0] = True
        found = False

        while queue:
            cur = queue.popleft()
            if cur == total - 1:
                found = True
                break
            for nxt in range(total):
                if not visited[nxt] and can_move(cur, nxt):
                    visited[nxt] = True
                    queue.append(nxt)

        print("happy" if found else "sad")


if __name__ == "__main__":
    main()
