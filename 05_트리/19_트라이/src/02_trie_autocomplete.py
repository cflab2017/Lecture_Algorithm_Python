# 주제: 트라이 자동 완성
# Time: O(m + 결과 수) 자동완성 — m = 접두사 길이
# Space: O(n × m) 트라이 저장

from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
        self.word: str = ""   # 단어 끝 노드에 전체 단어 저장


class AutocompleteTrie:
    """자동 완성 기능이 있는 트라이."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """단어 삽입.

        Time:  O(m)
        Space: O(m)
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.word = word

    def autocomplete(self, prefix: str, max_results: int = 10) -> list[str]:
        """접두사로 시작하는 모든 단어 반환 (알파벳 순).

        Time:  O(m + T) — T = 접두사 이하 전체 노드 수
        Space: O(결과 수 + h)
        """
        # 접두사 노드 찾기
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        # DFS로 모든 단어 수집
        results: list[str] = []
        self._collect_words(node, results, max_results)
        return sorted(results)

    def _collect_words(
        self,
        node: TrieNode,
        results: list[str],
        max_results: int,
    ) -> None:
        """DFS로 단어 수집."""
        if len(results) >= max_results:
            return
        if node.is_end:
            results.append(node.word)
        for ch in sorted(node.children.keys()):   # 알파벳 순
            self._collect_words(node.children[ch], results, max_results)

    def top_k_autocomplete(
        self,
        prefix: str,
        k: int = 5,
    ) -> list[str]:
        """상위 k개 자동 완성 (BFS — 짧은 단어 우선).

        Time:  O(m + T)
        Space: O(T)
        """
        from collections import deque

        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results: list[str] = []
        queue: deque[TrieNode] = deque([node])

        while queue and len(results) < k:
            curr = queue.popleft()
            if curr.is_end:
                results.append(curr.word)
            for ch in sorted(curr.children.keys()):
                queue.append(curr.children[ch])

        return results


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    trie = AutocompleteTrie()

    # 영어 단어 사전
    dictionary = [
        "apple", "application", "apply", "apt",
        "apartment", "append", "appear", "apple",
        "bat", "battle", "ball", "band", "bank",
        "can", "candy", "cancel", "cap",
        "do", "dog", "door", "double",
    ]

    for word in dictionary:
        trie.insert(word)

    print("=== 자동 완성 ===")
    test_prefixes = ["app", "ap", "ba", "ca", "z"]
    for p in test_prefixes:
        suggestions = trie.autocomplete(p)
        print(f"  '{p}' → {suggestions}")

    print("\n=== 상위 3개 자동 완성 (짧은 단어 우선) ===")
    for p in ["app", "ba"]:
        top = trie.top_k_autocomplete(p, k=3)
        print(f"  '{p}' 상위 3개: {top}")

    print("\n=== 검색창 시뮬레이션 ===")
    user_input = "appl"
    print(f"  입력: '{user_input}'")
    suggestions = trie.autocomplete(user_input, max_results=5)
    print(f"  제안:")
    for i, s in enumerate(suggestions, 1):
        print(f"    {i}. {s}")
