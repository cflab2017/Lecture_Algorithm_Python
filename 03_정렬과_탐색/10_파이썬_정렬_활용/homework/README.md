# 10강 과제: 파이썬 정렬 활용

> `sorted()`, `key`, 다중 기준 정렬을 실전 문제에 적용합니다.

---

## 문제 목록

| # | 문제 | 티어 | 핵심 기술 |
|---|------|------|----------|
| 1 | [백준 1181 – 단어 정렬](https://www.acmicpc.net/problem/1181) | Silver V | 다중 기준 정렬 + 중복 제거 |
| 2 | [백준 11650 – 좌표 정렬하기](https://www.acmicpc.net/problem/11650) | Silver V | 튜플 정렬 |
| 3 | [백준 18870 – 좌표 압축](https://www.acmicpc.net/problem/18870) | Silver II | 좌표 압축 + 이진 탐색 |

---

## 문제 1: 백준 1181 – 단어 정렬 (Silver V)

### 문제 설명
N개의 단어를 다음 기준으로 정렬:
1. 길이가 짧은 것 먼저
2. 길이가 같으면 사전 순
3. 중복 단어 제거

### 제한
- 1 ≤ N ≤ 20,000

### 접근법
```python
words = set(words)                         # 중복 제거
result = sorted(words, key=lambda w: (len(w), w))
```

### 주의사항
- 입력에서 중복 제거를 먼저 해야 함
- `sorted(set(...))` 으로 한 번에 가능

---

## 문제 2: 백준 11650 – 좌표 정렬하기 (Silver V)

### 문제 설명
2차원 좌표 N개를 x→y 순으로 정렬.

### 접근법
```python
coords = [tuple(map(int, input().split())) for _ in range(n)]
coords.sort()    # 튜플 기본 비교: x 같으면 y 비교
```

### 주의사항
- `sorted()` 또는 `.sort()` 모두 가능
- 튜플 기본 비교가 (x, y) 순서이므로 key 없이 OK

---

## 문제 3: 백준 18870 – 좌표 압축 (Silver II)

### 문제 설명
N개의 수를 상대적 순위(0-indexed)로 변환하여 출력.

예: `[5, 4, 2, 3, 1]` → `[4, 3, 1, 2, 0]`

### 제한
- 1 ≤ N ≤ 1,000,000
- -10⁹ ≤ 수 ≤ 10⁹

### 접근법
```python
# O(n log n)
sorted_unique = sorted(set(arr))
rank = {v: i for i, v in enumerate(sorted_unique)}
result = [rank[v] for v in arr]
```

### 이진 탐색 방법 (bisect)
```python
from bisect import bisect_left
sorted_unique = sorted(set(arr))
result = [bisect_left(sorted_unique, v) for v in arr]
```

### 주의사항
- 중복이 있을 수 있으므로 `set()` 으로 제거 필수
- 1억 이상 큰 값이 있으므로 배열 인덱스로 쓸 수 없음

---

## 제출 전 체크리스트

- [ ] 1181: 중복 단어를 제거했는가?
- [ ] 1181: 길이 같을 때 사전순으로 정렬됐는가?
- [ ] 11650: 입출력 속도 최적화(sys.stdin)를 사용했는가?
- [ ] 18870: N=1,000,000 에서 메모리와 시간이 충분한가?
- [ ] 18870: 중복값을 올바르게 처리했는가?

---

## 모범 답안

`answer/` 폴더 참조
