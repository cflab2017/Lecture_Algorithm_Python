# 06. 해시 (Hash Table)

## 소개

해시 테이블(Hash Table)은 **평균 O(1)** 에 삽입·삭제·검색이 가능한 자료구조입니다.
"O(1) 룩업의 마법"이라 불리며, 이진 탐색(O(log n))이나 선형 탐색(O(n))으로는 불가능한 성능을 제공합니다.

Python에서는 `dict`, `set`, `Counter`, `defaultdict`가 해시 기반으로 구현되어 있습니다.

```
키(key) "apple"  ->  해시 함수  ->  인덱스 3
                                      |
버킷:  [0][ ] [1][ ] [2][ ] [3]["apple":5] [4][ ] ...
                                      ^
                               O(1)에 접근!
```

**경쟁 프로그래밍에서 해시를 쓰는 이유:**
- 빈도 계산: 문자·단어 등장 횟수 O(n)
- 중복 확인: O(1) 멤버십 테스트
- 그룹화: 공통 키를 가진 원소 묶기
- Two-Sum 패턴: O(n^2) -> O(n)으로 개선

---

## 학습 목표

1. Python `dict`와 `set`의 평균 O(1) 연산을 이해하고 올바르게 활용한다.
2. `Counter`와 `defaultdict`를 사용해 빈도 계산 및 그룹화 문제를 효율적으로 해결한다.
3. 해시 충돌 개념을 이해하고, 최악 케이스 O(n)이 발생하는 상황을 인지한다.

---

## 핵심 개념

### 1. dict 연산 복잡도

| 연산 | 평균 | 최악 | 설명 |
|------|------|------|------|
| `d[key]` | O(1) | O(n) | 조회 |
| `d[key] = val` | O(1) | O(n) | 삽입/수정 |
| `del d[key]` | O(1) | O(n) | 삭제 |
| `key in d` | O(1) | O(n) | 멤버십 |
| `len(d)` | O(1) | -- | 크기 |
| `d.keys()` | O(1) | -- | 뷰 반환 |
| `list(d.keys())` | O(n) | -- | 리스트 변환 |

> **최악 O(n)**: 해시 충돌이 연쇄될 때 발생. 실전에서는 거의 드뭄.

---

### 2. 해시 충돌 (Hash Collision)

```
"apple" -> hash -> 3
"grape" -> hash -> 3  <- 충돌!

해결 방법:
  1. 체이닝(Chaining): 같은 버킷에 링크드 리스트 연결
  2. 개방 주소법(Open Addressing): 다른 빈 버킷을 탐색

Python dict는 개방 주소법(Open Addressing)을 사용.
```

---

### 3. set 연산

| 연산 | 시간 복잡도 | 예시 |
|------|------------|------|
| `x in s` | O(1) 평균 | 멤버십 테스트 |
| `s.add(x)` | O(1) 평균 | 추가 |
| `s.remove(x)` | O(1) 평균 | 제거 (없으면 KeyError) |
| `s.discard(x)` | O(1) 평균 | 제거 (없어도 OK) |
| `s | t` (합집합) | O(len(s)+len(t)) | 합집합 |
| `s & t` (교집합) | O(min(len(s),len(t))) | 교집합 |
| `s - t` (차집합) | O(len(s)) | 차집합 |
| `s ^ t` (대칭차) | O(len(s)+len(t)) | 대칭차집합 |

---

### 4. Counter

```python
from collections import Counter

c = Counter("aabbbcccc")
# Counter({'c': 4, 'b': 3, 'a': 2})

c.most_common(2)   # [('c', 4), ('b', 3)]  -- 상위 2개

# Counter 산술
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
c1 + c2   # Counter({'a': 4, 'b': 3})
c1 - c2   # Counter({'a': 2})  -- 양수만 유지
c1 & c2   # Counter({'a': 1, 'b': 1})  -- min
c1 | c2   # Counter({'a': 3, 'b': 2})  -- max
```

---

### 5. defaultdict

```python
from collections import defaultdict

# 일반 dict: KeyError 발생
d = {}
d["missing"] += 1   # KeyError!

# defaultdict: 기본값 자동 생성
d = defaultdict(int)
d["missing"] += 1   # 0 + 1 = 1, OK

# 자주 쓰는 패턴
graph  = defaultdict(list)   # 인접 리스트
cnt    = defaultdict(int)    # 빈도 계산
groups = defaultdict(list)   # 그룹화
```

---

## 예제로 보기

| 파일 | 내용 | 핵심 개념 |
|------|------|----------|
| `src/01_dict_basics.py` | dict CRUD, get(), 순회 | 기본 연산 |
| `src/02_set_operations.py` | 집합 연산, frozenset | 멤버십, 집합 |
| `src/03_counter_usage.py` | Counter 빈도 분석 | most_common, 산술 |
| `src/04_hash_applications.py` | Two-Sum, 애너그램 그룹 | 실전 패턴 |

---

## 자주 하는 실수

### 실수 1: 변경 가능한(mutable) 객체를 키로 사용

```python
# 잘못된 예 -- list는 해시 불가
d = {}
d[[1, 2, 3]] = "value"   # TypeError: unhashable type: 'list'

# 올바른 예 -- tuple 사용
d[(1, 2, 3)] = "value"   # OK
```

### 실수 2: defaultdict와 일반 dict 혼동

```python
from collections import defaultdict

# defaultdict는 없는 키에 기본값 제공
d = defaultdict(int)
print(d["없는키"])   # 0 (새 키가 생성됨!)
print(list(d.keys()))   # ['없는키'] <- 주의!

# 단순 조회에는 .get() 사용 권장
d2 = {}
print(d2.get("없는키", 0))   # 0 (키 생성 안 함)
```

### 실수 3: dict 순회 중 수정

```python
d = {"a": 1, "b": 2, "c": 3}
# 잘못된 예 -- RuntimeError!
for key in d:
    if d[key] == 2:
        del d[key]

# 올바른 예 -- 복사본으로 순회
for key in list(d.keys()):
    if d[key] == 2:
        del d[key]
```

### 실수 4: set은 순서가 없음

```python
s = {3, 1, 2}
print(list(s))   # [1, 2, 3] 또는 다른 순서 (비결정적)

# 정렬이 필요하면 sorted()
print(sorted(s))   # [1, 2, 3] 항상 정렬됨
```

### 실수 5: Counter 뺄셈에서 음수 제외

```python
from collections import Counter

c1 = Counter(a=2, b=3)
c2 = Counter(a=5, b=1)
result = c1 - c2
print(result)   # Counter({'b': 2}) -- 음수 결과는 제외!

# 음수 포함하려면 subtract 사용
c1.subtract(c2)
print(c1)   # Counter({'b': 2, 'a': -3})
```

---

## 정리

| 개념 | 핵심 포인트 |
|------|------------|
| dict | 평균 O(1) CRUD, 키는 해시 가능해야 함 |
| set | 평균 O(1) 멤버십, 중복 제거 |
| Counter | 빈도 계산, most_common, 산술 연산 |
| defaultdict | 기본값 자동 생성, 그룹화에 유용 |
| 해시 충돌 | 최악 O(n), 실전에서는 거의 평균 O(1) |

---

## 직접 해 보기

1. `src/04_hash_applications.py` 에서 Two-Sum 을 brute force O(n^2) 로도 구현해 보고 속도를 비교하세요.
2. `src/03_counter_usage.py` 에서 Counter 대신 직접 딕셔너리로 구현해 보세요.
3. `homework/README.md` 의 과제를 풀어 보세요.

---

## 다음 단원

[07. 힙과 우선순위 큐](../07_힙과_우선순위큐/README.md)
