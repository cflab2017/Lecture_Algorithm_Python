# 백준 1316 -- 그룹 단어 체커
# Time : O(N * K) -- 단어 N개, 각 단어 최대 K글자
# Space: O(1)    -- 방문 집합 크기는 알파벳 수(26) 이하
#
# 풀이:
#   각 단어를 순회하며 문자가 바뀌는 순간,
#   이미 방문한 문자가 다시 나타나면 그룹 단어가 아니다.

import sys

input = sys.stdin.readline


def is_group_word(word: str) -> bool:
    """그룹 단어 여부를 반환한다."""
    seen: set[str] = set()
    prev = ""
    for ch in word:
        if ch != prev:            # 문자가 바뀌었다
            if ch in seen:        # 이전에 본 문자가 다시 등장
                return False
            seen.add(prev)
            prev = ch
    return True


def solve() -> None:
    n = int(input())
    answer = 0
    for _ in range(n):
        word = input().strip()
        if is_group_word(word):
            answer += 1
    print(answer)


solve()
