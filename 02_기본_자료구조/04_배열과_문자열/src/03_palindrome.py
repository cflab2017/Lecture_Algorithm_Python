# Topic : 팰린드롬(Palindrome) 검사
# Time  : O(n) -- 문자열 길이에 비례
# Space : O(n) 나이브 / O(1) 투 포인터


def is_palindrome_naive(s: str) -> bool:
    """나이브 방법: 역순 문자열과 비교 -- Time O(n), Space O(n)."""
    cleaned = s.lower()
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointer(s: str) -> bool:
    """투 포인터 방법 -- Time O(n), Space O(1).

    시각화:
        r a c e c a r
        ^           ^   r==r -> 이동
          ^       ^     a==a -> 이동
            ^   ^       c==c -> 이동
              ^ ^        e==e -> left >= right -> 팰린드롬!
    """
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_alphanumeric(s: str) -> bool:
    """영문자/숫자만 고려하는 팰린드롬 -- LeetCode 125 스타일.

    예: 'A man, a plan, a canal: Panama' -> True
    Time O(n), Space O(1) (투 포인터).
    """
    left, right = 0, len(s) - 1
    while left < right:
        # 영숫자가 아닌 문자 건너뜀
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def longest_palindrome_expand(s: str) -> str:
    """중심 확장(Expand Around Center) -- O(n^2) 시간, O(1) 공간."""
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    best = ""
    for i in range(len(s)):
        odd = expand(i, i)          # 홀수 길이 팰린드롬
        even = expand(i, i + 1)     # 짝수 길이 팰린드롬
        if len(odd) > len(best):
            best = odd
        if len(even) > len(best):
            best = even
    return best


if __name__ == "__main__":
    print("=" * 50)
    print("팰린드롬 검사")
    print("=" * 50)

    test_cases = [
        ("racecar", True),
        ("hello",   False),
        ("abcba",   True),
        ("a",       True),
        ("",        True),
        ("abba",    True),
    ]

    print(f"{'문자열':15} {'나이브':8} {'투포인터':10}")
    print("-" * 35)
    for word, expected in test_cases:
        naive = is_palindrome_naive(word)
        tp    = is_palindrome_two_pointer(word)
        status = "OK" if naive == expected else "NG"
        print(f"{word!r:15} {str(naive):8} {str(tp):10} {status}")

    print()
    print("=" * 50)
    print("영숫자 팰린드롬")
    print("=" * 50)
    alphanums = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]
    for s in alphanums:
        short = repr(s)[:35]
        print(f"{short:37} -> {is_palindrome_alphanumeric(s)}")

    print()
    print("=" * 50)
    print("가장 긴 팰린드롬 부분 문자열")
    print("=" * 50)
    for s in ["babad", "cbbd", "racecar", "abcba"]:
        result = longest_palindrome_expand(s)
        print(f"{s!r:10} -> {result!r}")
