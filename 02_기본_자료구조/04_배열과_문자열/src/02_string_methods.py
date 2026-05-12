# Topic : 문자열 주요 메서드 실습
# Time  : 각 메서드별 주석 참고
# Space : O(n) -- 대부분 새로운 문자열 반환


def demo_split_join() -> None:
    """split / join 메서드 -- O(n)."""
    print("=" * 50)
    print("split / join")
    print("=" * 50)

    sentence = "사과,바나나,체리,딸기"
    fruits = sentence.split(",")        # 구분자로 분리
    print("split(','):", fruits)

    # 구분자 없이 -- 공백 기준, 연속 공백 무시
    words = "  hello   world  ".split()
    print("split()   :", words)         # ['hello', 'world']

    # split(' ') vs split() 차이
    spaced = "a  b".split(' ')          # 빈 문자열 포함!
    print("split(' ') :", spaced)       # ['a', '', 'b']

    # join -- 리스트를 문자열로
    joined = " | ".join(fruits)
    print("join(' | '):", joined)

    # 문자열 누적 -- join이 O(n), += 반복은 O(n^2)
    chars = list("Hello")
    fast = "".join(chars)               # O(n)
    print("''.join()  :", fast)


def demo_strip() -> None:
    """strip / lstrip / rstrip -- O(n)."""
    print()
    print("=" * 50)
    print("strip / lstrip / rstrip")
    print("=" * 50)

    s = "   Hello, Python!   "
    print("원본         :", repr(s))
    print("strip()      :", repr(s.strip()))
    print("lstrip()     :", repr(s.lstrip()))
    print("rstrip()     :", repr(s.rstrip()))

    # 특정 문자 제거
    s2 = "###중요###"
    print("strip('#')   :", s2.strip("#"))


def demo_replace_find() -> None:
    """replace / find / count -- O(n)."""
    print()
    print("=" * 50)
    print("replace / find / count")
    print("=" * 50)

    text = "banana"
    print("원본 :", text)
    print("replace('a','o')  :", text.replace("a", "o"))       # bonono
    print("replace('a','o',2):", text.replace("a", "o", 2))    # 최대 2회

    # find -- 없으면 -1 반환
    s = "Hello, World!"
    print("find('World') :", s.find("World"))   # 7
    print("find('xyz')   :", s.find("xyz"))     # -1
    print("index('World'):", s.index("World"))  # 7 (없으면 ValueError)

    # rfind -- 오른쪽부터 탐색
    t = "abcabcabc"
    print("rfind('abc')  :", t.rfind("abc"))    # 6
    print("count('abc')  :", t.count("abc"))    # 3


def demo_case_methods() -> None:
    """upper / lower / capitalize / title -- O(n)."""
    print()
    print("=" * 50)
    print("대소문자 변환")
    print("=" * 50)

    s = "hello, World!"
    print("원본         :", s)
    print("upper()      :", s.upper())
    print("lower()      :", s.lower())
    print("capitalize() :", s.capitalize())   # 첫 글자만 대문자
    print("title()      :", s.title())        # 단어별 첫 글자 대문자
    print("swapcase()   :", s.swapcase())     # 대<->소 교환


def demo_check_methods() -> None:
    """isdigit / isalpha / isalnum / startswith / endswith -- O(n)."""
    print()
    print("=" * 50)
    print("검사 메서드")
    print("=" * 50)

    samples = ["hello", "Hello123", "12345", "  ", ""]
    for s in samples:
        print(
            f"{s!r:12} -> isalpha={str(s.isalpha()):5}"
            f" isdigit={str(s.isdigit()):5}"
            f" isalnum={str(s.isalnum()):5}"
        )

    url = "https://example.com"
    print()
    print("startswith('https'):", url.startswith("https"))
    print("endswith('.com')   :", url.endswith(".com"))


def demo_ord_chr() -> None:
    """ord / chr -- 아스키 코드 변환."""
    print()
    print("=" * 50)
    print("ord() / chr() -- 아스키 코드")
    print("=" * 50)

    print("ord('A') =", ord("A"), "/ ord('a') =", ord("a"), "/ ord('0') =", ord("0"))
    print("chr(65)  =", chr(65),  "/ chr(97)  =", chr(97),  "/ chr(48)  =", chr(48))

    # 알파벳 인덱스 (0-based)
    for ch in "ace":
        idx = ord(ch) - ord("a")
        print(f"'{ch}' 의 알파벳 인덱스: {idx}")

    # 알파벳 전체 출력
    alphabet = [chr(ord("a") + i) for i in range(26)]
    print("알파벳:", "".join(alphabet))


if __name__ == "__main__":
    demo_split_join()
    demo_strip()
    demo_replace_find()
    demo_case_methods()
    demo_check_methods()
    demo_ord_chr()
