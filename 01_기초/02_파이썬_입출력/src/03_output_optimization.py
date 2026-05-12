# =============================================================================
# 파일명: 03_output_optimization.py
# 설명  : print() vs sys.stdout.write vs 버퍼 모아서 출력 속도 비교
# 시간복잡도: O(n) — n번 출력
# 공간복잡도: O(n) — 버퍼 방법에서 결과를 리스트에 저장
# =============================================================================

import sys
import io
import time
import random


def method_print_loop(numbers: list) -> float:
    """print()를 반복 호출하는 방법. 느리지만 코드가 단순합니다."""
    buf = io.StringIO()
    original = sys.stdout
    sys.stdout = buf

    t0 = time.perf_counter()
    for x in numbers:       # n번 print() 호출
        print(x)
    elapsed = time.perf_counter() - t0

    sys.stdout = original
    return elapsed


def method_stdout_write_loop(numbers: list) -> float:
    """sys.stdout.write()를 반복 호출하는 방법."""
    buf = io.StringIO()
    original = sys.stdout
    sys.stdout = buf

    t0 = time.perf_counter()
    write = sys.stdout.write
    for x in numbers:       # n번 write() 호출
        write(str(x))
        write('\n')
    elapsed = time.perf_counter() - t0

    sys.stdout = original
    return elapsed


def method_join_single_write(numbers: list) -> float:
    """모든 결과를 join()으로 연결 후 1회 출력. 가장 빠른 방법입니다."""
    buf = io.StringIO()
    original = sys.stdout
    sys.stdout = buf

    t0 = time.perf_counter()
    # 리스트 컴프리헨션 + join으로 한 문자열 생성 → 1회 write
    result = '\n'.join(map(str, numbers)) + '\n'
    sys.stdout.write(result)
    elapsed = time.perf_counter() - t0

    sys.stdout = original
    return elapsed


def method_list_append_join(numbers: list) -> float:
    """출력할 내용을 리스트에 모아 마지막에 한 번 출력합니다."""
    buf = io.StringIO()
    original = sys.stdout
    sys.stdout = buf

    t0 = time.perf_counter()
    output = []             # 출력 버퍼 역할
    for x in numbers:
        output.append(str(x))  # 문자열로 변환하여 저장
    sys.stdout.write('\n'.join(output) + '\n')  # 1회 출력
    elapsed = time.perf_counter() - t0

    sys.stdout = original
    return elapsed


def benchmark_output(n: int = 100_000) -> None:
    """네 가지 출력 방법의 속도를 비교합니다."""
    random.seed(42)
    numbers = [random.randint(1, 10 ** 9) for _ in range(n)]

    print(f"\n출력 방법 속도 비교 (n={n:,}개의 정수 출력)")
    print("=" * 55)

    t1 = method_print_loop(numbers)
    t2 = method_stdout_write_loop(numbers)
    t3 = method_join_single_write(numbers)
    t4 = method_list_append_join(numbers)

    baseline = t3 if t3 > 0 else 1e-9
    print(f"print() 반복:          {t1:.4f}초  ({t1/baseline:>5.1f}x)")
    print(f"write() 반복:          {t2:.4f}초  ({t2/baseline:>5.1f}x)")
    print(f"join + 1회 write:      {t3:.4f}초  ({1.0:>5.1f}x, 기준)")
    print(f"list.append + join:    {t4:.4f}초  ({t4/baseline:>5.1f}x)")

    print("\n[결론]")
    print("  print()를 n번 호출하는 것보다 한 번에 출력하는 것이 빠릅니다.")
    print("  '\\n'.join(map(str, results)) 패턴을 권장합니다.")


def show_output_patterns() -> None:
    """실전 출력 패턴을 보여줍니다."""
    print("\n" + "=" * 55)
    print("  출력 패턴 예시")
    print("=" * 55)

    results = [10, 20, 30, 40, 50]

    # 패턴 1: print() 반복 (느림)
    print("\n패턴 1: print() 반복 (N이 작을 때 OK)")
    for x in results:
        print(x)

    # 패턴 2: '\n'.join() 한 번에 출력 (권장)
    print("\n패턴 2: join + 1회 출력 (N이 클 때 권장)")
    print('\n'.join(map(str, results)))

    # 패턴 3: sys.stdout.write 직접 사용
    print("\n패턴 3: sys.stdout.write")
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

    # 패턴 4: f-string 활용 (복잡한 형식)
    print("\n패턴 4: f-string 형식 출력")
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    print('\n'.join(f"Case #{i}: {v}" for i, v in pairs))


def main():
    print("=" * 55)
    print("  출력 최적화 데모")
    print("=" * 55)

    show_output_patterns()
    benchmark_output(n=50_000)


if __name__ == "__main__":
    main()
