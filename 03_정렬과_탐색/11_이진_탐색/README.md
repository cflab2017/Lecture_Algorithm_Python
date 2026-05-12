# 11강: 이진 탐색

> **Part 03 – 정렬과 탐색** | 난이도: ⭐⭐⭐☆☆

---

## 소개: O(log n) vs O(n)

| n | O(n) 연산 수 | O(log n) 연산 수 | 비율 |
|---|------------|----------------|------|
| 1,000 | 1,000 | 10 | 100배 |
| 1,000,000 | 1,000,000 | 20 | 50,000배 |
| 1,000,000,000 | 10억 | 30 | 33,000,000배 |

정렬된 배열에서 선형 탐색(O(n))을 이진 탐색(O(log n))으로 바꾸면
10억 개 데이터도 **30번**의 비교만으로 찾을 수 있습니다.

**전제 조건**: 배열이 **정렬**되어 있어야 합니다.

---

## 학습 목표

1. 이진 탐색 알고리즘을 반복/재귀 두 가지 방법으로 구현한다.
2. `bisect_left`, `bisect_right` 의 차이를 이해하고 lower/upper bound에 활용한다.
3. 이진 탐색으로 구간 내 원소 개수, 최초/최후 등장 위치를 O(log n)에 구한다.

---

## 핵심 개념

### 이진 탐색 알고리즘

```
정렬된 배열: [1, 3, 5, 7, 9, 11, 13, 15]
찾는 값: 7

초기: left=0, right=7
       [1, 3, 5, 7, 9, 11, 13, 15]
        ↑                        ↑
       left                    right

1단계: mid=3, arr[3]=7 → 찾음!
```

### 탐색 공간 절반씩 감소 다이어그램

```
배열 길이 16:

단계 1: ████████ ████████   (16개 → 8개)
단계 2: ████                (8개 → 4개)
단계 3: ██                  (4개 → 2개)
단계 4: █                   (2개 → 1개) ← 최대 4 = log₂16 단계
```

### bisect_left / bisect_right

```python
from bisect import bisect_left, bisect_right

arr = [1, 3, 3, 3, 5, 7]
#      0  1  2  3  4  5

bisect_left(arr, 3)   # → 1  (3이 들어갈 가장 왼쪽 위치)
bisect_right(arr, 3)  # → 4  (3이 들어갈 가장 오른쪽 위치)

# 3의 개수
count = bisect_right(arr, 3) - bisect_left(arr, 3)  # 3
```

```
arr:  [1,  3,  3,  3,  5,  7]
인덱스: 0   1   2   3   4   5
              ↑           ↑
        bisect_left(3)  bisect_right(3)
              = 1              = 4
```

### lower_bound / upper_bound

| 함수 | 의미 | 반환 |
|------|------|------|
| `bisect_left(a, x)` | lower bound | x 이상인 첫 번째 인덱스 |
| `bisect_right(a, x)` | upper bound | x 초과하는 첫 번째 인덱스 |

### off-by-one 주의

```python
# 올바른 반복 이진 탐색
left, right = 0, len(arr) - 1
while left <= right:          # ← <= 이어야 길이 1 배열도 처리
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1        # ← mid+1 (mid 제외)
    else:
        right = mid - 1       # ← mid-1 (mid 제외)
```

---

## 예제로 보기

| 파일 | 내용 |
|------|------|
| `src/01_binary_search_impl.py` | 반복/재귀 이진 탐색 구현 |
| `src/02_bisect_module.py` | bisect_left, bisect_right, insort |
| `src/03_lower_upper_bound.py` | 구간 내 원소 수, lower/upper bound |
| `src/04_binary_search_applications.py` | 최초/최후 등장, 회전 배열 탐색 |

---

## 자주 하는 실수 5가지

1. **`left < right` vs `left <= right` 혼동**
   - `left <= right` : 원소가 1개일 때도 검사 (일반적으로 올바름)
   - `left < right` : 원소가 1개이면 루프 안 들어감 → 찾지 못할 수 있음

2. **`mid = (left + right) // 2` 정수 오버플로우**
   - Python은 임의 정밀도 정수라 오버플로우 없음
   - C/Java에서는 `left + (right - left) // 2` 사용

3. **정렬되지 않은 배열에 이진 탐색 사용**
   - 결과가 틀려도 오류가 나지 않아서 디버그가 어려움
   - 반드시 `assert arr == sorted(arr)` 로 전제 조건 확인

4. **bisect_left 반환값이 배열 범위 밖일 수 있음**
   ```python
   arr = [1, 2, 3]
   idx = bisect_left(arr, 10)   # idx = 3 (len(arr))
   arr[idx]                      # IndexError!
   # 해결: idx < len(arr) 먼저 확인
   ```

5. **찾는 값이 없을 때 처리 누락**
   ```python
   idx = bisect_left(arr, target)
   # idx가 배열 범위 내이고 arr[idx] == target인지 모두 확인
   if idx < len(arr) and arr[idx] == target:
       # 존재함
   ```

---

## 정리

| 목적 | 방법 |
|------|------|
| 값 존재 여부 | `bisect_left` 후 범위·값 확인 |
| 최초 등장 위치 | `bisect_left` |
| 최후 등장 위치 | `bisect_right() - 1` |
| 구간 [a,b] 내 원소 수 | `bisect_right(b) - bisect_left(a)` |
| 정렬 유지 삽입 | `insort_left` / `insort_right` |

---

## 직접 해 보기

1. `[1, 3, 5, 7, 9, 11, 13]` 에서 `7` 을 이진 탐색으로 찾는 과정을 단계별로 써 보세요.
2. `bisect_left([1,3,3,5], 3)` 과 `bisect_right([1,3,3,5], 3)` 값을 직접 계산하세요.
3. 정렬된 배열 `[1, 2, 3, 3, 3, 4, 5]` 에서 `3` 이 몇 개인지 bisect로 구하세요.

---

## 과제

`homework/README.md` 참조

---

## 다음 단원

**12강: 매개변수 탐색** →
이진 탐색의 응용 — "답" 공간에서 이진 탐색
