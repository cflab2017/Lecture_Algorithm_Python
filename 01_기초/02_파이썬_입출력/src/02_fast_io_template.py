# =============================================================================
# 파일명: 02_fast_io_template.py
# 설명  : 경쟁 프로그래밍에서 자주 쓰는 빠른 I/O 패턴 모음
# 시간복잡도: 패턴마다 O(n)
# 공간복잡도: O(n) — 입력 데이터 크기에 비례
# =============================================================================
# 사용법:
#   이 파일은 직접 실행하거나, 백준 코드 작성 시 참고 템플릿으로 사용합니다.
#   실제 stdin 대신 io.StringIO로 가상 입력을 만들어 시연합니다.
# =============================================================================

import sys
import io


# ===========================================================================
# 패턴 1: input()을 sys.stdin.readline으로 교체
# 가장 흔히 사용하는 패턴 — 기존 input() 코드 최소 변경
# ===========================================================================
def pattern1_override_input(fake_stdin: str) -> None:
    """input = sys.stdin.readline 패턴 시연."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_stdin)

    # 실제 백준 코드 시작 지점 -------------------------------------------------
    input = sys.stdin.readline  # input()을 readline으로 교체

    n = int(input())                         # 정수 하나
    a, b = map(int, input().split())         # 공백 구분 두 정수
    arr = list(map(int, input().split()))    # 정수 리스트
    s = input().strip()                      # 문자열 (strip 필수!)
    # -------------------------------------------------------------------------

    print(f"[패턴 1] n={n}, a={a}, b={b}, arr={arr}, s='{s}'")
    sys.stdin = original_stdin


# ===========================================================================
# 패턴 2: sys.stdin.read()로 전체 읽기 후 파싱
# 대용량 입력에서 가장 빠른 방법
# ===========================================================================
def pattern2_read_all(fake_stdin: str) -> None:
    """sys.stdin.read().split() 패턴 시연."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_stdin)

    # 실제 백준 코드 시작 지점 -------------------------------------------------
    data = sys.stdin.read().split()  # 모든 토큰을 리스트로
    idx = 0

    n = int(data[idx]); idx += 1
    arr = [int(data[idx + i]) for i in range(n)]
    idx += n
    # -------------------------------------------------------------------------

    print(f"[패턴 2] n={n}, arr={arr}")
    sys.stdin = original_stdin


# ===========================================================================
# 패턴 3: 여러 줄 입력 — 리스트 컴프리헨션
# ===========================================================================
def pattern3_multiline(fake_stdin: str, n: int) -> None:
    """여러 줄 입력을 리스트로 받는 패턴 시연."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_stdin)
    input_fn = sys.stdin.readline

    # n줄의 [행, 열] 쌍 읽기
    edges = [tuple(map(int, input_fn().split())) for _ in range(n)]
    print(f"[패턴 3] edges={edges}")
    sys.stdin = original_stdin


# ===========================================================================
# 패턴 4: EOF까지 읽기
# ===========================================================================
def pattern4_eof(fake_stdin: str) -> None:
    """EOF까지 입력을 읽는 패턴 시연."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_stdin)

    results = []
    # for line in sys.stdin — EOF에서 자동 종료
    for line in sys.stdin:
        line = line.strip()
        if not line:          # 빈 줄 무시
            continue
        a, b = map(int, line.split())
        results.append(a + b)

    print(f"[패턴 4] 결과: {results}")
    sys.stdin = original_stdin


# ===========================================================================
# 패턴 5: 2차원 배열 입력 (그래프, 행렬)
# ===========================================================================
def pattern5_2d_array(fake_stdin: str, rows: int) -> None:
    """2차원 배열을 빠르게 입력받는 패턴 시연."""
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_stdin)
    input_fn = sys.stdin.readline

    # 중첩 리스트 컴프리헨션으로 한 번에 읽기
    grid = [list(map(int, input_fn().split())) for _ in range(rows)]
    print(f"[패턴 5] grid=")
    for row in grid:
        print(f"  {row}")
    sys.stdin = original_stdin


def main():
    print("=" * 55)
    print("  빠른 I/O 패턴 모음 시연")
    print("=" * 55)

    # 패턴 1 시연
    pattern1_override_input("5\n3 7\n1 2 3 4 5\nhello\n")

    # 패턴 2 시연
    pattern2_read_all("4\n10 20 30 40\n")

    # 패턴 3 시연
    pattern3_multiline("1 2\n3 4\n5 6\n", n=3)

    # 패턴 4 시연 (EOF 처리)
    pattern4_eof("1 2\n3 4\n5 6\n7 8\n")

    # 패턴 5 시연 (2차원 배열)
    pattern5_2d_array("1 2 3\n4 5 6\n7 8 9\n", rows=3)

    print("\n" + "=" * 55)
    print("  백준 코드 기본 템플릿")
    print("=" * 55)
    template = """
import sys
input = sys.stdin.readline  # 빠른 입력

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # ... 풀이 코드 ...
    print("정답")

if __name__ == "__main__":
    solve()
"""
    print(template)


if __name__ == "__main__":
    main()
