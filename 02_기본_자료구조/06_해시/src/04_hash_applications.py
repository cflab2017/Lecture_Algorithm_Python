# Topic : 해시 응용 -- Two-Sum, 애너그램 그룹, 연속 수열, 부분합
# Time  : O(n) -- 해시 기반
# Space : O(n) -- 해시 테이블 크기

from collections import Counter, defaultdict


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Two-Sum: 합이 target인 두 인덱스 반환 -- O(n).

    Brute force O(n^2)를 해시로 O(n)으로 개선.
    """
    seen: dict[int, int] = {}   # {값: 인덱스}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


def group_anagrams(words: list[str]) -> list[list[str]]:
    """애너그램끼리 그룹화 -- O(n * k log k), k=단어 최대 길이.

    정렬된 문자열을 키로 사용.
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for word in words:
        key = "".join(sorted(word.lower()))
        groups[key].append(word)
    return list(groups.values())


def first_non_repeating(s: str) -> str:
    """첫 번째 유일한 문자 반환 -- O(n)."""
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return ""   # 없으면 빈 문자열


def longest_consecutive_sequence(nums: list[int]) -> int:
    """가장 긴 연속 수열 길이 반환 -- O(n).

    정렬 없이 해시 셋을 이용해 O(n) 달성.
    """
    num_set = set(nums)
    best = 0

    for num in num_set:
        if num - 1 not in num_set:    # 연속의 시작점만 탐색
            cur = num
            length = 1
            while cur + 1 in num_set:
                cur += 1
                length += 1
            best = max(best, length)

    return best


def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """합이 k인 부분 배열 개수 반환 -- O(n).

    누적 합 + 해시 맵 패턴.
    """
    count = 0
    prefix_sum = 0
    prefix_cnt: dict[int, int] = defaultdict(int)
    prefix_cnt[0] = 1   # 빈 배열의 누적 합 = 0

    for num in nums:
        prefix_sum += num
        count += prefix_cnt[prefix_sum - k]
        prefix_cnt[prefix_sum] += 1

    return count


if __name__ == "__main__":
    print("=" * 55)
    print("Two-Sum")
    print("=" * 55)
    cases = [
        ([2, 7, 11, 15], 9,  (0, 1)),
        ([3, 2, 4],      6,  (1, 2)),
        ([3, 3],         6,  (0, 1)),
        ([1, 5, 3, 7],   8,  (1, 2)),
    ]
    for nums, target, expected in cases:
        result = two_sum(nums, target)
        ok = "OK" if result == expected else "NG"
        print(f"nums={nums}, target={target} -> {result}  {ok}")

    print()
    print("=" * 55)
    print("애너그램 그룹화")
    print("=" * 55)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = group_anagrams(words)
    print("입력:", words)
    for g in groups:
        print(" ", sorted(g))

    print()
    print("=" * 55)
    print("첫 번째 유일한 문자")
    print("=" * 55)
    for s in ["leetcode", "loveleetcode", "aabb"]:
        result = first_non_repeating(s)
        print(f"{s!r:15} -> {result!r}")

    print()
    print("=" * 55)
    print("가장 긴 연속 수열")
    print("=" * 55)
    seq_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ]
    for nums, expected in seq_cases:
        result = longest_consecutive_sequence(nums)
        ok = "OK" if result == expected else "NG"
        print(f"{nums} -> {result}  {ok}")

    print()
    print("=" * 55)
    print("합이 k인 부분 배열 개수")
    print("=" * 55)
    sub_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
    ]
    for nums, k, expected in sub_cases:
        result = subarray_sum_equals_k(nums, k)
        ok = "OK" if result == expected else "NG"
        print(f"nums={nums}, k={k} -> {result}  {ok}")
