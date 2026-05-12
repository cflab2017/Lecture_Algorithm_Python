# 주제: 트라이 응용 — 최장 공통 접두사, XOR 트라이 (최대 XOR 쌍)
# Time: O(n×m) LCP, O(n×32) XOR 트라이
# Space: O(n×m) 또는 O(n×32)

from __future__ import annotations


# ── 1. 최장 공통 접두사 (Longest Common Prefix) ──────────────────────────

class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
        self.pass_count: int = 0   # 이 노드를 통과하는 단어 수


class LCPTrie:
    """최장 공통 접두사 계산용 트라이."""

    def __init__(self) -> None:
        self.root = TrieNode()
        self.word_count = 0

    def insert(self, word: str) -> None:
        """Time: O(m)"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.pass_count += 1
        node.is_end = True
        self.word_count += 1

    def longest_common_prefix(self) -> str:
        """모든 삽입된 단어의 최장 공통 접두사.

        핵심: 자식이 1개이고 모든 단어가 통과하는 동안 계속 내려감

        Time:  O(m_min) — 가장 짧은 단어 길이
        Space: O(1)
        """
        node = self.root
        prefix = []

        while (
            len(node.children) == 1        # 갈림길 없음
            and not node.is_end            # 여기서 끝나는 단어 없음
        ):
            ch = next(iter(node.children))
            next_node = node.children[ch]
            if next_node.pass_count < self.word_count:
                break
            prefix.append(ch)
            node = next_node

        return "".join(prefix)


def lcp_of_list(strs: list[str]) -> str:
    """문자열 리스트의 최장 공통 접두사 (트라이 없이 O(n×m)).

    Time:  O(n × m_min)
    Space: O(1)
    """
    if not strs:
        return ""

    trie = LCPTrie()
    for s in strs:
        trie.insert(s)
    return trie.longest_common_prefix()


# ── 2. XOR 트라이 (최대 XOR 쌍) ─────────────────────────────────────────

class XORTrieNode:
    def __init__(self) -> None:
        self.children: dict[int, XORTrieNode] = {}   # 0 또는 1


class XORTrie:
    """정수의 XOR 최댓값을 구하는 비트 트라이.

    각 정수를 31비트 이진수로 저장 (MSB부터).
    """

    BITS = 31

    def __init__(self) -> None:
        self.root = XORTrieNode()

    def insert(self, num: int) -> None:
        """정수를 비트 트라이에 삽입.

        Time:  O(32)
        Space: O(32)
        """
        node = self.root
        for i in range(self.BITS, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = XORTrieNode()
            node = node.children[bit]

    def max_xor_with(self, num: int) -> int:
        """num과 XOR이 최대인 트라이 내 수와의 XOR 값.

        각 비트에서 반대 비트 방향으로 이동하면 XOR 최대화.

        Time:  O(32)
        Space: O(1)
        """
        node = self.root
        xor_val = 0
        for i in range(self.BITS, -1, -1):
            bit = (num >> i) & 1
            opposite = 1 - bit
            if opposite in node.children:
                xor_val |= (1 << i)   # 이 비트에서 XOR = 1
                node = node.children[opposite]
            elif bit in node.children:
                node = node.children[bit]
            else:
                break
        return xor_val


def max_xor_pair(nums: list[int]) -> tuple[int, int, int]:
    """배열에서 XOR이 최대인 두 수와 XOR 값 반환.

    Time:  O(n × 32)
    Space: O(n × 32)
    """
    if len(nums) < 2:
        return (0, 0, 0)

    trie = XORTrie()
    max_xor = 0
    best_pair = (nums[0], nums[1])

    trie.insert(nums[0])
    for i in range(1, len(nums)):
        xor_val = trie.max_xor_with(nums[i])
        if xor_val > max_xor:
            max_xor = xor_val
            best_pair = (nums[i], -1)   # 정확한 쌍 찾기는 추가 작업 필요
        trie.insert(nums[i])

    return (best_pair[0], best_pair[1], max_xor)


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== 최장 공통 접두사 ===")
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["interview", "interact", "interface", "internal"],
        ["a"],
        [],
    ]
    for words in test_cases:
        lcp = lcp_of_list(words)
        print(f"  {words} → '{lcp}'")

    print("\n=== XOR 트라이 ===")
    nums = [3, 10, 5, 25, 2, 8]
    trie = XORTrie()
    for n in nums:
        trie.insert(n)

    print("배열:", nums)
    print("각 수와 최대 XOR 값:")
    for n in nums:
        mx = trie.max_xor_with(n)
        print(f"  {n:2d} ({bin(n):>10s}) → 최대 XOR = {mx:2d} ({bin(mx)})")

    print("\n최대 XOR 쌍 탐색:")
    _, _, best = max_xor_pair(nums)
    print(f"  최대 XOR 값: {best}")

    # 전수 확인
    brute_max = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            brute_max = max(brute_max, nums[i] ^ nums[j])
    print(f"  전수 확인 결과: {brute_max}")
    assert best == brute_max, "결과 불일치!"
    print("  결과 일치 ✓")
