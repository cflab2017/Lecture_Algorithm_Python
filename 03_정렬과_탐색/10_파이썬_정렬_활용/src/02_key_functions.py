"""
Topic  : key 함수 활용 — lambda, len, itemgetter, 다중 필드
Time   : O(n log n)  Timsort
Space  : O(n)
"""

from operator import itemgetter, attrgetter


# ── lambda 기초 ───────────────────────────────────────────────────────────────

def demo_lambda_key() -> None:
    """lambda를 key로 사용하는 다양한 패턴."""
    print("=== lambda key 활용 ===")

    # 튜플의 특정 인덱스
    coords = [(3, 4), (1, 2), (5, 0), (2, 8)]
    print(f"x좌표 순: {sorted(coords, key=lambda p: p[0])}")
    print(f"y좌표 순: {sorted(coords, key=lambda p: p[1])}")

    # 거리 순 (원점에서)
    print(f"거리 순 : {sorted(coords, key=lambda p: p[0]**2 + p[1]**2)}")

    # 딕셔너리 리스트
    people = [
        {"name": "홍길동", "age": 30},
        {"name": "이순신", "age": 25},
        {"name": "강감찬", "age": 35},
    ]
    print(f"\n나이 순: {sorted(people, key=lambda p: p['age'])}")
    print(f"이름 순: {sorted(people, key=lambda p: p['name'])}")


# ── 내장 함수 key ─────────────────────────────────────────────────────────────

def demo_builtin_key() -> None:
    """내장 함수를 key로 사용."""
    print("\n=== 내장 함수 key ===")

    words = ["python", "is", "awesome", "and", "fast"]
    print(f"길이 순(len)  : {sorted(words, key=len)}")
    print(f"절댓값(abs)   : {sorted([-3, 1, -5, 2, -1], key=abs)}")
    print(f"소문자(lower) : {sorted(['Banana', 'apple', 'Cherry'], key=str.lower)}")

    # str 변환
    mixed_nums = [100, 9, 20, 3, 50]
    print(f"숫자→사전순   : {sorted(mixed_nums, key=str)}")
    print(f"숫자→숫자순   : {sorted(mixed_nums)}")


# ── operator.itemgetter ───────────────────────────────────────────────────────

def demo_itemgetter() -> None:
    """itemgetter: lambda보다 빠르고 간결."""
    print("\n=== operator.itemgetter ===")

    data = [("Alice", 85, "A반"), ("Bob", 92, "B반"),
            ("Charlie", 85, "A반"), ("Dave", 78, "B반")]

    # 단일 인덱스
    print(f"이름 순   : {sorted(data, key=itemgetter(0))}")
    print(f"점수 순   : {sorted(data, key=itemgetter(1))}")

    # 다중 인덱스 — 튜플로 비교
    print(f"반→점수 순: {sorted(data, key=itemgetter(2, 1))}")

    # 딕셔너리 리스트에 사용
    products = [
        {"name": "사과", "price": 1200, "qty": 50},
        {"name": "배", "price": 2500, "qty": 30},
        {"name": "감", "price": 800, "qty": 70},
    ]
    print(f"\n가격 순: {sorted(products, key=itemgetter('price'))}")
    print(f"수량 순: {sorted(products, key=itemgetter('qty'))}")


# ── 복합 key 패턴 ─────────────────────────────────────────────────────────────

def demo_complex_key() -> None:
    """실전에서 자주 쓰는 복합 key 패턴."""
    print("\n=== 복합 key 패턴 ===")

    # 점수 내림차순 + 이름 오름차순 (음수 트릭)
    students = [("홍길동", 85), ("이순신", 92), ("강감찬", 85), ("유관순", 92)]
    result = sorted(students, key=lambda s: (-s[1], s[0]))
    print(f"점수↓ 이름↑: {result}")

    # 문자열 길이 오름차순 + 사전순
    words = ["cat", "at", "dog", "be", "ant"]
    result2 = sorted(words, key=lambda w: (len(w), w))
    print(f"길이↑ 사전순↑: {result2}")

    # 특수 케이스: None 포함 정렬
    data_with_none = [3, None, 1, None, 2]
    result3 = sorted(data_with_none, key=lambda x: (x is None, x or 0))
    print(f"None 마지막 : {result3}")


# ── attrgetter ────────────────────────────────────────────────────────────────

def demo_attrgetter() -> None:
    """attrgetter: 객체 속성 기준 정렬."""
    from dataclasses import dataclass

    @dataclass
    class Point:
        x: int
        y: int
        label: str

        def __repr__(self) -> str:
            return f"({self.x},{self.y},{self.label})"

    points = [Point(3, 4, "C"), Point(1, 2, "A"), Point(3, 1, "B")]

    print("\n=== attrgetter ===")
    print(f"x순          : {sorted(points, key=attrgetter('x'))}")
    print(f"x→y순         : {sorted(points, key=attrgetter('x', 'y'))}")
    print(f"label순       : {sorted(points, key=attrgetter('label'))}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_lambda_key()
    demo_builtin_key()
    demo_itemgetter()
    demo_complex_key()
    demo_attrgetter()
