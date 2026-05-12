# 백준 1744 — 수 묶기
# https://www.acmicpc.net/problem/1744
# Time: O(n log n)  Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    positives = sorted([x for x in nums if x > 1], reverse=True)
    ones = nums.count(1)
    negatives = sorted([x for x in nums if x < 0])
    zeros = nums.count(0)

    total = 0

    # 양수: 큰 것끼리 2개씩 곱하기
    i = 0
    while i + 1 < len(positives):
        total += positives[i] * positives[i + 1]
        i += 2
    if i < len(positives):
        total += positives[i]

    # 1: 그냥 더하기
    total += ones

    # 음수: 작은 것(절댓값 큰)끼리 2개씩 곱하기
    i = 0
    while i + 1 < len(negatives):
        total += negatives[i] * negatives[i + 1]
        i += 2
    if i < len(negatives):
        # 홀수 개 음수 → 0이 있으면 곱해서 소거, 없으면 그냥 더함
        if zeros == 0:
            total += negatives[i]
        # zeros > 0이면 0과 묶어서 0이 됨 (더하지 않음)

    print(total)


solve()
