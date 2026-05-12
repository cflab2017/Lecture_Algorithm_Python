"""
백준 11003 — 최솟값 찾기
https://www.acmicpc.net/problem/11003

난이도 : Platinum V
Time  : O(n)
Space : O(L)

풀이:
    deque를 이용한 슬라이딩 윈도우 최솟값.
    단조 증가 덱 유지: 덱 앞이 현재 창의 최솟값 인덱스.
    N이 최대 500만 → sys.stdin + sys.stdout.write 출력 최적화 필수.
"""

import sys
from collections import deque


def solve() -> None:
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    L = int(input_data[idx]); idx += 1
    A = [int(input_data[idx + i]) for i in range(N)]

    dq: deque[int] = deque()  # 인덱스 저장
    result = []

    for i in range(N):
        # 현재 값보다 크거나 같은 덱 뒤 원소 제거 (단조 증가 유지)
        while dq and A[dq[-1]] >= A[i]:
            dq.pop()
        dq.append(i)

        # 창 크기 L 초과한 인덱스 제거
        if dq[0] < i - L + 1:
            dq.popleft()

        result.append(A[dq[0]])

    sys.stdout.write(" ".join(map(str, result)) + "\n")


if __name__ == "__main__":
    solve()
