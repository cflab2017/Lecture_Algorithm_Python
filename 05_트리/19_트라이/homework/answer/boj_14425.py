# 백준 14425 — 문자열 집합
# https://www.acmicpc.net/problem/14425
# Time: O((n+m) × L)  Space: O(n × L)
# 방법 1: set (간결), 방법 2: 트라이 (학습 목적)

import sys

input = sys.stdin.readline


# ── 방법 1: Python set ────────────────────────────────────────────────────
def solve_set() -> None:
    n, m = map(int, input().split())
    word_set: set[str] = set()

    for _ in range(n):
        word_set.add(input().strip())

    count = 0
    for _ in range(m):
        word = input().strip()
        if word in word_set:
            count += 1

    print(count)


# ── 방법 2: 트라이 ────────────────────────────────────────────────────────
class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end


def solve_trie() -> None:
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1])
    idx += 2

    trie = Trie()
    for i in range(n):
        trie.insert(data[idx + i])
    idx += n

    count = 0
    for i in range(m):
        if trie.search(data[idx + i]):
            count += 1

    print(count)


# 제출 시 solve_set() 또는 solve_trie() 중 하나 선택
# set 방식이 더 빠름 (Python dict 최적화)
solve_trie()
