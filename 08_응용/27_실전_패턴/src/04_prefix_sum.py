"""
단원 27 — 실전 패턴: 구간 합 (Prefix Sum)
Topic : 1D and 2D Prefix Sum with O(1) Range Query
Time  : O(n) 전처리, O(1) 쿼리
Space : O(n) or O(nm)

설명:
    1. 1D 구간 합: prefix[i+1] = prefix[i] + arr[i]
       query(l, r) = prefix[r+1] - prefix[l]
    2. 2D 구간 합: 포함-배제 원리
       ps[i][j] = arr + ps_위 + ps_왼 - ps_대각위왼
       query(r1,c1,r2,c2) = ps[r2+1][c2+1] - ps[r1][c2+1]
                            - ps[r2+1][c1] + ps[r1][c1]
    3. 차분 배열(Difference Array): 구간 일괄 업데이트 O(1)
"""


# ──────────────────────────────────────────────
# 1. 1D 구간 합
# ──────────────────────────────────────────────

class PrefixSum1D:
    """
    1D 배열의 구간 합 쿼리.

    Time : O(n) 초기화, O(1) 쿼리
    Space: O(n)
    """

    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + arr[i]

    def query(self, l: int, r: int) -> int:
        """
        [l, r] 구간 합 반환 (0-indexed, 양끝 포함).

        Time : O(1)
        """
        return self.prefix[r + 1] - self.prefix[l]

    def range_count_ge(self, l: int, r: int, threshold: int) -> int:
        """[l, r] 에서 threshold 이상 원소 수 (누적 빈도가 아닌 합 기반 응용)."""
        # 단순 합 응용 예시 — 실제로는 정렬 + 이진 탐색 필요
        raise NotImplementedError


# ──────────────────────────────────────────────
# 2. 2D 구간 합
# ──────────────────────────────────────────────

class PrefixSum2D:
    """
    2D 행렬의 직사각형 구간 합 쿼리.

    Time : O(nm) 초기화, O(1) 쿼리
    Space: O(nm)
    """

    def __init__(self, grid: list[list[int]]) -> None:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        self.n = n
        self.m = m
        # ps[i][j] = (0,0)~(i-1,j-1) 직사각형 합 (1-indexed)
        self.ps = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.ps[i][j] = (
                    grid[i - 1][j - 1]
                    + self.ps[i - 1][j]
                    + self.ps[i][j - 1]
                    - self.ps[i - 1][j - 1]
                )

    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        (r1,c1) ~ (r2,c2) 직사각형 구간 합 (0-indexed, 양끝 포함).

        포함-배제 원리:
            전체 - 위쪽 제거 - 왼쪽 제거 + 대각 복원

        Time : O(1)
        """
        return (
            self.ps[r2 + 1][c2 + 1]
            - self.ps[r1][c2 + 1]
            - self.ps[r2 + 1][c1]
            + self.ps[r1][c1]
        )


# ──────────────────────────────────────────────
# 3. 차분 배열 (Difference Array)
# ──────────────────────────────────────────────

class DifferenceArray:
    """
    구간 일괄 업데이트 O(1), 최종 배열 복원 O(n).

    활용: [l, r] 구간에 val을 더하는 업데이트가 많을 때.

    Time : O(1) update, O(n) build
    Space: O(n)
    """

    def __init__(self, n: int) -> None:
        self.diff = [0] * (n + 1)
        self.n = n

    def update(self, l: int, r: int, val: int) -> None:
        """[l, r] 구간에 val 추가 (0-indexed). Time O(1)."""
        self.diff[l] += val
        if r + 1 <= self.n:
            self.diff[r + 1] -= val

    def build(self) -> list[int]:
        """최종 배열 반환. Time O(n)."""
        result = [0] * self.n
        cur = 0
        for i in range(self.n):
            cur += self.diff[i]
            result[i] = cur
        return result


def main() -> None:
    # ── 1. 1D 구간 합 ──
    print("=" * 55)
    print("1. 1D 구간 합")
    print("=" * 55)
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    ps1 = PrefixSum1D(arr)
    print(f"  배열: {arr}")
    print(f"  prefix: {ps1.prefix}")
    queries = [(0, 3), (2, 5), (0, 7), (3, 3)]
    for l, r in queries:
        ans = ps1.query(l, r)
        brute = sum(arr[l:r+1])
        print(f"  query({l},{r}) = {ans}  (직접 합: {brute})")

    # ── 2. 2D 구간 합 ──
    print()
    print("=" * 55)
    print("2. 2D 구간 합")
    print("=" * 55)
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    ps2 = PrefixSum2D(grid)
    print("  행렬:")
    for row in grid:
        print(f"    {row}")
    print()

    q2d = [
        (0, 0, 1, 1),   # 1+2+5+6=14
        (1, 1, 2, 2),   # 6+7+10+11=34
        (0, 0, 2, 3),   # 전체 합=78
    ]
    for r1, c1, r2, c2 in q2d:
        ans = ps2.query(r1, c1, r2, c2)
        brute = sum(grid[r][c] for r in range(r1, r2+1)
                    for c in range(c1, c2+1))
        print(f"  query({r1},{c1},{r2},{c2}) = {ans}  (직접: {brute})")

    # ── 3. 차분 배열 ──
    print()
    print("=" * 55)
    print("3. 차분 배열 — 구간 업데이트")
    print("=" * 55)
    n = 8
    da = DifferenceArray(n)
    updates = [(1, 3, 10), (2, 5, 20), (4, 7, -5)]
    print("  초기: [0] * 8")
    for l, r, v in updates:
        da.update(l, r, v)
        print(f"  update({l},{r},{v:+})")
    result = da.build()
    print(f"  최종: {result}")
    print("  직접 확인:")
    manual = [0] * n
    for l, r, v in updates:
        for i in range(l, r + 1):
            manual[i] += v
    print(f"  기댓값: {manual}")
    print(f"  일치: {result == manual}")

    # ── 복잡도 요약 ──
    print()
    print("=" * 55)
    print("구간 합 복잡도 요약")
    print("=" * 55)
    print("  1D 전처리: O(n),   쿼리: O(1)")
    print("  2D 전처리: O(nm),  쿼리: O(1)")
    print("  차분 배열: O(1) 업데이트, O(n) 복원")
    print("  세그먼트트리: O(n) 전처리, O(log n) 업데이트+쿼리")


if __name__ == "__main__":
    main()
