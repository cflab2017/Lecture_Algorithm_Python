# =============================================================================
# 백준 1546번: 평균
# 링크: https://www.acmicpc.net/problem/1546
# 시간복잡도: O(n) — 배열을 두 번 순회 (최댓값, 합 계산)
# 공간복잡도: O(n) — 점수 배열 저장
# =============================================================================
# 풀이 전략:
#   1. N개의 점수를 읽는다.
#   2. 최댓값 M을 찾는다.  ← O(n)
#   3. 각 점수를 (점수 / M * 100)으로 변환한 뒤 평균을 구한다.  ← O(n)
#   N ≤ 1,000이므로 어떤 풀이도 통과하지만 O(n)이 이상적입니다.
# =============================================================================

import sys


def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])                    # 과목 수
    scores = list(map(int, input_data[1:n + 1]))  # 점수 목록

    # 최댓값 탐색 — O(n)
    max_score = max(scores)

    # 변환된 점수의 합 계산 — O(n)
    # 변환 공식: new_score = score / max_score * 100
    # 평균 = sum(new_scores) / n
    #       = sum(score / max_score * 100 for score in scores) / n
    #       = (sum(scores) * 100 / max_score) / n
    total = sum(scores)                        # 원점수 합
    average = total / max_score * 100 / n     # 변환 후 평균

    print(f"{average:.12f}")  # 소수점 12자리 출력 (오차 허용범위 내)


if __name__ == "__main__":
    solve()
