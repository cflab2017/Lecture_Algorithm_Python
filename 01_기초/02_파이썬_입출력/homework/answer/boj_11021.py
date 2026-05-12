# =============================================================================
# 백준 11021번: A+B - 7
# 링크: https://www.acmicpc.net/problem/11021
# 시간복잡도: O(T) — T개의 테스트 케이스 처리
# 공간복잡도: O(T) — 출력 버퍼
#
# 출력 형식: 'Case #x: A+B' (x는 1부터 시작하는 케이스 번호)
# =============================================================================

import sys
input = sys.stdin.readline


def solve():
    t = int(input())    # 테스트 케이스 수
    output = []

    for case_num in range(1, t + 1):         # 케이스 번호: 1부터 시작
        a, b = map(int, input().split())
        # f-string으로 형식 지정
        output.append(f"Case #{case_num}: {a + b}")

    sys.stdout.write('\n'.join(output) + '\n')


if __name__ == "__main__":
    solve()
