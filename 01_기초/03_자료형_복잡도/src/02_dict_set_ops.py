# =============================================================================
# 파일명: 02_dict_set_ops.py
# 설명  : dict/set 연산 시간복잡도 실측 및 Counter 활용 예제
# 시간복잡도: dict/set 조회 O(1) 평균, list 탐색 O(n)
# 공간복잡도: O(n) — 저장되는 원소 수에 비례
# =============================================================================

import timeit
import time
import random
from collections import Counter, defaultdict


# ---------------------------------------------------------------------------
# set vs list 멤버십 검사 비교
# ---------------------------------------------------------------------------
def benchmark_membership(n: int = 100_000) -> None:
    """set과 list의 멤버십 검사 속도를 비교합니다."""
    print(f"\n[set vs list 멤버십 검사] n={n:,}")
    print("-" * 55)

    random.seed(42)
    data = random.sample(range(n * 2), n)  # n개의 고유한 정수

    # list 멤버십 — O(n)
    repeat = 1_000
    t_list = timeit.timeit(
        stmt=f'{n - 1} in lst',
        setup=f'lst = {data}',
        number=repeat
    )

    # set 멤버십 — O(1) 평균
    t_set = timeit.timeit(
        stmt=f'{n - 1} in s',
        setup=f's = set({data})',
        number=repeat
    )

    ratio = t_list / t_set if t_set > 0 else float('inf')
    print(f"  list ({repeat}회): {t_list:.6f}초  O(n)")
    print(f"  set  ({repeat}회): {t_set:.6f}초  O(1) 평균")
    print(f"  set이 {ratio:.1f}배 빠름")

    # 크기별 list vs set 차이
    print(f"\n  크기별 멤버십 검사 시간 (100회, 최악의 경우):")
    print(f"  {'크기':>10}  {'list(초)':>12}  {'set(초)':>12}  {'배율':>8}")
    for size in [1_000, 10_000, 100_000]:
        sample = list(range(size))
        target = size - 1  # 최악의 경우: 마지막 원소

        t_l = timeit.timeit(
            stmt=f'{target} in lst',
            setup=f'lst = list(range({size}))',
            number=100
        )
        t_s = timeit.timeit(
            stmt=f'{target} in s',
            setup=f's = set(range({size}))',
            number=100
        )
        r = t_l / t_s if t_s > 0 else float('inf')
        print(f"  {size:>10,}  {t_l:>12.6f}  {t_s:>12.6f}  {r:>8.1f}x")


# ---------------------------------------------------------------------------
# dict 기본 연산 데모
# ---------------------------------------------------------------------------
def demo_dict_operations() -> None:
    """dict의 주요 연산을 시연합니다."""
    print("\n[dict 기본 연산 데모]")
    print("-" * 55)

    # 삽입 — O(1) 평균
    d = {}
    d['apple'] = 3
    d['banana'] = 1
    d['cherry'] = 5
    print(f"  삽입 후 dict: {d}")

    # 조회 — O(1) 평균
    print(f"  d['apple'] = {d['apple']}")

    # 안전한 조회 — get() 사용 (KeyError 방지)
    print(f"  d.get('grape', 0) = {d.get('grape', 0)}")  # 기본값 0

    # 키 존재 확인 — O(1) 평균
    print(f"  'banana' in d: {'banana' in d}")
    print(f"  'grape' in d:  {'grape' in d}")

    # 삭제 — O(1) 평균
    del d['banana']
    print(f"  del d['banana'] 후: {d}")

    # defaultdict — 기본값 자동 생성
    word_count = defaultdict(int)
    text = "apple banana apple cherry banana apple"
    for word in text.split():
        word_count[word] += 1  # 첫 등장 시 KeyError 없음
    print(f"\n  defaultdict(int) 빈도 세기:")
    for word, count in sorted(word_count.items()):
        print(f"    {word}: {count}")


# ---------------------------------------------------------------------------
# Counter 활용 예제
# ---------------------------------------------------------------------------
def demo_counter() -> None:
    """collections.Counter의 활용 예제를 보여줍니다."""
    print("\n[Counter 활용 예제]")
    print("-" * 55)

    # 기본 사용
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    cnt = Counter(words)
    print(f"  Counter(words) = {cnt}")

    # 가장 많이 등장한 원소
    print(f"  most_common(2) = {cnt.most_common(2)}")

    # 정수 리스트에서 빈도 세기
    nums = [1, 2, 3, 2, 1, 3, 3, 4, 4, 4, 4]
    num_cnt = Counter(nums)
    print(f"\n  Counter([1,2,3,2,1,3,3,4,4,4,4]) = {num_cnt}")
    print(f"  4의 등장 횟수: {num_cnt[4]}")

    # Counter 연산
    c1 = Counter({'a': 3, 'b': 2, 'c': 1})
    c2 = Counter({'a': 1, 'b': 2, 'd': 3})
    print(f"\n  c1 + c2 = {c1 + c2}")  # 합산
    print(f"  c1 - c2 = {c1 - c2}")  # 차이 (양수만)
    print(f"  c1 & c2 = {c1 & c2}")  # 최솟값
    print(f"  c1 | c2 = {c1 | c2}")  # 최댓값

    # 문자열 애너그램 검사
    def is_anagram(s1: str, s2: str) -> bool:
        """두 문자열이 애너그램인지 확인합니다. O(n)"""
        return Counter(s1) == Counter(s2)

    print(f"\n  is_anagram('listen', 'silent') = {is_anagram('listen', 'silent')}")
    print(f"  is_anagram('hello', 'world')   = {is_anagram('hello', 'world')}")


def main():
    print("=" * 55)
    print("  dict / set 연산 시간복잡도 데모")
    print("=" * 55)

    benchmark_membership(n=100_000)
    demo_dict_operations()
    demo_counter()

    print("\n" + "=" * 55)
    print("  핵심 정리")
    print("=" * 55)
    print("  x in list  : O(n)   ← 피해야 함 (반복 탐색 시)")
    print("  x in set   : O(1)   ← 멤버십 검사에 사용")
    print("  d[k]       : O(1)   ← 키-값 매핑")
    print("  Counter    : O(n)   ← 빈도 세기에 최적")


if __name__ == "__main__":
    main()
