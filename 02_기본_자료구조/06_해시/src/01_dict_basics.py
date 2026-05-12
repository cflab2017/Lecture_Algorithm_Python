# Topic : dict CRUD, get() 기본값, 순회 패턴
# Time  : O(1) 평균 -- 삽입/삭제/조회
# Space : O(n) -- 저장된 키-값 쌍 수


def demo_crud() -> None:
    """dict 기본 CRUD 연산."""
    print("=" * 50)
    print("dict CRUD")
    print("=" * 50)

    # 생성
    d: dict[str, int] = {}
    d["apple"] = 3
    d["banana"] = 5
    d["cherry"] = 2
    print("생성 후:", d)

    # 조회 -- 없는 키 접근 시 KeyError
    print("d['apple']:", d["apple"])
    try:
        _ = d["grape"]
    except KeyError as e:
        print(f"KeyError 발생: {e}")

    # 안전한 조회 -- get()
    print("d.get('grape', 0) :", d.get("grape", 0))   # 기본값 0
    print("d.get('apple', 0) :", d.get("apple", 0))   # 3

    # 수정
    d["apple"] = 10
    print("수정 후:", d)

    # 삭제
    del d["cherry"]
    print("삭제 후:", d)

    removed = d.pop("banana", -1)
    print(f"pop('banana') = {removed}, 남은 dict: {d}")


def demo_iteration() -> None:
    """dict 순회 패턴."""
    print()
    print("=" * 50)
    print("dict 순회")
    print("=" * 50)

    scores = {"Alice": 95, "Bob": 87, "Carol": 92, "David": 78}

    # 키만
    print("keys()  :", list(scores.keys()))

    # 값만
    print("values():", list(scores.values()))

    # 키-값 쌍
    print("items():")
    for name, score in scores.items():
        print(f"  {name}: {score}")

    # 정렬된 순회
    print("점수 내림차순:")
    for name, score in sorted(scores.items(), key=lambda x: -x[1]):
        print(f"  {name}: {score}")


def demo_advanced_patterns() -> None:
    """고급 dict 패턴."""
    print()
    print("=" * 50)
    print("고급 패턴")
    print("=" * 50)

    # setdefault -- 키 없을 때만 설정
    d: dict[str, list[int]] = {}
    for num in [1, 2, 1, 3, 2, 1]:
        key = "odd" if num % 2 else "even"
        d.setdefault(key, []).append(num)
    print("setdefault 그룹화:", d)

    # dict comprehension
    squares = {x: x ** 2 for x in range(1, 6)}
    print("squares:", squares)

    # 필터링
    large = {k: v for k, v in squares.items() if v > 9}
    print("v > 9 필터:", large)

    # 병합 (Python 3.9+)
    a = {"x": 1, "y": 2}
    b = {"y": 20, "z": 3}
    merged = a | b   # b가 우선
    print("a | b:", merged)

    # 빈도 계산
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    freq: dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    print("빈도:", freq)
    print("최빈값:", max(freq, key=freq.get))  # type: ignore[arg-type]


if __name__ == "__main__":
    demo_crud()
    demo_iteration()
    demo_advanced_patterns()
