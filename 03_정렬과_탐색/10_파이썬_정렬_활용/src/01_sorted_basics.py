"""
Topic  : sorted() vs list.sort() 기초
Time   : O(n log n)  Timsort
Space  : O(n) for sorted(), O(1) extra for .sort()
"""

from dataclasses import dataclass, field


# ── sorted() vs list.sort() ───────────────────────────────────────────────────

def demo_sorted_vs_sort() -> None:
    """두 함수의 핵심 차이 시연."""
    original = [3, 1, 4, 1, 5, 9, 2, 6]

    # sorted() : 새 리스트 반환, 원본 불변
    new_list = sorted(original)
    print(f"sorted() 반환: {new_list}")
    print(f"원본 유지    : {original}")

    # list.sort() : in-place, None 반환
    copy = original[:]
    ret = copy.sort()
    print(f"sort() 반환값: {ret}     ← None!")
    print(f"copy 변경됨  : {copy}")

    # 흔한 실수
    mistake = [3, 1, 2]
    mistake.sort()           # 올바른 사용
    print(f"\n올바른 sort: {mistake}")

    oops = sorted([3, 1, 2])
    print(f"반환값 사용  : {oops}     ← 이렇게 써야 함")


# ── 문자열 정렬 ───────────────────────────────────────────────────────────────

def demo_string_sort() -> None:
    """문자열 정렬 다양한 예시."""
    words = ["banana", "Apple", "cherry", "date", "fig"]

    print("\n=== 문자열 정렬 ===")
    print(f"기본 (사전순, 대소문자 구분): {sorted(words)}")
    print(f"대소문자 무시              : {sorted(words, key=str.lower)}")
    print(f"길이 순                   : {sorted(words, key=len)}")
    print(f"길이 역순                 : {sorted(words, key=len, reverse=True)}")
    print(f"마지막 글자 순            : {sorted(words, key=lambda w: w[-1])}")

    # 숫자 문자열 주의
    num_strs = ["10", "9", "100", "2", "20"]
    print(f"\n숫자 문자열 사전순  : {sorted(num_strs)}")
    print(f"숫자 문자열 숫자순  : {sorted(num_strs, key=int)}")


# ── 숫자 정렬 ─────────────────────────────────────────────────────────────────

def demo_number_sort() -> None:
    """숫자 정렬 다양한 예시."""
    nums = [-5, 3, -1, 4, -9, 2]

    print("\n=== 숫자 정렬 ===")
    print(f"오름차순     : {sorted(nums)}")
    print(f"내림차순     : {sorted(nums, reverse=True)}")
    print(f"절댓값 순    : {sorted(nums, key=abs)}")
    print(f"제곱 순      : {sorted(nums, key=lambda x: x**2)}")


# ── 커스텀 객체 정렬 ──────────────────────────────────────────────────────────

@dataclass
class Student:
    name: str
    score: int
    grade: str

    def __repr__(self) -> str:
        return f"Student({self.name}, {self.score}, {self.grade})"


def demo_object_sort() -> None:
    """객체 정렬."""
    students = [
        Student("홍길동", 85, "A"),
        Student("이순신", 92, "B"),
        Student("강감찬", 85, "A"),
        Student("유관순", 78, "B"),
    ]

    print("\n=== 객체 정렬 ===")
    by_score = sorted(students, key=lambda s: s.score)
    print(f"점수 오름차순: {by_score}")

    by_score_desc = sorted(students, key=lambda s: -s.score)
    print(f"점수 내림차순: {by_score_desc}")

    by_name = sorted(students, key=lambda s: s.name)
    print(f"이름 순      : {by_name}")

    # attrgetter 사용
    from operator import attrgetter
    by_grade_score = sorted(students, key=attrgetter('grade', 'score'))
    print(f"반→점수 순   : {by_grade_score}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_sorted_vs_sort()
    demo_string_sort()
    demo_number_sort()
    demo_object_sort()
