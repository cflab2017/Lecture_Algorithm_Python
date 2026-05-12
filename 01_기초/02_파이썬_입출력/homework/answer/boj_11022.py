# =============================================================================
# 백준 11022번: A+B - 8
# 링크: https://www.acmicpc.net/problem/11022
# 시간복잡도: O(T) — T개의 테스트 케이스 처리
# 공간복잡도: O(T) — 출력 버퍼
#
# 출력 형식: 'Case #x: A + B = C' (x는 케이스 번호, C = A+B)
# =============================================================================

import sys
input = sys.stdin.readline


def solve():
    t = int(input())    # 테스트 케이스 수
    output = []

    for case_num in range(1, t + 1):
        a, b = map(int, input().split())
        # 형식: 'Case #1: 1 + 1 = 2'
        output.append(f"Case #{case_num}: {a} + {b} = {a + b}")

    sys.stdout.write('\n'.join(output) + '\n')


if __name__ == "__main__":
    solve()
