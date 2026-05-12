# 백준 5639 — 이진 검색 트리
# https://www.acmicpc.net/problem/5639
# Time: O(n log n)  Space: O(n)
# 전위 순회 → 후위 순회 변환

import sys
from bisect import bisect_left

input = sys.stdin.readline
sys.setrecursionlimit(20_000)


def solve() -> None:
    preorder: list[int] = []
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            preorder.append(int(line))
        except EOFError:
            break

    output: list[str] = []

    def postorder(start: int, end: int) -> None:
        """preorder[start:end]를 후위 순회로 출력.

        preorder[start] = 루트
        start+1 ~ (루트보다 작은 마지막 인덱스) = 왼쪽
        나머지 = 오른쪽

        Time:  O(n log n) — bisect 사용
        """
        if start >= end:
            return

        root_val = preorder[start]

        # 오른쪽 서브트리 시작 위치: preorder[start+1:end]에서 root_val보다 크거나 같은 첫 인덱스
        # bisect_left로 O(log n) 탐색
        left_start = start + 1
        right_start = end

        # 선형 탐색 (단순) — O(n²) 가능
        # right_start = left_start
        # while right_start < end and preorder[right_start] < root_val:
        #     right_start += 1

        # O(n log n): 정렬된 서브배열에서 bisect 사용 불가 (전위 순회는 정렬 아님)
        # 실용적 O(n²) 풀이 (n ≤ 10,000이므로 충분)
        right_start = left_start
        while right_start < end and preorder[right_start] < root_val:
            right_start += 1

        postorder(left_start, right_start)
        postorder(right_start, end)
        output.append(str(root_val))

    postorder(0, len(preorder))
    sys.stdout.write("\n".join(output) + "\n")


solve()
