# 백준 5052 — 전화번호 목록
# https://www.acmicpc.net/problem/5052
# Time: O(n × m)  Space: O(n × m)
# 트라이: 삽입 중 접두사 충돌 탐지

import sys

input = sys.stdin.readline


class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class PhoneTrie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.consistent = True

    def insert(self, number: str) -> None:
        """번호 삽입. 삽입 중 충돌 감지.

        충돌 조건:
          1) 기존 번호가 이 번호의 접두사 (중간 is_end 만남)
          2) 이 번호가 기존 번호의 접두사 (삽입 후 자식이 있음)
        """
        node = self.root
        for ch in number:
            if node.is_end:
                # 기존 짧은 번호가 현재 번호의 접두사
                self.consistent = False
                return
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True
        if node.children:
            # 현재 번호가 기존 긴 번호의 접두사
            self.consistent = False


def solve() -> None:
    t = int(input())
    results: list[str] = []

    for _ in range(t):
        n = int(input())
        trie = PhoneTrie()
        numbers = [input().strip() for _ in range(n)]

        for num in numbers:
            trie.insert(num)

        results.append("YES" if trie.consistent else "NO")

    sys.stdout.write("\n".join(results) + "\n")


solve()
