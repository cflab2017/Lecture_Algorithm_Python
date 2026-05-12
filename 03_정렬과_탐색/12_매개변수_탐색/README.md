# 12강: 매개변수 탐색

> **Part 03 – 정렬과 탐색** | 난이도: ⭐⭐⭐☆☆

---

## 소개: "답" 에 이진 탐색을 적용

매개변수 탐색(Parametric Search)은 이진 탐색을 **값** 이 아니라 **답의 공간**에
적용하는 기법입니다.

### 핵심 패턴

> "어떤 값 X가 가능한가?" 를 O(n) 결정 함수로 판단하고,
> X의 범위 [lo, hi] 에서 이진 탐색으로 최적 X를 O(n log(범위)) 에 찾는다.

자주 등장하는 문제 유형:

| 패턴 | 예시 |
|------|------|
| **최솟값의 최댓값** | 공유기를 K대 설치할 때 인접 거리의 최솟값 최대화 |
| **최댓값의 최솟값** | K명에게 나눠줄 때 한 사람의 최대 책임량 최소화 |
| **가능한 최댓값** | 나무를 H로 자를 때 M미터 이상 얻는 H의 최댓값 |

---

## 학습 목표

1. 결정 함수(feasibility function)를 정의하고 단조성을 확인한다.
2. "최솟값의 최댓값" / "최댓값의 최솟값" 패턴 템플릿을 암기한다.
3. 탐색 방향(left vs right 갱신)을 문제 유형에 따라 올바르게 설정한다.

---

## 핵심 개념

### 매개변수 탐색 템플릿

```python
def feasible(mid: int) -> bool:
    # mid 값이 조건을 만족하는가?
    ...

left, right = 최솟값, 최댓값
answer = left     # 또는 right (문제에 따라 초기값 결정)

while left <= right:
    mid = (left + right) // 2
    if feasible(mid):
        answer = mid           # 가능한 값 갱신
        left = mid + 1         # 더 큰 값 시도 (최대화)
        # 또는 right = mid - 1 (최소화)
    else:
        right = mid - 1        # 줄여야 함
        # 또는 left = mid + 1  (늘려야 함)
```

### 결정 함수의 단조성

매개변수 탐색이 가능하려면 결정 함수가 **단조**여야 합니다:

```
최대화 문제 (가능한 최댓값):
X=1: ✅  X=2: ✅  X=3: ✅  X=4: ❌  X=5: ❌
→ 어느 지점 이후 모두 ❌ → 이진 탐색 가능

최소화 문제 (가능한 최솟값):
X=1: ❌  X=2: ❌  X=3: ✅  X=4: ✅  X=5: ✅
→ 어느 지점 이후 모두 ✅ → 이진 탐색 가능
```

### 최댓값의 최솟값 패턴

"K개 그룹으로 나눌 때, 가장 큰 그룹의 크기를 최소화"

```python
def feasible(max_size):
    # max_size 제한으로 K그룹 이하로 나눌 수 있는가?
    groups = 1
    current = 0
    for item in items:
        if current + item > max_size:
            groups += 1
            current = item
        else:
            current += item
    return groups <= K

left, right = max(items), sum(items)
answer = right
while left <= right:
    mid = (left + right) // 2
    if feasible(mid):
        answer = mid      # 최솟값 갱신
        right = mid - 1   # 더 작은 값 시도
    else:
        left = mid + 1
```

### 최솟값의 최댓값 패턴

"K개를 배치할 때, 인접 간격의 최솟값을 최대화"

```python
def feasible(min_dist):
    # min_dist 이상 거리를 두고 K개 배치 가능한가?
    ...

left, right = 1, max_position
answer = 0
while left <= right:
    mid = (left + right) // 2
    if feasible(mid):
        answer = mid      # 최댓값 갱신
        left = mid + 1    # 더 큰 값 시도
    else:
        right = mid - 1
```

---

## 예제로 보기

| 파일 | 내용 |
|------|------|
| `src/01_parametric_template.py` | 범용 매개변수 탐색 템플릿 |
| `src/02_cable_cutting.py` | 케이블/나무 자르기 변형 |
| `src/03_book_pages.py` | K명에게 책 페이지 분배 (최댓값 최소화) |
| `src/04_kth_smallest.py` | 곱셈 테이블에서 k번째 작은 수 |

---

## 자주 하는 실수 5가지

1. **결정 함수의 방향을 반대로 설정**
   - 최대화: 조건 만족 시 `left = mid + 1` (더 큰 값 탐색)
   - 최소화: 조건 만족 시 `right = mid - 1` (더 작은 값 탐색)
   - 반대로 하면 무한루프 또는 잘못된 답

2. **탐색 범위(lo, hi) 설정 오류**
   - lo가 너무 크거나 hi가 너무 작으면 답을 놓침
   - 안전하게: lo = 가능한 최솟값, hi = 가능한 최댓값

3. **결정 함수가 단조가 아닌데 사용**
   - ✅ ❌ ✅ 패턴이면 이진 탐색 불가
   - 문제를 다시 분석해야 함

4. **정수/실수 경계 처리**
   - 정수 탐색: `while left <= right`
   - 실수 탐색: `while right - left > eps` (예: 1e-9)

5. **answer 초기값 미설정**
   - feasible 이 항상 False 인 케이스 처리 누락
   - 항상 answer 초기값을 명시적으로 설정

---

## 정리

| 문제 유형 | 결정 함수 방향 | answer 갱신 |
|----------|-------------|------------|
| 최대화 (가능한 최댓값) | 만족 → left++ | `answer = mid` when feasible |
| 최소화 (가능한 최솟값) | 만족 → right-- | `answer = mid` when feasible |

---

## 직접 해 보기

1. 나무 자르기(백준 2805)를 결정 함수로 풀어 보세요.
2. 공유기 설치(백준 2110)에서 결정 함수의 단조성을 설명하세요.
3. 책 분배 문제에서 K=1, K=n 일 때의 탐색 범위를 계산하세요.

---

## 과제

`homework/README.md` 참조

---

## 다음 단원

**13강: 그래프 표현** → `04_그래프_기초/13_그래프_표현/`
인접 리스트, 인접 행렬, 가중치 그래프 표현 방법
