# =============================================================================
# 백준 11279번: 최대 힙
# 링크: https://www.acmicpc.net/problem/11279
# 시간복잡도: O(N log N) — N번의 heappush/heappop, 각 O(log N)
# 공간복잡도: O(N) — 힙에 저장되는 원소 수
#
# 자료구조 선택: heapq (최솟값 힙) + 음수 변환 트릭으로 최댓값 힙 구현
#   - 파이썬 heapq는 최솟값 힙만 지원합니다.
#   - 값을 음수로 저장하면 최솟값 힙이 사실상 최댓값 힙이 됩니다.
#     예: push(-5), push(-3) → pop()이 -5 반환 → 실제 최댓값 5
# =============================================================================

import sys
import heapq
input = sys.stdin.readline


def solve():
    n = int(input())    # 연산 횟수
    heap = []           # 최댓값 힙 (음수 변환 트릭 사용)
    output = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            # 최댓값 꺼내기 — O(log N)
            if heap:
                # 음수로 저장했으므로, 꺼낼 때 다시 음수를 취해 양수로 변환
                output.append(str(-heapq.heappop(heap)))
            else:
                output.append('0')  # 빈 힙이면 0 출력
        else:
            # 값 삽입 — 음수로 변환하여 저장 O(log N)
            heapq.heappush(heap, -x)

    sys.stdout.write('\n'.join(output) + '\n')


if __name__ == "__main__":
    solve()
