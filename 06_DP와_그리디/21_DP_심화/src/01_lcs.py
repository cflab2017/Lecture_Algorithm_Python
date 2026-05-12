# 주제: LCS (Longest Common Subsequence) — dp 테이블 + 수열 복원
# Time: O(n × m)   Space: O(n × m) → O(m) 최적화 가능

def lcs_length(a: str, b: str) -> int:
    """LCS 길이만 반환.

    Time:  O(n × m)
    Space: O(n × m)
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def lcs_reconstruct(a: str, b: str) -> str:
    """LCS 수열 복원 (역추적).

    Time:  O(n × m) dp + O(n + m) 역추적
    Space: O(n × m)
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 역추적: (n, m)에서 (0, 0)으로
    result: list[str] = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))


def lcs_space_optimized(a: str, b: str) -> int:
    """공간 최적화 LCS (롤링 배열 — 길이만).

    Time:  O(n × m)
    Space: O(m) — 현재 행과 이전 행만 유지
    """
    n, m = len(a), len(b)
    prev = [0] * (m + 1)

    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr

    return prev[m]


def print_dp_table(a: str, b: str) -> None:
    """LCS dp 테이블 시각화."""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    header = f"{'':>4}" + "".join(f"{'':>3}{ch}" for ch in " " + b)
    print(header)
    for i, row in enumerate(dp):
        label = " " if i == 0 else a[i - 1]
        print(f"{label:>4}" + "".join(f"{v:>4}" for v in row))


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== LCS 테이블 시각화 ===")
    a, b = "ABCBDAB", "BDCAB"
    print(f"A = {a}")
    print(f"B = {b}")
    print()
    print_dp_table(a, b)

    print(f"\nLCS 길이: {lcs_length(a, b)}")
    print(f"LCS 수열: '{lcs_reconstruct(a, b)}'")
    print(f"공간O(m): {lcs_space_optimized(a, b)}")

    print("\n=== 추가 테스트 ===")
    test_cases = [
        ("AGGTAB", "GXTXAYB"),
        ("ABCDEF", "ABCDEF"),
        ("ABC", "DEF"),
        ("", "ABC"),
        ("A", "A"),
    ]
    for s1, s2 in test_cases:
        length = lcs_length(s1, s2)
        seq = lcs_reconstruct(s1, s2)
        print(f"  LCS('{s1}', '{s2}') = {length}, 수열='{seq}'")

    print("\n=== LCS 활용: diff (문자 삽입/삭제) ===")
    def diff_count(s1: str, s2: str) -> tuple[int, int]:
        """편집 거리를 LCS로 계산 (삽입+삭제만)."""
        lcs = lcs_length(s1, s2)
        deletions = len(s1) - lcs
        insertions = len(s2) - lcs
        return deletions, insertions

    pairs = [("kitten", "sitting"), ("sunday", "saturday")]
    for s1, s2 in pairs:
        d, i = diff_count(s1, s2)
        print(f"  '{s1}' → '{s2}': 삭제={d}, 삽입={i}")
