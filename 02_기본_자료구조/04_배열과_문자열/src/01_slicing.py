# Topic : 슬라이싱 기초 및 2D 배열 슬라이싱
# Time  : O(k) -- 슬라이싱 길이 k에 비례
# Space : O(k) -- 슬라이싱 결과 복사본 크기


def demonstrate_1d_slicing() -> None:
    """1차원 리스트 슬라이싱 예제."""
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("=" * 45)
    print("원본 배열:", arr)
    print("=" * 45)

    # 기본 슬라이싱
    print("arr[2:6]   :", arr[2:6])     # [2, 3, 4, 5]
    print("arr[:4]    :", arr[:4])      # [0, 1, 2, 3]
    print("arr[6:]    :", arr[6:])      # [6, 7, 8, 9]
    print("arr[:]     :", arr[:])       # 전체 복사

    # 음수 인덱스
    print()
    print("arr[-1]    :", arr[-1])      # 9 (마지막)
    print("arr[-3:]   :", arr[-3:])     # [7, 8, 9]
    print("arr[:-3]   :", arr[:-3])     # [0..6]

    # step 슬라이싱
    print()
    print("arr[::2]   :", arr[::2])     # 짝수 인덱스
    print("arr[1::2]  :", arr[1::2])    # 홀수 인덱스
    print("arr[::-1]  :", arr[::-1])    # 역순 복사
    print("arr[8:1:-2]:", arr[8:1:-2])  # 역방향 step


def demonstrate_copy_semantics() -> None:
    """슬라이싱은 얕은 복사(shallow copy)를 생성한다."""
    print()
    print("=" * 45)
    print("복사 의미론(Shallow Copy) 확인")
    print("=" * 45)

    original = [10, 20, 30, 40, 50]
    sliced = original[1:4]     # [20, 30, 40] -- 새 리스트
    sliced[0] = 999

    print("original:", original)   # 원본 변경 없음
    print("sliced  :", sliced)     # [999, 30, 40]
    print("-> 슬라이싱 결과는 독립된 새 리스트입니다.")

    # 중첩 리스트의 얕은 복사 주의
    nested = [[1, 2], [3, 4], [5, 6]]
    copied = nested[:]         # 외부 리스트는 복사
    copied[0][0] = 999         # 내부 리스트는 공유!
    print()
    print("nested (내부 공유 확인):", nested)   # [[999, 2], ...]
    print("-> 중첩 리스트는 copy.deepcopy()를 사용하세요.")


def demonstrate_2d_slicing() -> None:
    """2차원 배열(리스트의 리스트) 슬라이싱 예제."""
    print()
    print("=" * 45)
    print("2D 배열 슬라이싱")
    print("=" * 45)

    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9, 10, 11, 12],
    ]

    print("원본 행렬:")
    for row in matrix:
        print(" ", row)

    # 행 슬라이싱
    sub_rows = matrix[0:2]          # 0~1번 행
    print("\nmatrix[0:2] -- 상위 2행:")
    for row in sub_rows:
        print(" ", row)

    # 열 슬라이싱 (리스트 컴프리헨션 사용)
    col_2 = [row[2] for row in matrix]   # 2번 열
    print("\n2번 열:", col_2)

    # 부분 행렬
    sub_matrix = [row[1:3] for row in matrix[0:2]]
    print("\nmatrix[0:2][열 1:3] -- 2x2 부분 행렬:")
    for row in sub_matrix:
        print(" ", row)


def demonstrate_string_slicing() -> None:
    """문자열 슬라이싱 -- 문자열도 시퀀스."""
    print()
    print("=" * 45)
    print("문자열 슬라이싱")
    print("=" * 45)

    s = "Hello, World!"
    print("원본:", s)
    print("s[7:12] :", s[7:12])    # World
    print("s[:5]   :", s[:5])      # Hello
    print("s[::-1] :", s[::-1])    # 역순
    print("s[::2]  :", s[::2])     # 2칸 간격


if __name__ == "__main__":
    demonstrate_1d_slicing()
    demonstrate_copy_semantics()
    demonstrate_2d_slicing()
    demonstrate_string_slicing()
