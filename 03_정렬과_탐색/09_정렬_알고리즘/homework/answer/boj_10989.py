"""
백준 10989 – 수 정렬하기 3
https://www.acmicpc.net/problem/10989
Time  : O(n + k)  k = 10,000
Space : O(k)      카운트 배열만 사용 (메모리 8MB 제한 통과)

제한: N ≤ 10,000,000, 1 ≤ 수 ≤ 10,000
     메모리 8MB → 숫자를 전부 저장하면 초과!
     계수 정렬로 카운트만 저장
"""

import sys


def main() -> None:
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0])

    max_val = 10_001
    count = [0] * max_val

    for i in range(1, n + 1):
        count[int(input_data[i])] += 1

    out = []
    for val in range(1, max_val):
        if count[val]:
            out.append((str(val) + '\n') * count[val])

    sys.stdout.write(''.join(out))


if __name__ == "__main__":
    main()
