# =============================================================================
# 백준 1927번: 최소 힙
# 링크: https://www.acmicpc.net/problem/1927
# 시간복잡도: O(N log N) — N번의 heappush/heappop, 각 O(log N)
# 공간복잡도: O(N) — 힙에 저장되는 원소 수
#
# 자료구조 선택: heapq (최솟값 힙)
#   - 이유: 항상 최솟값을 O(log N)으로 삽입/삭제 가능
#   - list + sorted()를 사용하면 삭제마다 O(N log N) → 전체 O(N² log N)
#   - set은 최솟값 접근이 O(N)이므로 적합하지 않음
# =============================================================================

import sys
import heapq
input = sys.stdin.readline


def solve():
    n = int(input())    # 연산 횟수
    heap = []           # 최솟값 힙 (heapq 사용)
    output = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            # 최솟값 꺼내기 — O(log N)
            if heap:
                output.append(str(heapq.heappop(heap)))
            else:
                output.append('0')  # 빈 힙이면 0 출력
        else:
            # 값 삽입 — O(log N)
            heapq.heappush(heap, x)

    sys.stdout.write('\n'.join(output) + '\n')


if __name__ == "__main__":
    solve()
