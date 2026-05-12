"""
Topic  : 계수 정렬(Counting Sort) & 기수 정렬(Radix Sort) 개념
Time   : Counting O(n+k), Radix O(nk)  (k = 값의 범위 or 자릿수)
Space  : O(k)
"""


# ── 계수 정렬 ─────────────────────────────────────────────────────────────────

def counting_sort(arr: list[int]) -> list[int]:
    """기본 계수 정렬.

    값 범위 k 만큼의 카운트 배열을 이용.
    단, 모든 원소 >= 0 이어야 함.
    """
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1

    result: list[int] = []
    for val, cnt in enumerate(count):
        result.extend([val] * cnt)
    return result


def counting_sort_stable(arr: list[int], max_val: int) -> list[int]:
    """안정(stable) 계수 정렬 — 원소 순서 보존.

    누적합(prefix sum) 기법 사용.
    """
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1

    # 누적합
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    for x in reversed(arr):        # 역순 순회 → stable
        count[x] -= 1
        output[count[x]] = x

    return output


# ── 기수 정렬 (10진수) ────────────────────────────────────────────────────────

def radix_sort(arr: list[int]) -> list[int]:
    """LSD(Least Significant Digit) 기수 정렬.

    각 자릿수에 대해 안정 계수 정렬을 수행.
    Time : O(d·(n+10))  d = 자릿수 수, 10진수이므로 k=10
    """
    if not arr:
        return []
    a = arr[:]
    max_val = max(a)
    exp = 1          # 1, 10, 100, …
    while max_val // exp > 0:
        a = _counting_sort_by_digit(a, exp)
        exp *= 10
    return a


def _counting_sort_by_digit(arr: list[int], exp: int) -> list[int]:
    """exp 번째 자릿수 기준 안정 계수 정렬."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for x in arr:
        digit = (x // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for x in reversed(arr):
        digit = (x // exp) % 10
        count[digit] -= 1
        output[count[digit]] = x

    return output


# ── 시각화 ───────────────────────────────────────────────────────────────────

def visualize_counting(arr: list[int]) -> None:
    """계수 정렬 과정 시각화."""
    print(f"입력 배열  : {arr}")
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    print(f"카운트 배열: {count}  (인덱스 = 값)")

    prefix = count[:]
    for i in range(1, max_val + 1):
        prefix[i] += prefix[i - 1]
    print(f"누적합 배열: {prefix}")

    result = counting_sort_stable(arr, max_val)
    print(f"정렬 결과  : {result}")


def visualize_radix(arr: list[int]) -> None:
    """기수 정렬 자릿수별 정렬 과정."""
    print(f"\n기수 정렬 입력: {arr}")
    a = arr[:]
    max_val = max(a)
    exp = 1
    step = 1
    while max_val // exp > 0:
        a = _counting_sort_by_digit(a, exp)
        print(f"  자릿수 10^{step-1} ({exp:>4}의 자리) 정렬 후: {a}")
        exp *= 10
        step += 1
    print(f"최종 결과 : {a}")


# ── 한계와 활용 ───────────────────────────────────────────────────────────────

def when_to_use() -> None:
    """계수 정렬 적합 조건 안내."""
    print("\n=== 계수 정렬 사용 조건 ===")
    examples = [
        ("성적 정렬 (0~100)", 100, 10_000, "✅ k=100, n=10000 → O(n+k) = O(10100)"),
        ("나이 정렬 (1~120)", 120, 1_000_000, "✅ k=120, n=1M → 매우 효율적"),
        ("주민번호 정렬 (범위 큼)", 999_999_999, 1_000, "❌ k≈10억 → 메모리 초과"),
        ("실수 값 정렬", -1, 1000, "❌ 실수에는 사용 불가"),
    ]
    for desc, k, n, verdict in examples:
        print(f"  {desc:30s}: {verdict}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1, 7]

    print("=" * 50)
    print("계수 정렬 시각화")
    print("=" * 50)
    visualize_counting(arr)

    sorted_basic = counting_sort(arr)
    print(f"\n기본 계수 정렬 결과: {sorted_basic}")

    grades = [88, 74, 96, 88, 74, 100, 60]
    print(f"\n성적 계수 정렬: {grades} → {counting_sort(grades)}")

    # 기수 정렬
    print("\n" + "=" * 50)
    print("기수 정렬 시각화")
    print("=" * 50)
    big_nums = [170, 45, 75, 90, 802, 24, 2, 66]
    visualize_radix(big_nums)

    # 정확성 검증
    import random
    test = [random.randint(0, 500) for _ in range(30)]
    assert counting_sort(test) == sorted(test), "계수 정렬 오류!"
    assert radix_sort(test) == sorted(test), "기수 정렬 오류!"
    print("\n정확성 검증: PASS")

    when_to_use()
