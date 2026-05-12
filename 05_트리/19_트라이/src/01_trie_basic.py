# 주제: 트라이 기본 — 삽입, 탐색, 접두사 확인
# Time: O(m) 삽입/탐색 — m = 단어 길이
# Space: O(alphabet_size × max_len × n) 최악

from __future__ import annotations


class TrieNode:
    """트라이 노드."""

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False   # 이 노드에서 끝나는 단어 존재 여부


class Trie:
    """접두사 트리(Prefix Tree) 구현."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """단어 삽입.

        Time:  O(m) — m = 단어 길이
        Space: O(m) — 새 노드 최대 m개 생성
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """단어가 트라이에 정확히 존재하는지 확인.

        Time:  O(m)
        Space: O(1)
        """
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """해당 접두사로 시작하는 단어가 존재하는지 확인.

        Time:  O(m) — m = 접두사 길이
        Space: O(1)
        """
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode | None:
        """접두사 경로 끝 노드 반환 (없으면 None).

        Time:  O(m)
        Space: O(1)
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def delete(self, word: str) -> bool:
        """단어 삭제. 다른 단어와 공유하는 노드는 보존.

        Time:  O(m)
        Space: O(m) — 재귀 스택
        """
        def _delete(node: TrieNode, word: str, depth: int) -> bool:
            """True이면 현재 노드 삭제 가능."""
            if depth == len(word):
                if not node.is_end:
                    return False   # 단어가 없음
                node.is_end = False
                return len(node.children) == 0   # 자식 없으면 삭제 가능

            ch = word[depth]
            if ch not in node.children:
                return False

            should_delete = _delete(node.children[ch], word, depth + 1)
            if should_delete:
                del node.children[ch]
                return not node.is_end and len(node.children) == 0

            return False

        return _delete(self.root, word, 0)

    def count_words(self) -> int:
        """저장된 단어 수.

        Time:  O(n × m)
        Space: O(h) — DFS 스택
        """
        def dfs(node: TrieNode) -> int:
            total = 1 if node.is_end else 0
            for child in node.children.values():
                total += dfs(child)
            return total

        return dfs(self.root)


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "apt", "bat", "ball", "band"]

    print("=== 삽입 ===")
    for w in words:
        trie.insert(w)
        print(f"  insert('{w}')")

    print("\n=== 단어 탐색 ===")
    test_words = ["app", "apple", "ap", "appl", "bat", "ba", "ban"]
    for w in test_words:
        found = trie.search(w)
        print(f"  search('{w}'): {found}")

    print("\n=== 접두사 확인 ===")
    prefixes = ["ap", "app", "b", "ba", "bal", "bx", ""]
    for p in prefixes:
        exists = trie.starts_with(p)
        print(f"  starts_with('{p}'): {exists}")

    print(f"\n총 저장 단어 수: {trie.count_words()}")

    print("\n=== 삭제 ===")
    print(f"  delete('app'): {trie.delete('app')}")
    print(f"  search('app'): {trie.search('app')}")
    print(f"  search('apple'): {trie.search('apple')}")  # 여전히 존재해야 함
    print(f"  총 단어 수: {trie.count_words()}")
