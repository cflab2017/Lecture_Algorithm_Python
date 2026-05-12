# 03. 자료형 복잡도 (Data Structure Time Complexities)

## 소개

같은 문제를 풀더라도 **어떤 자료구조를 선택하느냐**에 따라 알고리즘의 성능이
수십~수백 배 달라질 수 있습니다. 예를 들어 `list`에서 첫 번째 원소를 삭제하면 O(n)이지만,
`deque`를 사용하면 O(1)입니다. 파이썬 내장 자료구조의 시간복잡도를 정확히 알아야
최적의 알고리즘을 설계할 수 있습니다.

---

## 학습 목표

1. 파이썬 주요 자료구조(list, dict, set, deque)의 연산별 시간복잡도를 설명할 수 있다.
2. 문제 상황에 맞는 적절한 자료구조를 선택할 수 있다.
3. `list.pop(0)` 대신 `deque.popleft()` 등 올바른 대안을 적용할 수 있다.

---

## 핵심 개념

### 1. list 연산 시간복잡도

| 연산 | 시간복잡도 | 설명 |
|------|------------|------|
| `lst[i]` | O(1) | 인덱스 접근 |
| `lst.append(x)` | O(1) 분할 상환 | 끝에 추가 |
| `lst.pop()` | O(1) 분할 상환 | 끝에서 제거 |
| `lst.insert(0, x)` | O(n) | 앞에 삽입 — 모든 원소 이동 |
| `lst.pop(0)` | O(n) | 앞에서 제거 — 모든 원소 이동 |
| `x in lst` | O(n) | 선형 탐색 |
| `lst.sort()` | O(n log n) | Timsort |
| `len(lst)` | O(1) | 길이 (미리 저장됨) |

> **주의**: `list.pop(0)`을 루프에서 n번 호출하면 O(n²) — BFS 큐로 절대 사용 금지!

### 2. dict / set 연산 시간복잡도

| 자료구조 | 연산 | 시간복잡도 (평균) | 최악 |
|----------|------|-------------------|------|
| `dict` | `d[k]` 조회 | O(1) | O(n) |
| `dict` | `d[k] = v` 삽입 | O(1) | O(n) |
| `dict` | `k in d` | O(1) | O(n) |
| `set` | `x in s` | O(1) | O(n) |
| `set` | `s.add(x)` | O(1) | O(n) |
| `set` | `s.remove(x)` | O(1) | O(n) |

최악의 경우(O(n))는 해시 충돌이 많을 때입니다. 실제로는 거의 O(1)로 동작합니다.

### 3. collections.deque 연산 시간복잡도

| 연산 | 시간복잡도 | list 대비 |
|------|------------|-----------|
| `dq.append(x)` | O(1) | 동일 |
| `dq.appendleft(x)` | O(1) | **list.insert(0,x)는 O(n)** |
| `dq.pop()` | O(1) | 동일 |
| `dq.popleft()` | O(1) | **list.pop(0)은 O(n)** |
| `dq[0]` | O(1) | 동일 |
| `dq[i]` (중간) | O(n) | 동일 |

`deque`는 **양쪽 끝 연산이 O(1)**인 자료구조입니다. BFS 큐로 필수 사용!

### 4. collections.Counter 사용법

```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
cnt = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

print(cnt['apple'])          # 3
print(cnt.most_common(2))    # [('apple', 3), ('banana', 2)]
print(cnt.most_common())     # 빈도 순 전체 목록
```

`Counter`는 내부적으로 `dict`를 사용하므로 조회는 O(1) 평균입니다.

---

## 예제로 보기

### 예제 1: list 연산 시간 측정 (`src/01_list_complexity.py`)

`timeit`으로 `append` vs `insert(0)`, `pop()` vs `pop(0)` 속도를 실측합니다.

```bash
python src/01_list_complexity.py
```

```
[예상 출력]
append (끝에 추가):    0.0012초
insert(0) (앞에 추가): 0.1234초  → 102.8배 느림
pop() (끝 제거):       0.0015초
pop(0) (앞 제거):      0.0987초  →  65.8배 느림
```

### 예제 2: dict / set 연산 (`src/02_dict_set_ops.py`)

`set` vs `list`의 멤버십 테스트 속도, `Counter` 활용 예제를 보여줍니다.

```bash
python src/02_dict_set_ops.py
```

### 예제 3: deque vs list 큐 비교 (`src/03_deque_vs_list.py`)

BFS에서 자주 쓰는 큐 연산의 속도를 실측합니다.

```bash
python src/03_deque_vs_list.py
```

### 예제 4: 자료구조 선택 가이드 (`src/04_choosing_structure.py`)

실제 문제 상황에서 어떤 자료구조를 선택해야 하는지 예제를 통해 설명합니다.

```bash
python src/04_choosing_structure.py
```

---

## 다른 시각으로 보기: 비유 표

| 자료구조 | 실생활 비유 | 특징 |
|----------|-------------|------|
| `list` | 순서가 있는 선반 | 끝에 추가/제거는 빠르지만 앞쪽 조작은 느림 |
| `dict` | 전화번호부 (이름→번호) | 이름으로 바로 찾기 O(1) |
| `set` | 출석부 (있음/없음만) | 포함 여부 확인 O(1), 순서 없음 |
| `deque` | 양방향 줄서기 | 앞뒤 모두 O(1)로 추가/제거 |
| `heapq` | 우선순위 대기표 | 최솟값 꺼내기 O(log n) |

---

## 자주 하는 실수

1. **BFS에서 `list.pop(0)` 사용**
   ```python
   # 잘못된 코드 — O(n²)
   queue = [start]
   while queue:
       node = queue.pop(0)  # O(n)!
       ...
   # 올바른 코드 — O(n log n) → 사실상 O(n)
   from collections import deque
   queue = deque([start])
   while queue:
       node = queue.popleft()  # O(1)
       ...
   ```

2. **`x in list`로 반복 멤버십 검사**
   ```python
   # 잘못된 코드 — O(n²)
   visited = []
   for node in graph:
       if node not in visited:  # O(n) 검사를 n번 → O(n²)
           visited.append(node)
   # 올바른 코드 — O(n)
   visited = set()
   for node in graph:
       if node not in visited:  # O(1) 검사를 n번 → O(n)
           visited.add(node)
   ```

3. **dict 기본값 처리에 KeyError**
   ```python
   # 잘못된 코드
   count = {}
   for x in data:
       count[x] += 1  # 첫 등장 시 KeyError!
   # 올바른 코드
   from collections import defaultdict
   count = defaultdict(int)
   for x in data:
       count[x] += 1  # 기본값 0에서 시작
   # 또는
   count = {}
   for x in data:
       count[x] = count.get(x, 0) + 1
   ```

4. **heapq 최댓값 꺼내기**
   ```python
   import heapq
   # 잘못된 코드 — heapq는 최솟값 힙
   heapq.heappush(heap, x)
   max_val = heapq.heappop(heap)  # 최솟값이 나옴!
   # 올바른 코드 — 음수로 변환
   heapq.heappush(heap, -x)
   max_val = -heapq.heappop(heap)  # 최댓값
   ```

5. **deque의 중간 인덱스 접근**
   ```python
   from collections import deque
   dq = deque([1, 2, 3, 4, 5])
   # dq[0], dq[-1] → O(1) OK
   # dq[2] → O(n) 주의! 중간 원소 접근은 느림
   # 중간 원소를 자주 접근해야 하면 list를 사용하세요.
   ```

---

## 정리

| 상황 | 권장 자료구조 |
|------|---------------|
| 인덱스로 랜덤 접근 필요 | `list` |
| 앞뒤 양방향 추가/제거 (BFS 큐) | `deque` |
| 키-값 매핑 | `dict` |
| 중복 없는 집합 / 빠른 멤버십 검사 | `set` |
| 빈도 세기 | `Counter` |
| 최솟값/최댓값 빠른 접근 | `heapq` |

---

## 직접 해 보기

1. `src/01_list_complexity.py`를 실행하고 `append` vs `insert(0)`의 속도 차이를 기록하세요.
2. 본인의 BFS 코드에서 `list.pop(0)`을 `deque.popleft()`로 바꾸고 속도를 비교하세요.
3. `homework/README.md`의 과제를 완성하세요.

---

## 다음 단원

➡️ [04. 배열과 문자열](../04_배열과_문자열/README.md)

---

## 참고 자료

- [Python 공식 문서 - TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
- [Python collections 문서](https://docs.python.org/3/library/collections.html)
- [백준 1927번 — 최소 힙](https://www.acmicpc.net/problem/1927)
