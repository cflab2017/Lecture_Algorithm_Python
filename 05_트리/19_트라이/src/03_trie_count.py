# 주제: 트라이 카운트 — 접두사 개수, 단어 빈도
# Time: O(m) 삽입/접두사카운트 — m = 단어 길이
# Space: O(n × m)

from __future__ import annotations


class CountTrieNode:
    """카운트 기능이 있는 트라이 노드."""

    def __init__(self) -> None:
        self.children: dict[str, CountTrieNode] = {}
        self.is_end: bool = False
        self.prefix_count: int = 0   # 이 노드를 통과한 단어 수
        self.word_count: int = 0     # 이 노드에서 끝나는 단어 수 (중복 허용)


class CountTrie:
    """접두사 카운트와 단어 빈도를 지원하는 트라이."""

    def __init__(self) -> None:
        self.root = CountTrieNode()

    def insert(self, word: str) -> None:
        """단어 삽입 (중복 허용 — 빈도 카운트).

        Time:  O(m)
        Space: O(m)
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = CountTrieNode()
            node = node.children[ch]
            node.prefix_count += 1   # 통과 카운트 증가
        node.is_end = True
        node.word_count += 1

    def count_words_with_prefix(self, prefix: str) -> int:
        """주어진 접두사로 시작하는 단어 수 반환.

        Time:  O(m)
        Space: O(1)
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count

    def count_exact(self, word: str) -> int:
        """정확히 그 단어의 삽입 횟수 반환.

        Time:  O(m)
        Space: O(1)
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.word_count if node.is_end else 0

    def delete_one(self, word: str) -> bool:
        """단어 하나 삭제 (word_count 1 감소).

        Time:  O(m)
        Space: O(m) — 재귀
        """
        if self.count_exact(word) == 0:
            return False

        node = self.root
        for ch in word:
            node = node.children[ch]
            node.prefix_count -= 1
        node.word_count -= 1
        if node.word_count == 0:
            node.is_end = False
        return True

    def most_common_prefix(self) -> str:
        """가장 많은 단어가 공유하는 접두사 (최대 prefix_count 경로).

        Time:  O(m_max)
        Space: O(1)
        """
        node = self.root
        prefix = []
        while node.children:
            # 가장 많이 공유된 자식 선택
            best_ch = max(
                node.children,
                key=lambda ch: node.children[ch].prefix_count,
            )
            best_node = node.children[best_ch]
            if best_node.prefix_count == node.prefix_count or node.is_end:
                break
            prefix.append(best_ch)
            node = best_node
        return "".join(prefix)


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    trie = CountTrie()

    # 단어 삽입 (중복 포함)
    words = [
        "apple", "apple", "apple",
        "application", "application",
        "apply",
        "apt", "apt",
        "banana", "band",
    ]

    for w in words:
        trie.insert(w)

    print("=== 접두사 카운트 ===")
    prefixes = ["app", "ap", "appl", "apple", "b", "ba", "ban", "xyz"]
    for p in prefixes:
        cnt = trie.count_words_with_prefix(p)
        print(f"  '{p}' 접두사 단어 수: {cnt}")

    print("\n=== 단어 빈도 ===")
    check_words = ["apple", "apply", "apt", "banana", "band", "app"]
    for w in check_words:
        cnt = trie.count_exact(w)
        print(f"  '{w}' 등장 횟수: {cnt}")

    print("\n=== 삭제 후 카운트 ===")
    trie.delete_one("apple")
    print(f"  'apple' 1개 삭제 후: {trie.count_exact('apple')}")
    print(f"  'app' 접두사 단어 수: {trie.count_words_with_prefix('app')}")

    print(f"\n=== 가장 공통된 접두사 ===")
    print(f"  '{trie.most_common_prefix()}'")
