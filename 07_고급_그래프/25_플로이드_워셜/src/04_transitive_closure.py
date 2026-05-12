"""
단원 25 — 플로이드-워셜: 전이 폐쇄 (Transitive Closure)
Topic : Transitive Closure (도달 가능성) via Floyd-Warshall
Time  : O(V³)  — 비트 연산으로 O(V³/64) 최적화 가능
Space : O(V²)

설명:
    reach[i][j] = True 이면 i에서 j로 도달 가능.
    플로이드-워셜의 min(dist) 대신 OR(reach) 로 변경.
    reach[i][j] |= (reach[i][k] and reach[k][j])
    또는 정수 비트마스크: reach[i] |= reach[k] if reach[i] >> k & 1
"""


def transitive_closure_bool(
    n: int,
    edges: list[tuple[int, int]],
    directed: bool = True,
) -> list[list[bool]]:
    """
    bool 행렬로 전이 폐쇄를 계산한다.

    Time : O(V³)
    Space: O(V²)
    """
    reach: list[list[bool]] = [[False] * n for _ in range(n)]

    # 자기 자신은 도달 가능
    for i in range(n):
        reach[i][i] = True

    # 직접 연결된 간선
    for u, v in edges:
        reach[u][v] = True
        if not directed:
            reach[v][u] = True

    # 플로이드-워셜 (OR 버전)
    for k in range(n):
        for i in range(n):
            if not reach[i][k]:
                continue
            for j in range(n):
                if reach[k][j]:
                    reach[i][j] = True

    return reach


def transitive_closure_bitset(
    n: int,
    edges: list[tuple[int, int]],
    directed: bool = True,
) -> list[int]:
    """
    정수 비트마스크로 전이 폐쇄를 계산한다.
    reach[i] 의 j번째 비트가 1이면 i→j 도달 가능.

    Time : O(V³ / 64)  (정수 비트 연산 활용)
    Space: O(V²/64) → 실질적으로 O(V) 정수 리스트
    """
    reach = [0] * n

    # 자기 자신
    for i in range(n):
        reach[i] |= (1 << i)

    # 직접 연결
    for u, v in edges:
        reach[u] |= (1 << v)
        if not directed:
            reach[v] |= (1 << u)

    # 플로이드 (비트 OR)
    for k in range(n):
        for i in range(n):
            if reach[i] >> k & 1:    # i → k 도달 가능
                reach[i] |= reach[k] # i → k의 모든 이웃 도달 가능

    return reach


def print_reach_matrix(reach: list[list[bool]], labels: list[str]) -> None:
    """도달 가능성 행렬 출력."""
    n = len(labels)
    header = "      " + "".join(f"{lb:>5}" for lb in labels)
    print(header)
    print("      " + "─" * (5 * n))
    for i, row in enumerate(reach):
        cells = ["O" if r else "X" for r in row]
        print(f"  {labels[i]:>3} |" + "".join(f"{c:>5}" for c in cells))


def main() -> None:
    # ── 예제 1: 방향 그래프 ──
    print("=" * 55)
    print("예제 1: 방향 그래프 전이 폐쇄")
    print("  0→1, 1→2, 2→3, 3→0  (사이클)")
    print("=" * 55)

    edges1 = [(0, 1), (1, 2), (2, 3), (3, 0)]
    n = 4
    labels = ["0", "1", "2", "3"]

    reach_bool = transitive_closure_bool(n, edges1)
    print_reach_matrix(reach_bool, labels)

    reach_bits = transitive_closure_bitset(n, edges1)
    print()
    print("비트마스크 결과 (같은 내용):")
    for i in range(n):
        reachable = [j for j in range(n) if reach_bits[i] >> j & 1]
        print(f"  {i} 에서 도달 가능: {reachable}")

    # ── 예제 2: DAG (사이클 없음) ──
    print()
    print("=" * 55)
    print("예제 2: DAG — 수강 선수 과목 관계")
    print("  수학→물리→화학, 수학→통계→AI, 물리→AI")
    print("=" * 55)

    subjects = ["수학", "물리", "화학", "통계", "AI"]
    edges2 = [(0, 1), (1, 2), (0, 3), (3, 4), (1, 4)]
    reach2 = transitive_closure_bool(5, edges2)
    print_reach_matrix(reach2, ["수학", "물리", "화학", "통계", "AI"])

    print()
    print("'수학'을 알면 수강 가능한 과목:")
    can_take = [subjects[j] for j in range(5) if reach2[0][j] and j != 0]
    print(f"  {can_take}")

    # ── 예제 3: 백준 11403 유형 ──
    print()
    print("=" * 55)
    print("예제 3: 백준 11403 스타일 — 0-indexed 인접 행렬 입력")
    print("=" * 55)
    adj = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    edges3 = [(i, j) for i in range(4) for j in range(4) if adj[i][j]]
    reach3 = transitive_closure_bool(4, edges3)

    print("입력 adj:")
    for row in adj:
        print(f"  {row}")
    print("출력 reach (O=1, X=0):")
    for row in reach3:
        print(f"  {[1 if r else 0 for r in row]}")


if __name__ == "__main__":
    main()
