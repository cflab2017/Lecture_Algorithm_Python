# Topic : Counter -- 빈도 계산, most_common, 산술 연산
# Time  : O(n) -- Counter 생성
# Space : O(k) -- k = 고유 원소 수

from collections import Counter


def demo_counter_creation() -> None:
    """Counter 생성 다양한 방법."""
    print("=" * 50)
    print("Counter 생성")
    print("=" * 50)

    # 문자열
    c1 = Counter("aababcabcd")
    print("문자열:", c1)

    # 리스트
    c2 = Counter([1, 2, 1, 3, 2, 1])
    print("리스트:", c2)

    # 키워드 인수
    c3 = Counter(red=4, blue=2, green=1)
    print("키워드:", c3)

    # dict에서
    c4 = Counter({"a": 3, "b": 1})
    print("dict  :", c4)


def demo_most_common() -> None:
    """most_common -- 상위 K개 원소."""
    print()
    print("=" * 50)
    print("most_common")
    print("=" * 50)

    text = "the quick brown fox jumps over the lazy dog"
    word_cnt = Counter(text.split())
    print("전체:", word_cnt)
    print("상위 3개:", word_cnt.most_common(3))
    print("하위 3개:", word_cnt.most_common()[:-4:-1])  # 역순 슬라이싱

    char_cnt = Counter(text.replace(" ", ""))
    print("\n문자 상위 5개:", char_cnt.most_common(5))


def demo_arithmetic() -> None:
    """Counter 산술 연산."""
    print()
    print("=" * 50)
    print("Counter 산술")
    print("=" * 50)

    c1 = Counter(a=4, b=2, c=0, d=-2)
    c2 = Counter(a=1, b=2, c=3)
    print("c1:", c1)
    print("c2:", c2)

    print("c1 + c2 (합)  :", c1 + c2)   # 양수만
    print("c1 - c2 (차)  :", c1 - c2)   # 양수만
    print("c1 & c2 (min) :", c1 & c2)   # 각 키 최소값
    print("c1 | c2 (max) :", c1 | c2)   # 각 키 최대값

    # subtract -- 음수 포함
    c3 = Counter(a=4, b=2)
    c3.subtract(Counter(a=1, b=5))
    print("subtract 후:", c3)   # a:3, b:-3

    # update -- 더하기
    c4 = Counter(a=1)
    c4.update({"a": 2, "b": 3})
    print("update 후:", c4)


def demo_practical_uses() -> None:
    """Counter 실전 활용 패턴."""
    print()
    print("=" * 50)
    print("실전 활용")
    print("=" * 50)

    # 1. 중복 원소 찾기
    nums = [1, 2, 3, 2, 4, 1, 5, 1]
    cnt = Counter(nums)
    duplicates = [n for n, c in cnt.items() if c > 1]
    print("중복 원소:", sorted(duplicates))

    # 2. 유니크 원소 수
    print("유니크 원소 수:", len(cnt))

    # 3. 전체 합
    print("전체 원소 수:", sum(cnt.values()))

    # 4. 애너그램 확인
    def is_anagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    print("listen/silent 애너그램:", is_anagram("listen", "silent"))

    # 5. 두 리스트 공통 원소 (중복 포함)
    a = [1, 2, 2, 3, 4]
    b = [2, 2, 3, 3, 5]
    intersection = list((Counter(a) & Counter(b)).elements())
    print("공통 원소 (중복 포함):", sorted(intersection))


if __name__ == "__main__":
    demo_counter_creation()
    demo_most_common()
    demo_arithmetic()
    demo_practical_uses()
