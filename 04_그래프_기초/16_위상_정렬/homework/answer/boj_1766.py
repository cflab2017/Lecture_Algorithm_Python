"""
백준 1766 – 문제집
https://www.acmicpc.net/problem/1766
Time  : O((V + E) log V)
Space : O(V + E)

전략: heapq(최소 힙) + 위상 정렬
     선수 조건 완료 + 번호 작은 것 먼저
"""

import sys
import heapq

input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    heap: list[int] = [i for i in range(1, n + 1) if in_degree[i] == 0]
    heapq.heapify(heap)
    result: list[int] = []

    while heap:
        prob = heapq.heappop(heap)
        result.append(prob)
        for nxt in graph[prob]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heapq.heappush(heap, nxt)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
