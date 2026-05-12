# Topic : 애너그램(Anagram) 검사
# Time  : O(n) Counter 방법 / O(n log n) sorted 방법
# Space : O(1) -- 알파벳 26개 고정 (Counter 방법)

from collections import Counter


def is_anagram_sorted(s: str, t: str) -> bool:
    """sorted 비교 -- Time O(n log n), Space O(n).

    두 문자열을 정렬해서 같으면 애너그램.
    """
    return sorted(s.lower()) == sorted(t.lower())


def is_anagram_counter(s: str, t: str) -> bool:
    """Counter 비교 -- Time O(n), Space O(1) (알파벳 26자 고정).

    Counter는 각 문자의 빈도를 딕셔너리로 저장한다.
    """
    return Counter(s.lower()) == Counter(t.lower())


def is_anagram_manual(s: str, t: str) -> bool:
    """직접 딕셔너리 구현 -- Time O(n), Space O(1).

    Counter 없이 구현하는 방법.
    """
    if len(s) != len(t):
        return False

    freq: dict[str, int] = {}
    for ch in s.lower():
        freq[ch] = freq.get(ch, 0) + 1
    for ch in t.lower():
        freq[ch] = freq.get(ch, 0) - 1
        if freq[ch] < 0:
            return False
    return True


def is_anagram_array(s: str, t: str) -> bool:
    """배열(크기 26) 사용 -- Time O(n), Space O(1).

    소문자만 허용하는 경우 가장 빠른 구현.
    """
    if len(s) != len(t):
        return False

    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord("a")] += 1
    for ch in t:
        count[ord(ch) - ord("a")] -= 1
    return all(c == 0 for c in count)


def group_anagrams(words: list[str]) -> list[list[str]]:
    """애너그램 그룹핑 -- Time O(n * k log k), Space O(n*k).

    k = 단어 최대 길이.
    정렬된 문자열을 키로 사용하여 그룹화.
    """
    groups: dict[str, list[str]] = {}
    for word in words:
        key = "".join(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


def find_all_anagram_positions(text: str, pattern: str) -> list[int]:
    """문자열에서 패턴의 모든 애너그램 위치 반환 -- O(n) 슬라이딩 윈도우.

    text 안에서 pattern의 애너그램이 시작하는 인덱스 목록.
    """
    result = []
    n, k = len(text), len(pattern)
    if k > n:
        return result

    pattern_cnt = Counter(pattern)
    window_cnt  = Counter(text[:k])

    if window_cnt == pattern_cnt:
        result.append(0)

    for i in range(1, n - k + 1):
        # 윈도우 슬라이딩: 왼쪽 문자 제거, 오른쪽 문자 추가
        left_char  = text[i - 1]
        right_char = text[i + k - 1]

        window_cnt[right_char] += 1
        window_cnt[left_char]  -= 1
        if window_cnt[left_char] == 0:
            del window_cnt[left_char]

        if window_cnt == pattern_cnt:
            result.append(i)

    return result


if __name__ == "__main__":
    print("=" * 50)
    print("애너그램 검사")
    print("=" * 50)

    pairs = [
        ("listen",  "silent",  True),
        ("hello",   "world",   False),
        ("rat",     "car",     False),
        ("anagram", "nagaram", True),
    ]

    print(f"{'s':12} {'t':12} {'sorted':8} {'counter':9} {'manual':8}")
    print("-" * 51)
    for s, t, expected in pairs:
        r1 = is_anagram_sorted(s, t)
        r2 = is_anagram_counter(s, t)
        r3 = is_anagram_manual(s, t)
        ok = "OK" if r1 == expected else "NG"
        print(f"{s:12} {t:12} {str(r1):8} {str(r2):9} {str(r3):8} {ok}")

    print()
    print("=" * 50)
    print("애너그램 그룹핑")
    print("=" * 50)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = group_anagrams(words)
    print("입력:", words)
    for g in groups:
        print(" ", sorted(g))

    print()
    print("=" * 50)
    print("슬라이딩 윈도우 애너그램 위치")
    print("=" * 50)
    text, pat = "cbaebabacd", "abc"
    positions = find_all_anagram_positions(text, pat)
    print(f"text={text!r}, pattern={pat!r}")
    print("애너그램 시작 위치:", positions)   # [0, 6]
