# 09강 과제: 정렬 알고리즘

> 이론으로 배운 정렬을 백준 문제에 직접 적용해 봅니다.

---

## 문제 목록

| # | 문제 | 티어 | 핵심 기술 |
|---|------|------|----------|
| 1 | [백준 2750 – 수 정렬하기](https://www.acmicpc.net/problem/2750) | Bronze II | 버블 정렬 직접 구현 |
| 2 | [백준 2751 – 수 정렬하기 2](https://www.acmicpc.net/problem/2751) | Silver V | 병합 정렬 or sys.stdin 최적화 |
| 3 | [백준 10989 – 수 정렬하기 3](https://www.acmicpc.net/problem/10989) | Silver V | 계수 정렬 (메모리 제한 8MB) |

---

## 문제 1: 백준 2750 – 수 정렬하기 (Bronze II)

### 문제 설명
N개의 수가 주어질 때, 오름차순으로 정렬하여 출력.

### 제한
- 1 ≤ N ≤ 1,000
- -1,000 ≤ 수 ≤ 1,000

### 접근법
N이 최대 1,000이므로 O(n²) 버블 정렬로도 충분합니다.
직접 구현해서 알고리즘 원리를 복습해 보세요.

### 풀이 힌트
```python
# 버블 정렬 기본 구조
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

---

## 문제 2: 백준 2751 – 수 정렬하기 2 (Silver V)

### 문제 설명
N개의 수를 오름차순으로 정렬.

### 제한
- 1 ≤ N ≤ 1,000,000
- -1,000,000 ≤ 수 ≤ 1,000,000

### 접근법
N = 10⁶이므로 O(n²) 정렬은 시간 초과.
O(n log n)이 필요합니다.

옵션 A: 병합 정렬 직접 구현
옵션 B: `sys.stdin` + `sorted()` 사용

### 주의사항
- 입력이 많을 때 `input()` 은 매우 느림 → `sys.stdin` 사용
- `print()` 를 100만 번 호출하면 느림 → `'\n'.join()` 사용

```python
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
print('\n'.join(map(str, arr)))
```

---

## 문제 3: 백준 10989 – 수 정렬하기 3 (Silver V)

### 문제 설명
N개의 수를 오름차순으로 정렬.

### 제한
- 1 ≤ N ≤ 10,000,000 (천만!)
- 1 ≤ 수 ≤ 10,000
- **메모리 제한: 8MB**

### 접근법
메모리가 8MB밖에 없어서 숫자를 배열에 전부 저장할 수 없습니다!
- int 하나 = 약 28 bytes (CPython)
- 천만 개 × 28 bytes ≈ 280MB → 초과

**계수 정렬** 사용:
- 카운트 배열 크기: 10,001 × 4 bytes ≈ 40KB → 문제없음
- 각 숫자의 등장 횟수만 세면 됨

```python
# 핵심 아이디어
count = [0] * 10001
for _ in range(n):
    count[int(sys.stdin.readline())] += 1

result = []
for val, cnt in enumerate(count):
    result.extend([str(val)] * cnt)
print('\n'.join(result))
```

---

## 제출 전 체크리스트

- [ ] 2750: 버블 정렬로 직접 구현했는가?
- [ ] 2751: sys.stdin 사용으로 입력 속도를 높였는가?
- [ ] 10989: 메모리 8MB 제한 내에서 계수 정렬을 사용했는가?
- [ ] 모든 문제에서 엣지 케이스(N=1, 중복 값) 테스트했는가?

---

## 모범 답안

`answer/` 폴더 참조

| 파일 | 설명 |
|------|------|
| `boj_2750.py` | 버블 정렬 구현 |
| `boj_2751.py` | 병합 정렬 or 빠른 입출력 |
| `boj_10989.py` | 계수 정렬 |
