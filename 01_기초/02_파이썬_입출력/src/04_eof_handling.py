# =============================================================================
# 파일명: 04_eof_handling.py
# 설명  : EOF(End of File)까지 읽는 다양한 패턴 시연
# 시간복잡도: O(n) — 줄 수에 비례
# 공간복잡도: O(n) — 결과 저장
# =============================================================================
# EOF 문제 유형:
#   - "입력의 끝까지" 라고 나온 경우
#   - 줄 수가 주어지지 않은 경우
#   - 백준 예시: 10951번 A+B-4, 11021번 A+B-7
# =============================================================================

import sys
import io


def pattern_try_except(fake_input: str) -> list:
    """방법 1: readline()이 빈 문자열을 반환하면 EOF.

    readline()은 빈 줄은 '\\n'을 반환하고,
    EOF에서는 '' (빈 문자열)을 반환합니다.
    """
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_input)

    results = []
    try:
        while True:
            line = sys.stdin.readline()
            if not line:        # readline()은 EOF에서 빈 문자열 반환
                break
            line = line.strip()
            if not line:        # 빈 줄 건너뛰기
                continue
            a, b = map(int, line.split())
            results.append(a + b)
    except (EOFError, ValueError):
        pass  # EOF 또는 잘못된 입력 → 조용히 종료

    sys.stdin = original_stdin
    return results


def pattern_for_in_stdin(fake_input: str) -> list:
    """방법 2: for line in sys.stdin 패턴.

    가장 파이써닉한 방법입니다.
    파일 객체를 직접 이터레이트하면 EOF에서 자동으로 종료됩니다.
    """
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_input)

    results = []
    for line in sys.stdin:      # EOF에서 자동 종료
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        results.append(a + b)

    sys.stdin = original_stdin
    return results


def pattern_read_all_split(fake_input: str) -> list:
    """방법 3: sys.stdin.read()로 전체 읽기 후 파싱.

    입력을 한 번에 읽어 메모리에 올린 뒤 파싱합니다.
    반복 시스템 콜이 없어 가장 빠릅니다.
    """
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_input)

    data = sys.stdin.read().split()  # 전체 읽기 후 공백으로 분리
    results = []
    i = 0
    while i + 1 < len(data):
        a = int(data[i])
        b = int(data[i + 1])
        results.append(a + b)
        i += 2

    sys.stdin = original_stdin
    return results


def pattern_readline_empty_check(fake_input: str) -> list:
    """방법 4: readline() 반환값으로 EOF 감지.

    readline()이 '' 반환 → EOF
    readline()이 '\\n' 반환 → 빈 줄 (EOF 아님)
    """
    original_stdin = sys.stdin
    sys.stdin = io.StringIO(fake_input)

    results = []
    while True:
        line = sys.stdin.readline()
        if line == '':           # EOF 감지: 빈 문자열
            break
        line = line.strip()
        if not line:             # 빈 줄 건너뛰기 ('\n'만 있는 경우)
            continue
        try:
            a, b = map(int, line.split())
            results.append(a + b)
        except ValueError:
            continue             # 잘못된 형식 무시

    sys.stdin = original_stdin
    return results


def main():
    print("=" * 55)
    print("  EOF 처리 패턴 시연")
    print("=" * 55)

    # 테스트 입력 (빈 줄 포함)
    test_input = "1 2\n3 4\n\n5 6\n7 8\n"
    expected = [3, 7, 11, 15]  # 각 줄의 a+b

    print(f"\n테스트 입력:")
    for line in test_input.rstrip('\n').split('\n'):
        display = repr(line) if line else "'' (빈 줄)"
        print(f"  {display}")
    print(f"\n기대 결과: {expected}")

    # 각 패턴 시연
    r1 = pattern_try_except(test_input)
    r2 = pattern_for_in_stdin(test_input)
    r3 = pattern_read_all_split(test_input)
    r4 = pattern_readline_empty_check(test_input)

    print(f"\n방법 1 (readline + empty check): {r1}")
    print(f"방법 2 (for in stdin):           {r2}")
    print(f"방법 3 (read all):               {r3}")
    print(f"방법 4 (readline empty check):   {r4}")

    all_correct = (r1 == r2 == r3 == r4 == expected)
    print(f"\n모든 방법 결과 일치: {all_correct}")

    print("\n" + "=" * 55)
    print("  readline() EOF 동작 설명")
    print("=" * 55)
    stream = io.StringIO("line1\nline2\n")
    print(f"  1회: repr={repr(stream.readline())}  <- 일반 줄")
    print(f"  2회: repr={repr(stream.readline())}  <- 일반 줄")
    print(f"  3회: repr={repr(stream.readline())}  <- EOF! 빈 문자열")
    print(f"  4회: repr={repr(stream.readline())}  <- 여전히 빈 문자열")

    print("\n[결론] readline()이 '' 반환 → EOF 신호")
    print("[결론] readline()이 '\\n' 반환 → 빈 줄 (EOF 아님)")


if __name__ == "__main__":
    main()
