# =============================================================================
# 파일명: 03_space_complexity.py
# 설명  : O(1), O(n), O(n²) 공간복잡도를 sys.getsizeof로 측정
# 시간복잡도: O(n²) — 2차원 배열 생성 시
# 공간복잡도: 각 함수별 주석 참고
# =============================================================================

import sys


# ---------------------------------------------------------------------------
# O(1) 공간 — 고정된 수의 변수만 사용
# ---------------------------------------------------------------------------
def sum_o1_space(arr: list) -> int:
    """배열의 합 계산. 공간복잡도: O(1) — 변수 2개만 사용"""
    total = 0       # 변수 1개
    for x in arr:   # 루프 변수 1개 (스택 사용 무시)
        total += x
    return total


# ---------------------------------------------------------------------------
# O(n) 공간 — 입력 크기에 비례하는 추가 공간
# ---------------------------------------------------------------------------
def prefix_sum_on_space(arr: list) -> list:
    """누적 합 배열 반환. 공간복잡도: O(n) — 결과 배열 n개"""
    n = len(arr)
    prefix = [0] * (n + 1)  # n+1개의 추가 공간
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


# ---------------------------------------------------------------------------
# O(n²) 공간 — 2차원 배열 (n × n)
# ---------------------------------------------------------------------------
def create_matrix_on2_space(n: int) -> list:
    """n×n 행렬 생성. 공간복잡도: O(n²)"""
    matrix = [[0] * n for _ in range(n)]  # n*n개의 공간
    for i in range(n):
        matrix[i][i] = 1  # 단위행렬 형태
    return matrix


# ---------------------------------------------------------------------------
# 재귀 호출 스택 공간 — O(n) (호출 깊이만큼)
# ---------------------------------------------------------------------------
def recursive_factorial(n: int) -> int:
    """재귀 팩토리얼. 공간복잡도: O(n) — 호출 스택 깊이 n"""
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)  # 스택 프레임 n개 쌓임


def iterative_factorial(n: int) -> int:
    """반복 팩토리얼. 공간복잡도: O(1) — 추가 공간 없음"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ---------------------------------------------------------------------------
# 메모리 사용량 측정 헬퍼
# ---------------------------------------------------------------------------
def list_total_size(obj: list) -> int:
    """리스트의 총 메모리 사용량을 계산합니다 (헤더 + 모든 원소)."""
    if not isinstance(obj, list):
        return sys.getsizeof(obj)
    total = sys.getsizeof(obj)
    for item in obj:
        total += sys.getsizeof(item)
    return total


def main():
    print("=" * 55)
    print("  공간복잡도 (Space Complexity) 데모")
    print("=" * 55)

    sizes = [10, 100, 1000]

    # -----------------------------------------------------------------------
    # O(1) 공간 측정
    # -----------------------------------------------------------------------
    print("\n[O(1) 공간] 변수 사용량 (입력 크기와 무관)")
    for n in sizes:
        print(f"  n={n:>5}: 추가 변수 2개만 사용 → 상수 공간")

    # -----------------------------------------------------------------------
    # O(n) 공간 측정
    # -----------------------------------------------------------------------
    print("\n[O(n) 공간] 누적 합 배열 크기")
    for n in sizes:
        arr = list(range(n))
        prefix = prefix_sum_on_space(arr)
        total_bytes = list_total_size(prefix)
        print(
            f"  n={n:>5}: prefix 배열 크기 = "
            f"{len(prefix):>5}개, "
            f"총 {total_bytes:>7} bytes "
            f"(≈ {total_bytes/1024:.1f} KB)"
        )

    # -----------------------------------------------------------------------
    # O(n²) 공간 측정
    # -----------------------------------------------------------------------
    print("\n[O(n²) 공간] n×n 행렬 크기")
    for n in [10, 100, 300]:
        matrix = create_matrix_on2_space(n)
        total_bytes = sys.getsizeof(matrix)
        for row in matrix:
            total_bytes += sys.getsizeof(row)
            total_bytes += sum(sys.getsizeof(x) for x in row)
        print(
            f"  n={n:>4}: {n}×{n} 행렬, "
            f"원소 수 = {n*n:>6}개, "
            f"총 {total_bytes:>9} bytes "
            f"(≈ {total_bytes/1024:.1f} KB)"
        )

    # -----------------------------------------------------------------------
    # 재귀 vs 반복 비교
    # -----------------------------------------------------------------------
    print("\n[재귀 vs 반복] 팩토리얼 공간 비교")
    n = 10
    rec = recursive_factorial(n)
    itr = iterative_factorial(n)
    print(f"  재귀 팩토리얼({n}!) = {rec}  → 호출 스택 {n}단계 (O(n) 공간)")
    print(f"  반복 팩토리얼({n}!) = {itr}  → 변수 1개만 사용 (O(1) 공간)")

    # -----------------------------------------------------------------------
    # 파이썬 정수 크기 참고
    # -----------------------------------------------------------------------
    print("\n[참고] 파이썬 객체 크기")
    print(f"  int (작은 값 28):   {sys.getsizeof(28)} bytes")
    print(f"  int (큰 값 10^18):  {sys.getsizeof(10**18)} bytes")
    print(f"  float:              {sys.getsizeof(1.0)} bytes")
    print(f"  빈 list []:         {sys.getsizeof([])} bytes")
    print(f"  list 1000개:        {sys.getsizeof([0]*1000)} bytes (헤더만)")
    print("\n[결론] 파이썬 int는 C의 int(4 bytes)보다 훨씬 큽니다.")
    print("       대용량 데이터 처리 시 메모리 제한에 주의하세요.")


if __name__ == "__main__":
    main()
