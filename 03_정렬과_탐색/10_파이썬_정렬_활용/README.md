# 10강: 파이썬 정렬 활용

> **Part 03 – 정렬과 탐색** | 난이도: ⭐⭐☆☆☆

---

## 소개: Timsort

파이썬의 `sorted()` 와 `list.sort()` 는 **Timsort** 알고리즘을 사용합니다.

- 시간 복잡도: **O(n log n)** (최선 O(n) — 이미 정렬된 경우)
- 공간 복잡도: **O(n)**
- **안정 정렬(stable)** 보장
- 실제 데이터에서 매우 빠름 (run 탐지, binary insertion sort 혼합)

코딩 테스트에서는 직접 정렬을 구현할 필요가 거의 없습니다.
**key 파라미터와 람다**를 자유자재로 사용하는 것이 핵심입니다.

---

## 학습 목표

1. `sorted()` 와 `list.sort()` 의 차이를 설명하고 상황에 맞게 선택한다.
2. `key` 파라미터에 `lambda`, `len`, `operator.itemgetter` 등을 활용한다.
3. 다중 기준 정렬, 좌표 압축, Top-K 추출에 정렬을 응용한다.

---

## 핵심 개념

### sorted() vs list.sort()

| 항목 | `sorted(iterable)` | `list.sort()` |
|------|-------------------|--------------|
| 반환값 | 새 리스트 반환 | None 반환 (in-place) |
| 원본 변경 | 변경 안 함 | 변경됨 |
| 입력 타입 | 모든 iterable | 리스트만 |
| 사용 예 | `new = sorted(lst)` | `lst.sort()` |

```python
lst = [3, 1, 2]
new = sorted(lst)   # lst 그대로, new = [1, 2, 3]
lst.sort()          # lst 자체가 [1, 2, 3]
```

### key 파라미터

`key` 는 각 원소에 적용되는 함수로, 비교의 기준이 됩니다.

```python
# 길이 순 정렬
words = ["banana", "apple", "fig"]
sorted(words, key=len)          # ['fig', 'apple', 'banana']

# 절댓값 순 정렬
nums = [-5, 3, -1, 4]
sorted(nums, key=abs)           # [-1, 3, 4, -5]

# lambda: 두 번째 원소 기준
pairs = [(1, 3), (2, 1), (3, 2)]
sorted(pairs, key=lambda x: x[1])  # [(2,1), (3,2), (1,3)]
```

### operator.itemgetter

`lambda x: x[1]` 보다 약간 빠르고 가독성이 좋음.

```python
from operator import itemgetter, attrgetter

data = [("Alice", 85), ("Bob", 92), ("Charlie", 85)]
sorted(data, key=itemgetter(1))              # 점수 기준
sorted(data, key=itemgetter(1, 0))           # 점수, 이름 순
```

### 다중 기준 정렬

튜플 비교는 왼쪽부터 순서대로:

```python
# 점수 내림차순, 같으면 이름 오름차순
students = [("Alice", 85), ("Bob", 92), ("Charlie", 85)]
sorted(students, key=lambda s: (-s[1], s[0]))
# [('Bob', 92), ('Alice', 85), ('Charlie', 85)]
```

### 안정 정렬 보장

파이썬 정렬은 **안정**이므로, 같은 키를 가진 원소는 원래 순서 유지.

```python
data = [("A", 2), ("B", 1), ("C", 2)]
sorted(data, key=lambda x: x[1])
# [('B', 1), ('A', 2), ('C', 2)]  ← A가 C보다 앞
```

### reverse=True

```python
sorted([3, 1, 2], reverse=True)    # [3, 2, 1]
# 주의: key=lambda x: -x 로도 가능하지만 reverse=True 가 더 명확
```

---

## 예제로 보기

| 파일 | 내용 |
|------|------|
| `src/01_sorted_basics.py` | sorted vs sort, 문자열·숫자·객체 |
| `src/02_key_functions.py` | key=lambda, len, itemgetter, 다중 필드 |
| `src/03_multi_key_sort.py` | 이름→나이 등 다중 기준, 튜플 비교 |
| `src/04_sort_applications.py` | 좌표 압축, 중복 제거, Top-K |

---

## 자주 하는 실수 5가지

1. **`sorted()` 의 반환값을 무시하고 원본을 사용**
   ```python
   lst = [3, 1, 2]
   sorted(lst)        # ← 반환값 버림!
   print(lst)         # [3, 1, 2] — 정렬 안 됨
   # 해결: lst = sorted(lst)  또는  lst.sort()
   ```

2. **`list.sort()` 가 None을 반환하는 것을 모름**
   ```python
   result = lst.sort()   # result = None!
   # 해결: lst.sort() 후 lst 사용
   ```

3. **다중 기준 내림차순에서 `reverse=True` 가 모두에 적용됨**
   ```python
   # 점수 내림차순, 이름 오름차순 하고 싶을 때
   # 잘못된 방법:
   sorted(data, key=lambda x: (x[1], x[0]), reverse=True)
   # ← 이름도 내림차순이 됨!
   # 올바른 방법:
   sorted(data, key=lambda x: (-x[1], x[0]))
   ```

4. **문자열과 숫자 혼합 시 TypeError**
   ```python
   # 백준 문자열 정렬에서 숫자를 문자열로 받으면
   lst = ["10", "9", "100"]
   sorted(lst)              # ['10', '100', '9'] — 사전순!
   sorted(lst, key=int)     # ['9', '10', '100'] — 올바른 숫자 순
   ```

5. **key 함수에 side effect 사용**
   - key 함수는 여러 번 호출될 수 있으므로 상태를 변경하면 안 됨
   - 순수 함수(pure function)만 사용할 것

---

## 정리

| 사용 목적 | 권장 방법 |
|----------|----------|
| 단순 오름차순 | `sorted(lst)` |
| 단순 내림차순 | `sorted(lst, reverse=True)` |
| 특정 필드 기준 | `key=lambda x: x[1]` |
| 여러 필드 기준 | `key=lambda x: (x[1], x[0])` |
| 내림차순 포함 다중 | `key=lambda x: (-x[1], x[0])` |
| 튜플 리스트 | `key=itemgetter(1)` |
| 객체 정렬 | `key=attrgetter('score')` |

---

## 직접 해 보기

1. 학생 리스트 `[("홍길동", 85, "A반"), ...]` 를 반, 점수 내림차순, 이름 순으로 정렬해 보세요.
2. `["apple", "Banana", "cherry"]` 를 대소문자 무시하고 정렬하려면?
3. 좌표 압축이 필요한 이유를 설명하고, `[100, 50, 200, 50, 100]` 을 0-indexed 압축하세요.

---

## 과제

`homework/README.md` 참조

---

## 다음 단원

**11강: 이진 탐색** →
정렬된 배열에서 O(log n) 탐색, `bisect` 모듈 완전 정복
