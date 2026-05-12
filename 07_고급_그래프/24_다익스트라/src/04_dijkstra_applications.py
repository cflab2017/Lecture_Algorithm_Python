"""
단원 24 — 다익스트라: 응용 (K번째 최단 경로, 상태 그래프)
Topic : Modified Dijkstra — K-th Shortest Path & State Graph
Time  : K번째 최단: O(K * (V+E) log V) / 상태 그래프: O((V*S+E) log(V*S))
Space : O(V + E) ~ O(V * S)

설명:
    1) K번째 최단 경로: 목적지를 K번 방문하면 K번째 최단 거리
    2) 상태 그래프 Dijkstra: (위치, 추가상태) 를 노드로 확장
       예) 연료 제한, 통행료 무료 쿠폰 1회 사용
"""

import heapq
import sys

INF = sys.maxsize


# ──────────────────────────────────────────────
# 1. K번째 최단 경로
# ──────────────────────────────────────────────

def kth_shortest_path(
    graph: list[list[tuple[int, int]]],
    src: int,
    dst: int,
    k: int,
) -> int:
    """
    src → dst 의 K번째 최단 경로 거리를 반환한다.
    도달 불가이거나 K개 경로가 없으면 INF 반환.

    원리:
      - 각 노드를 최대 K번까지 방문 허용 (visit_cnt[v] 배열)
      - 힙에서 꺼낼 때 visit_cnt[v] 를 증가, K번 초과하면 스킵
      - dst 가 K번째로 꺼내지는 순간의 거리가 K번째 최단 거리

    Time : O(K * (V + E) log(KV))
    Space: O(K * V)
    """
    n = len(graph)
    visit_cnt = [0] * n
    heap: list[tuple[int, int]] = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        visit_cnt[u] += 1

        if visit_cnt[u] > k:  # K번 초과 → 스킵
            continue
        if u == dst and visit_cnt[u] == k:
            return d

        for v, w in graph[u]:
            if visit_cnt[v] < k:
                heapq.heappush(heap, (d + w, v))

    return INF


# ──────────────────────────────────────────────
# 2. 상태 그래프 다익스트라 — 통행료 무료 쿠폰 1회
# ──────────────────────────────────────────────

def dijkstra_with_coupon(
    graph: list[list[tuple[int, int]]],
    src: int,
    dst: int,
) -> int:
    """
    통행료 무료 쿠폰 1장을 사용할 수 있을 때 src→dst 최소 비용.

    상태: (현재 노드, 쿠폰 사용 여부)
    - 쿠폰 미사용: state=0
    - 쿠폰 사용됨: state=1

    dist[v][s]: 노드 v, 쿠폰 상태 s 에서의 최소 비용

    Time : O((2*(V+E)) log(2V))
    Space: O(V)
    """
    n = len(graph)
    # dist[node][coupon_used]
    dist = [[INF, INF] for _ in range(n)]
    dist[src][0] = 0
    # (cost, node, coupon_used)
    heap: list[tuple[int, int, int]] = [(0, src, 0)]

    while heap:
        cost, u, used = heapq.heappop(heap)
        if cost > dist[u][used]:
            continue

        for v, w in graph[u]:
            # 쿠폰 미사용 상태로 이동
            nc = cost + w
            if nc < dist[v][used]:
                dist[v][used] = nc
                heapq.heappush(heap, (nc, v, used))

            # 쿠폰 사용 (아직 안 썼을 때만)
            if used == 0:
                nc_free = cost  # 이 간선 무료
                if nc_free < dist[v][1]:
                    dist[v][1] = nc_free
                    heapq.heappush(heap, (nc_free, v, 1))

    return min(dist[dst])


# ──────────────────────────────────────────────
# 3. 상태 그래프 다익스트라 — 연료 제한
# ──────────────────────────────────────────────

def dijkstra_with_fuel(
    graph: list[list[tuple[int, int]]],
    fuel_graph: list[list[tuple[int, int]]],
    src: int,
    dst: int,
    max_fuel: int,
) -> int:
    """
    각 이동마다 연료를 소모하고, 특정 노드에서만 충전 가능할 때 최단 거리.
    간단화: 연료 소모 = 간선 가중치, fuel_graph 는 충전 노드 집합

    실제 상태: (노드, 현재 연료)
    이 예제에서는 단순 fuel 제한 도달 가능성만 확인한다.

    Time : O((V * F + E * F) log(V * F))  여기서 F = max_fuel
    Space: O(V * F)
    """
    n = len(graph)
    # dist[node][fuel] : 해당 상태까지의 최소 거리
    dist = [[INF] * (max_fuel + 1) for _ in range(n)]
    dist[src][max_fuel] = 0
    heap: list[tuple[int, int, int]] = [(0, src, max_fuel)]

    refuel_nodes = {v for edges in fuel_graph for v, _ in edges}

    while heap:
        cost, u, fuel = heapq.heappop(heap)
        if cost > dist[u][fuel]:
            continue
        if u == dst:
            return cost

        for v, w in graph[u]:
            if fuel < w:
                continue  # 연료 부족
            new_fuel = fuel - w
            # 충전 노드 도달 시 연료 보충
            if v in refuel_nodes:
                new_fuel = max_fuel
            nc = cost + w
            if nc < dist[v][new_fuel]:
                dist[v][new_fuel] = nc
                heapq.heappush(heap, (nc, v, new_fuel))

    return INF


def main() -> None:
    # ── K번째 최단 경로 ──
    print("=" * 55)
    print("1. K번째 최단 경로 (방향 그래프)")
    print("=" * 55)

    edges = [
        (0, 1, 1), (0, 2, 4),
        (1, 2, 2), (1, 3, 5),
        (2, 3, 1),
    ]
    n = 4
    g: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))

    for k in range(1, 5):
        d = kth_shortest_path(g, 0, 3, k)
        label = str(d) if d < INF else "INF (없음)"
        print(f"  {k}번째 최단 경로 (0→3): {label}")

    # ── 통행료 무료 쿠폰 ──
    print()
    print("=" * 55)
    print("2. 통행료 무료 쿠폰 1장")
    print("=" * 55)

    # 0 --10-- 1 --10-- 3
    # |                 |
    # 1                 1
    # |                 |
    # 2 ---1--- (고속도로, 통행료 100)--- 3
    edges2 = [
        (0, 1, 10), (1, 3, 10),
        (0, 2, 1),  (2, 3, 100),
    ]
    g2: list[list[tuple[int, int]]] = [[] for _ in range(4)]
    for u, v, w in edges2:
        g2[u].append((v, w))

    normal = INF  # 일반 다익스트라 결과
    heap_tmp: list[tuple[int, int]] = [(0, 0)]
    dist_tmp = [INF] * 4
    dist_tmp[0] = 0
    import heapq as hq
    while heap_tmp:
        d, u = hq.heappop(heap_tmp)
        if d > dist_tmp[u]:
            continue
        for v, w in g2[u]:
            if dist_tmp[u] + w < dist_tmp[v]:
                dist_tmp[v] = dist_tmp[u] + w
                hq.heappush(heap_tmp, (dist_tmp[v], v))
    normal = dist_tmp[3]

    coupon_result = dijkstra_with_coupon(g2, 0, 3)
    print(f"  쿠폰 없이 0→3: {normal}")
    print(f"  쿠폰 1장으로 0→3: {coupon_result}")
    print(f"  절감 비용: {normal - coupon_result}")

    print()
    print("=" * 55)
    print("응용 패턴 요약")
    print("=" * 55)
    print("  K번째 최단: visit_cnt[v] <= K 허용")
    print("  상태 추가 : (노드, 상태) 복합 키로 dist 확장")
    print("  쿠폰/연료 : 상태 차원 1개 추가 → O(V*S log(V*S))")


if __name__ == "__main__":
    main()
