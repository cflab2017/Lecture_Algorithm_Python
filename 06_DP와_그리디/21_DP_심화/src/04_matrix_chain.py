# 주제: 행렬 체인 곱셈 순서 최적화 (Matrix Chain Multiplication)
# Time: O(n³)   Space: O(n²)


def matrix_chain_order(dims: list[int]) -> tuple[int, list[list[int]]]:
    """행렬 체인 곱셈 최소 연산 수.

    dims[i-1] × dims[i] = i번째 행렬 크기
    예: dims = [30, 35, 15, 5, 10, 20, 25]
        행렬 0: 30×35, 행렬 1: 35×15, ..., 행렬 5: 20×25

    dp[i][j] = 행렬 i~j를 곱하는 최소 곱셈 수
    dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1])
               for k in range(i, j)

    Time:  O(n³)
    Space: O(n²)

    Returns:
        (최소 연산 수, 분할 정보 테이블 s)
    """
    n = len(dims) - 1   # 행렬 수
    INF = float("inf")

    # dp[i][j]: 행렬 i~j 곱하는 최소 비용
    dp = [[0] * n for _ in range(n)]
    # s[i][j]: 최적 분할점
    s = [[0] * n for _ in range(n)]

    # 길이 l = 2, 3, ..., n인 부분 문제 순서대로
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = INF

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dims[i] * dims[k + 1] * dims[j + 1]
                )
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k

    return dp[0][n - 1], s


def reconstruct_order(s: list[list[int]], i: int, j: int) -> str:
    """최적 괄호 표현 복원.

    Time:  O(n)
    Space: O(n) 재귀 스택
    """
    if i == j:
        return f"A{i}"
    k = s[i][j]
    left = reconstruct_order(s, i, k)
    right = reconstruct_order(s, k + 1, j)
    return f"({left} × {right})"


def naive_count_multiplications(
    order: list[int], dims: list[int]
) -> int:
    """주어진 순서로 행렬을 곱할 때 실제 곱셈 수 계산 (검증용).

    order: 행렬 인덱스 순서
    dims: 행렬 차원 리스트
    """
    # 현재 결과 행렬의 행/열
    current_rows = dims[order[0]]
    current_cols = dims[order[0] + 1]
    total = 0

    for idx in order[1:]:
        next_rows = dims[idx]
        next_cols = dims[idx + 1]
        total += current_rows * current_cols * next_cols
        current_cols = next_cols

    return total


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # 교재 예시: dims = [30, 35, 15, 5, 10, 20, 25]
    # 행렬 A0(30×35), A1(35×15), A2(15×5), A3(5×10), A4(10×20), A5(20×25)
    dims = [30, 35, 15, 5, 10, 20, 25]
    n = len(dims) - 1

    print("=== 행렬 정보 ===")
    for i in range(n):
        print(f"  A{i}: {dims[i]} × {dims[i+1]}")

    min_cost, s = matrix_chain_order(dims)
    order_str = reconstruct_order(s, 0, n - 1)

    print(f"\n최소 연산 수: {min_cost:,}")
    print(f"최적 순서: {order_str}")

    print("\n=== dp 테이블 ===")
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = min_cost if (i == 0 and j == n - 1) else 0

    # 재계산
    dp2, s2 = matrix_chain_order(dims)
    print(f"{'':>8}" + "".join(f"{'A'+str(j):>10}" for j in range(n)))
    dp_table = [[0] * n for _ in range(n)]
    INF = float("inf")
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp_table[i][j] = INF
            for k in range(i, j):
                cost = dp_table[i][k] + dp_table[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                if cost < dp_table[i][j]:
                    dp_table[i][j] = cost
    for i in range(n):
        row_str = f"{'A'+str(i):>8}"
        for j in range(n):
            val = dp_table[i][j] if dp_table[i][j] != INF else 0
            row_str += f"{val:>10,}"
        print(row_str)

    print("\n=== 작은 예시 ===")
    small = [10, 30, 5, 60]
    cost, s_small = matrix_chain_order(small)
    print(f"dims={small}")
    print(f"최소 비용: {cost}, 순서: {reconstruct_order(s_small, 0, 2)}")
    print(f"  (A0×A1)×A2: {10*30*60 + 10*5*60}")  # 잘못된 순서 (그냥 참고)
    print(f"  A0×(A1×A2): {30*5*60 + 10*30*60}")
