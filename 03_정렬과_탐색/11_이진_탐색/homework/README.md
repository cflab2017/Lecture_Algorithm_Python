# 11강 과제: 이진 탐색

> O(log n) 탐색을 백준 문제에 적용합니다.

---

## 문제 목록

| # | 문제 | 티어 | 핵심 기술 |
|---|------|------|----------|
| 1 | [백준 1920 – 수 찾기](https://www.acmicpc.net/problem/1920) | Silver IV | 기본 이진 탐색 |
| 2 | [백준 10816 – 숫자 카드 2](https://www.acmicpc.net/problem/10816) | Silver IV | bisect lower/upper bound |
| 3 | [백준 2805 – 나무 자르기](https://www.acmicpc.net/problem/2805) | Silver II | 매개변수 탐색 |

---

## 문제 1: 백준 1920 – 수 찾기 (Silver IV)

### 문제 설명
N개의 정수 집합에서 M개의 쿼리가 존재하는지 각각 판별.

### 제한
- N ≤ 100,000, M ≤ 100,000

### 접근법
- N 개를 정렬 후, M개 쿼리마다 이진 탐색 → O((N+M) log N)
- `bisect_left` 사용 또는 `set` 사용 가능

### 주의사항
- `in` 연산자는 리스트에서 O(n) → 시간 초과
- `set`에서 `in` 은 O(1) → 가장 빠름
- 이진 탐색 연습을 위해 `bisect` 로도 구현해 보세요

---

## 문제 2: 백준 10816 – 숫자 카드 2 (Silver IV)

### 문제 설명
N개의 숫자 카드 중 M개의 숫자가 각각 몇 번 나타나는지 출력.

### 접근법
```python
from bisect import bisect_left, bisect_right
cards.sort()
for q in queries:
    count = bisect_right(cards, q) - bisect_left(cards, q)
```

### 주의사항
- `Counter` 사용도 가능하지만 bisect 연습 권장
- 입출력 최적화 필수 (N, M 각 500,000)

---

## 문제 3: 백준 2805 – 나무 자르기 (Silver II)

### 문제 설명
N개의 나무를 높이 H로 자를 때 M미터 이상 가져가려면 H의 최댓값은?

### 접근법
**매개변수 탐색** (Parametric Search):
- "H로 잘랐을 때 M미터 이상 얻을 수 있는가?"를 결정 함수로
- H의 범위 [0, max(trees)] 에서 이진 탐색

```python
def can_get(trees, h, m):
    return sum(max(0, t - h) for t in trees) >= m

left, right = 0, max(trees)
ans = 0
while left <= right:
    mid = (left + right) // 2
    if can_get(trees, mid, m):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
```

### 주의사항
- 최댓값을 구하므로 조건 만족 시 `ans = mid`, `left = mid + 1`
- 나무 높이 합이 long int 범위이므로 Python은 문제없음

---

## 제출 전 체크리스트

- [ ] 1920: 정렬 후 이진 탐색 또는 set 사용?
- [ ] 10816: bisect_right - bisect_left 로 개수 세기?
- [ ] 2805: 매개변수 탐색 방향(최댓값 탐색)이 맞는가?
- [ ] 모든 문제 sys.stdin 최적화 적용?

---

## 모범 답안

`answer/` 폴더 참조
