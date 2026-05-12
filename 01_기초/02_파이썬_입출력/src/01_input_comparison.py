# =============================================================================
# 파일명: 01_input_comparison.py
# 설명  : input() vs sys.stdin.readline() 속도 비교 (io.StringIO 사용)
# 시간복잡도: O(n) — n개의 줄을 읽음
# 공간복잡도: O(n) — 읽은 데이터 저장
# =============================================================================
# 참고: 실제 stdin을 사용하는 대신, io.StringIO로 가상 입력 스트림을 생성하여
#       두 방법의 내부 파싱 속도를 비교합니다.
# =============================================================================

import sys
import io
import time
import random


def simulate_input_builtin(lines: list) -> list:
    """input()처럼 한 줄씩 읽어 정수로 변환합니다.

    실제 input()은 시스템 콜 + 프롬프트 처리 등 추가 오버헤드가 있지만,
    여기서는 readline()과의 순수 파싱 속도 차이를 측정합니다.
    """
    result = []
    for line in lines:          # 미리 준비된 줄 목록
        result.append(int(line.strip()))  # input()의 동작 모사
    return result


def simulate_readline(stream: io.StringIO, n: int) -> list:
    """sys.stdin.readline()처럼 스트림에서 한 줄씩 읽습니다."""
    result = []
    for _ in range(n):
        result.append(int(stream.readline()))  # \n은 int() 변환시 무시
    return result


def simulate_read_all(stream: io.StringIO) -> list:
    """sys.stdin.read().split()으로 한 번에 읽습니다."""
    return list(map(int, stream.read().split()))


def benchmark_io(n: int = 100_000) -> None:
    """n개의 정수 입력을 세 가지 방법으로 읽는 속도를 비교합니다."""
    print(f"\n입력 방법 속도 비교 (n={n:,}개의 정수)")
    print("=" * 55)

    # 테스트 데이터 생성
    random.seed(42)
    numbers = [random.randint(1, 10 ** 9) for _ in range(n)]
    text = '\n'.join(map(str, numbers)) + '\n'
    lines = [str(x) for x in numbers]  # 미리 문자열로 변환

    # -----------------------------------------------------------------------
    # 방법 1: input() 모사 (list of strings에서 파싱)
    # -----------------------------------------------------------------------
    t0 = time.perf_counter()
    result1 = simulate_input_builtin(lines)
    t_input = time.perf_counter() - t0
    print(f"input() 모사            : {t_input:.4f}초")

    # -----------------------------------------------------------------------
    # 방법 2: sys.stdin.readline() 모사
    # -----------------------------------------------------------------------
    stream2 = io.StringIO(text)
    t0 = time.perf_counter()
    result2 = simulate_readline(stream2, n)
    t_readline = time.perf_counter() - t0
    print(f"sys.stdin.readline() 모사: {t_readline:.4f}초")

    # -----------------------------------------------------------------------
    # 방법 3: sys.stdin.read().split() 모사
    # -----------------------------------------------------------------------
    stream3 = io.StringIO(text)
    t0 = time.perf_counter()
    result3 = simulate_read_all(stream3)
    t_read = time.perf_counter() - t0
    print(f"sys.stdin.read().split(): {t_read:.4f}초")

    # -----------------------------------------------------------------------
    # 결과 검증
    # -----------------------------------------------------------------------
    assert result1 == result2 == result3, "결과가 다릅니다!"
    print("\n결과 일치: OK")

    # -----------------------------------------------------------------------
    # 속도 비교 요약
    # -----------------------------------------------------------------------
    baseline = t_read  # read().split()을 기준으로
    if baseline > 0:
        print("\n속도 비교 (read().split() 대비)")
        print(f"  input() 모사:          {t_input/baseline:>6.1f}배 느림")
        print(f"  readline() 모사:       {t_readline/baseline:>6.1f}배 느림")
        print(f"  read().split():        {1.0:>6.1f}배 (기준)")

    print("\n[결론]")
    print("  - 입력 개수가 많을수록 sys.stdin.read()가 유리합니다.")
    print("  - 경쟁 프로그래밍에서 N > 10,000이면 sys.stdin을 사용하세요.")


def show_usage_patterns() -> None:
    """올바른 입력 패턴을 출력합니다."""
    print("\n" + "=" * 55)
    print("  실전 입력 패턴 예시")
    print("=" * 55)

    patterns = [
        ("정수 하나",
         "n = int(sys.stdin.readline())"),
        ("공백 구분 두 정수",
         "a, b = map(int, sys.stdin.readline().split())"),
        ("정수 리스트",
         "arr = list(map(int, sys.stdin.readline().split()))"),
        ("input 덮어쓰기",
         "input = sys.stdin.readline\nn = int(input())"),
        ("전체 읽기",
         "data = sys.stdin.read().split()\nn = int(data[0])"),
    ]

    for name, code in patterns:
        print(f"\n# {name}")
        for line in code.split('\n'):
            print(f"  {line}")


def main():
    print("=" * 55)
    print("  파이썬 I/O 속도 비교 데모")
    print("=" * 55)

    # readline()에서 \n 처리 시연
    print("\n[readline()의 \\n 처리]")
    stream = io.StringIO("hello\nworld\n")
    raw = stream.readline()
    print(f"  readline() 결과: repr={repr(raw)}")
    print(f"  .strip() 적용:   {repr(raw.strip())}")
    print(f"  int() 변환:      {int('42\n')} (\\n 자동 무시)")

    # 벤치마크 실행
    benchmark_io(n=100_000)
    show_usage_patterns()


if __name__ == "__main__":
    main()
