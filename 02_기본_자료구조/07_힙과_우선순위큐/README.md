# 07. 힙과 우선순위 큐 (Heap & Priority Queue)

## 소개

힙(Heap)은 **"가장 작은(또는 큰) 원소를 O(log n)에 삽입·추출"** 할 수 있는 자료구조입니다.
단순 정렬(O(n log n))로 최솟값을 찾을 수 있지만, 원소가 계속 추가·제거되는 상황에서는 힙이 훨씬 효율적입니다.

**언제 힙을 쓰나요?**
- 스트리밍 데이터에서 Top-K 원소 유지
- 다익스트라 최단 경로 알고리즘
- 허프만 인코딩
- 작업 스케줄링 (우선순위 큐)
- 실시간 중앙값(median) 계산

---

## 학습 목표

1. 힙의 완전 이진 트리 구조와 힙 속성(heap property)을 이해한다.
2. Python `heapq` 모듈의 min-heap을 활용하고, 음수 트릭으로 max-heap을 구현한다.
3. Top-K 패턴과 힙 정렬을 구현하여 O(n log k) 알고리즘을 작성할 수 있다.

---

## 핵심 개념

### 1. 힙 구조 -- 완전 이진 트리

```
         1          <- 루트 (최솟값)
       /   \
      3     2
     / \   / \
    7   5 4   6

배열 표현: [1, 3, 2, 7, 5, 4, 6]
인덱스:     0  1  2  3  4  5  6

부모(i) = (i - 1) // 2
왼쪽(i) = 2 * i + 1
오른쪽(i) = 2 * i + 2
```

**Min-Heap 속성**: 부모 노드의 값 <= 자식 노드의 값

---

### 2. heapq 연산 복잡도

| 연산 | 함수 | 시간 복잡도 | 설명 |
|------|------|------------|------|
| 삽입 | `heappush(h, x)` | O(log n) | 힙에 원소 추가 |
| 최솟값 추출 | `heappop(h)` | O(log n) | 루트 제거 후 재구성 |
| 최솟값 조회 | `h[0]` | O(1) | 제거 없이 루트 확인 |
| 힙 생성 | `heapify(lst)` | O(n) | 리스트를 힙으로 변환 |
| 상위 K개 | `nlargest(k, h)` | O(n log k) | k번째 큰 원소들 |
| 하위 K개 | `nsmallest(k, h)` | O(n log k) | k번째 작은 원소들 |
| push+pop | `heappushpop(h, x)` | O(log n) | push 후 pop (최적화) |

---

### 3. Min-Heap vs Max-Heap

```python
import heapq

# Min-Heap (기본)
min_h = []
heapq.heappush(min_h, 3)
heapq.heappush(min_h, 1)
heapq.heappush(min_h, 2)
print(heapq.heappop(min_h))   # 1 (최솟값)

# Max-Heap -- 음수 변환 트릭
max_h = []
heapq.heappush(max_h, -3)
heapq.heappush(max_h, -1)
heapq.heappush(max_h, -2)
print(-heapq.heappop(max_h))  # 3 (최댓값)
```

---

### 4. Top-K 패턴

```
전체 N개에서 상위 K개만 유지:

방법 1: heapq.nlargest(k, arr) -- O(n log k)
방법 2: 크기 k인 min-heap 유지 -- O(n log k)

크기 k min-heap 유지:
  for num in arr:
      heappush(h, num)
      if len(h) > k:
          heappop(h)    # 가장 작은 것 제거
  -> 힙에 남은 k개가 최대 k개
```

---

## 예제로 보기

| 파일 | 내용 | 핵심 개념 |
|------|------|----------|
| `src/01_min_heap.py` | heapq 기초 push/pop/heapify | min-heap 연산 |
| `src/02_max_heap.py` | 음수 변환으로 max-heap 구현 | 음수 트릭 |
| `src/03_top_k.py` | Top-K 최대/최소 원소 | nlargest, nsmallest |
| `src/04_heap_sort.py` | 힙 정렬 O(n log n) | heapify + heappop |

---

## 자주 하는 실수

### 실수 1: Max-Heap에서 음수 복원 잊음

```python
import heapq

h = []
for v in [3, 1, 4, 1, 5]:
    heapq.heappush(h, -v)

val = heapq.heappop(h)
print(val)    # -5 <- 부호 복원 안 함!
print(-val)   # 5  <- 올바른 최댓값
```

### 실수 2: heappushpop vs heappush+heappop

```python
import heapq

h = [1, 2, 3]
heapq.heapify(h)

# 비효율적 -- O(log n) * 2번
heapq.heappush(h, 0)
heapq.heappop(h)

# 효율적 -- O(log n) 1번 (내부적으로 최적화)
heapq.heappushpop(h, 0)
```

### 실수 3: 힙에서 임의 원소 삭제 불가

```python
import heapq

h = [1, 3, 2, 5, 4]
heapq.heapify(h)
# del h[2]   # 힙 속성 파괴! 직접 삭제 금지
# 대안: lazy deletion (삭제 표시 후 pop 시 건너뜀)
```

### 실수 4: 튜플 힙에서 첫 번째 값이 같을 때 두 번째 값 비교

```python
import heapq

h = []
heapq.heappush(h, (1, "b"))
heapq.heappush(h, (1, "a"))
print(heapq.heappop(h))   # (1, 'a') -- 사전순으로 비교
# 비교 불가한 타입은 (priority, id, obj) 형태로 사용
```

### 실수 5: heapify는 in-place 변환 -- 반환값 없음

```python
import heapq

lst = [3, 1, 4, 1, 5, 9]
h = heapq.heapify(lst)   # None 반환!
print(h)   # None

# 올바른 사용
heapq.heapify(lst)
print(lst[0])   # 1 (최솟값)
```

---

## 정리

| 개념 | 핵심 포인트 |
|------|------------|
| Min-Heap | 루트가 최솟값, Python heapq 기본 |
| Max-Heap | 음수 변환 트릭 (-x push, -pop 반환) |
| heapify | 리스트 -> 힙 O(n), in-place |
| Top-K | nlargest/nsmallest O(n log k) |
| 힙 정렬 | O(n log n), in-place 가능 |

---

## 직접 해 보기

1. `src/01_min_heap.py` 에서 heapify O(n)이 왜 O(n log n)보다 빠른지 확인하세요.
2. `src/03_top_k.py` 에서 스트리밍 방식으로 Top-K를 유지해 보세요.
3. `homework/README.md` 의 과제를 풀어 보세요.

---

## 다음 단원

[08. 연결 리스트](../08_연결_리스트/README.md)
