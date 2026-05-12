"""
단원 24 — 다익스트라: 음수 간선 문제 + 벨만-포드 대안
Topic : Negative Weights — Why Dijkstra Fails + Bellman-Ford
Time  : 다익스트라 O((V+E) log V) / 벨만-포드 O(VE)
Space : O(V + E)

설명:
    음수 간선이 존재할 때 다익스트라가 오답을 내는 이유를 직접 확인하고,
    벨만-포드(Bellman-Ford) 알고리즘으로 올바른 답을 구한다.
    음수 사이클(negative cycle) 검출 방법도 포함한다.
"""

import heapq
import sys

INF = sys.maxsize


# ──────────────────────────────────────────────
# 1. 다익스트라 (음수 간선에서 오답)
# ──────────────────────────────────────────────

def dijkstra(graph: list[list[tuple[int, int]]], src: int) -> list[int]:
    """
    기본 다익스트라 (음수 간선 미지원).

    Time : O((V + E) log V)
    Space: O(V + E)
    """
    n = len(graph)
    dist = [INF] * n
    dist[src] = 0
    heap: list[tuple[int, int]] = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


# ──────────────────────────────────────────────
# 2. 벨만-포드 (음수 간선 지원, 음수 사이클 검출)
# ──────────────────────────────────────────────

def bellman_ford(
    n: int,
    edges: list[tuple[int, int, int]],
    src: int,
) -> tuple[list[int], bool]:
    """
    벨만-포드 알고리즘.

    Args:
        n    : 노드 수
        edges: (u, v, w) 방향 간선 목록
        src  : 출발 노드

    Returns:
        (dist, has_negative_cycle)
        dist[v]              : src → v 최단 거리
        has_negative_cycle   : True 이면 음수 사이클 존재

    Time : O(V * E)  — V-1 번 완화 반복 + 1번 사이클 체크
    Space: O(V)
    """
    dist = [INF] * n
    dist[src] = 0

    # V-1 번 반복: 최단 경로는 V-1 개 이하의 간선을 가짐
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:   # 조기 종료 최적화
            break

    # V번째 반복에서도 완화되면 음수 사이클 존재
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, has_negative_cycle


# ──────────────────────────────────────────────
# 3. 실험
# ──────────────────────────────────────────────

def main() -> None:
    # ── 케이스 1: 음수 간선 그래프 ──
    # 0 ─4─▶ 1 ─(-3)─▶ 2
    # 0 ─2─▶ 2
    #
    # 실제 최단: 0→2 = 0+4+(-3) = 1
    # 다익스트라: 먼저 0→2(2)를 확정하므로 오답!
    print("=" * 55)
    print("케이스 1: 음수 간선 그래프")
    print("  0 --4→ 1 --(-3)→ 2")
    print("  0 --2→ 2")
    print("=" * 55)

    edges1 = [(0, 1, 4), (1, 2, -3), (0, 2, 2)]
    n1 = 3

    # 다익스트라용 그래프
    g_dijk = [[] for _ in range(n1)]
    for u, v, w in edges1:
        g_dijk[u].append((v, w))

    dist_dijk = dijkstra(g_dijk, 0)
    dist_bf, neg_cycle = bellman_ford(n1, edges1, 0)

    print(f"{'노드':>5} {'다익스트라':>12} {'벨만-포드':>12} {'정답?'}")
    print("-" * 50)
    for i in range(n1):
        d = dist_dijk[i] if dist_dijk[i] < INF else "INF"
        b = dist_bf[i] if dist_bf[i] < INF else "INF"
        correct = "✓" if d == b else "✗ 오답!"
        print(f"  0 → {i}  {str(d):>10}  {str(b):>10}  {correct}")

    print(f"\n음수 사이클: {'있음' if neg_cycle else '없음'}")

    # ── 케이스 2: 음수 사이클 ──
    print()
    print("=" * 55)
    print("케이스 2: 음수 사이클 그래프")
    print("  0 --1→ 1 --(-2)→ 2 --1→ 1  (사이클: 1→2→1)")
    print("=" * 55)

    edges2 = [(0, 1, 1), (1, 2, -2), (2, 1, 1)]
    dist2, neg2 = bellman_ford(3, edges2, 0)
    print(f"음수 사이클 감지: {'있음 → 최단 거리 정의 불가' if neg2 else '없음'}")

    # ── 케이스 3: 정상 (음수 간선 없음) ──
    print()
    print("=" * 55)
    print("케이스 3: 정상 그래프 (음수 없음) — 두 알고리즘 동일")
    print("=" * 55)

    edges3 = [(0, 1, 3), (0, 2, 1), (1, 3, 2), (2, 1, 1), (2, 3, 5)]
    n3 = 4
    g3 = [[] for _ in range(n3)]
    for u, v, w in edges3:
        g3[u].append((v, w))

    dist3_d = dijkstra(g3, 0)
    dist3_b, _ = bellman_ford(n3, edges3, 0)

    for i in range(n3):
        dd = dist3_d[i] if dist3_d[i] < INF else "INF"
        db = dist3_b[i] if dist3_b[i] < INF else "INF"
        print(f"  0 → {i}: 다익스트라={dd}, 벨만-포드={db}")

    # ── 알고리즘 비교 요약 ──
    print()
    print("=" * 55)
    print("알고리즘 선택 가이드")
    print("=" * 55)
    print("  음수 간선 없음     → 다익스트라  O((V+E) log V)")
    print("  음수 간선 있음     → 벨만-포드   O(VE)")
    print("  음수 사이클 감지   → 벨만-포드 V번째 반복 확인")
    print("  전쌍 최단 경로     → 플로이드-워셜 O(V³)")


if __name__ == "__main__":
    main()
