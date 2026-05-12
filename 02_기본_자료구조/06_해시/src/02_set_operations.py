# Topic : set 집합 연산, frozenset, 멤버십 테스트
# Time  : O(1) 평균 -- add/remove/in
# Space : O(n) -- 원소 수


def demo_set_basics() -> None:
    """set 기본 연산."""
    print("=" * 50)
    print("set 기본 연산")
    print("=" * 50)

    s: set[int] = set()

    # 추가
    for v in [3, 1, 4, 1, 5, 9, 2, 6, 5]:
        s.add(v)
    print("add 후 (중복 제거):", sorted(s))

    # 멤버십 -- O(1)
    print("5 in s:", 5 in s)
    print("7 in s:", 7 in s)

    # 제거
    s.remove(1)           # 없으면 KeyError
    s.discard(100)        # 없어도 OK
    print("remove(1), discard(100) 후:", sorted(s))

    # pop -- 임의 원소 제거
    val = s.pop()
    print(f"pop() = {val}, 남은: {sorted(s)}")


def demo_set_operations() -> None:
    """집합 연산 -- 합/교/차/대칭차."""
    print()
    print("=" * 50)
    print("집합 연산")
    print("=" * 50)

    A = {1, 2, 3, 4, 5}
    B = {3, 4, 5, 6, 7}
    print("A:", sorted(A))
    print("B:", sorted(B))

    print("A | B (합집합)  :", sorted(A | B))
    print("A & B (교집합)  :", sorted(A & B))
    print("A - B (차집합)  :", sorted(A - B))
    print("B - A (차집합)  :", sorted(B - A))
    print("A ^ B (대칭차)  :", sorted(A ^ B))

    # 부분집합 / 상위집합
    C = {1, 2, 3}
    print()
    print(f"{sorted(C)} <= {sorted(A)}: {C <= A}  (issubset)")
    print(f"{sorted(A)} >= {sorted(C)}: {A >= C}  (issuperset)")
    print(f"A.isdisjoint(B): {A.isdisjoint(B)}")  # 서로소 여부

    D = {10, 20}
    print(f"A.isdisjoint(D={sorted(D)}): {A.isdisjoint(D)}")  # True


def demo_frozenset() -> None:
    """frozenset -- 불변 집합, dict 키로 사용 가능."""
    print()
    print("=" * 50)
    print("frozenset")
    print("=" * 50)

    fs = frozenset([1, 2, 3, 2, 1])
    print("frozenset:", fs)
    print("1 in fs:", 1 in fs)

    # frozenset을 dict 키로 사용
    d: dict[frozenset[int], str] = {}
    d[frozenset([1, 2])] = "pair"
    d[frozenset([3, 4, 5])] = "triple"
    print("frozenset 키 dict:", d)

    # 집합 연산도 지원
    fa = frozenset([1, 2, 3])
    fb = frozenset([2, 3, 4])
    print("fa & fb:", fa & fb)


def demo_performance() -> None:
    """set vs list 멤버십 성능 비교."""
    import time
    print()
    print("=" * 50)
    print("멤버십 성능: set vs list")
    print("=" * 50)

    n = 500_000
    data = list(range(n))
    target = n - 1  # 최악 케이스

    # list -- O(n)
    t0 = time.perf_counter()
    _ = target in data
    list_time = time.perf_counter() - t0

    # set -- O(1)
    data_set = set(data)
    t0 = time.perf_counter()
    _ = target in data_set
    set_time = time.perf_counter() - t0

    print(f"list (O(n)): {list_time:.6f}s")
    print(f"set  (O(1)): {set_time:.6f}s")
    if set_time > 0 and set_time < list_time:
        print(f"set가 약 {list_time / set_time:.0f}배 빠릅니다!")


if __name__ == "__main__":
    demo_set_basics()
    demo_set_operations()
    demo_frozenset()
    demo_performance()
