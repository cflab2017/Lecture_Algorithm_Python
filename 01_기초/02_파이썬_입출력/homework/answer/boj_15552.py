# =============================================================================
# 백준 15552번: 빠른 A+B
# 링크: https://www.acmicpc.net/problem/15552
# 시간복잡도: O(T) — T개의 테스트 케이스 처리
# 공간복잡도: O(T) — 출력 결과를 리스트에 저장
#
# 핵심: T ≤ 1,000,000이므로 반드시 빠른 I/O 필요
#   - sys.stdin.readline() 사용 (input() 사용 시 TLE)
#   - 출력을 리스트에 모아 한 번에 출력 (print() 반복 호출 시 TLE)
# =============================================================================

import sys
input = sys.stdin.readline  # input() 대체 — 빠른 입력


def solve():
    t = int(input())          # 테스트 케이스 수
    output = []               # 출력 버퍼 — 한 번에 출력하기 위해

    for _ in range(t):
        a, b = map(int, input().split())  # 공백 구분 두 정수 읽기
        output.append(str(a + b))         # 결과를 문자열로 변환하여 저장

    # 한 번에 출력 — print()를 T번 호출하는 것보다 훨씬 빠름
    sys.stdout.write('\n'.join(output) + '\n')


if __name__ == "__main__":
    solve()
