# 단원 27 — 실전 패턴 (코딩 테스트 최빈출)

> **Part 08 응용** | 이전: [26_최소_신장_트리](../../07_고급_그래프/26_최소_신장_트리/)

---

## 소개

마지막 단원에서는 코딩 테스트에서 가장 자주 출제되는 **4가지 실전 패턴**을 집중적으로 다룹니다.
개별 알고리즘을 익혔다면 이제 패턴을 조합하여 실전 문제를 빠르게 풀 수 있어야 합니다.

| 패턴 | 핵심 아이디어 | 시간 복잡도 | 대표 문제 |
|------|--------------|------------|-----------|
| 투 포인터 | 두 인덱스를 이동하며 O(n) 탐색 | O(n) | 두 수의 합, 부분 합 |
| 슬라이딩 윈도우 | 고정/가변 창을 이동하며 구간 처리 | O(n) | 최대 합 구간, 최솟값 |
| 비트마스킹 | 정수 비트로 집합/상태 표현 | O(2ⁿ) or O(n) | TSP, 방문 상태 DP |
| 구간 합 | 누적 합으로 구간 쿼리 O(1) | O(n) 전처리 | 구간 합, 2D 구간 합 |

---

## 학습 목표

1. 투 포인터와 슬라이딩 윈도우의 차이점을 구분하고 각각의 템플릿을 외울 수 있다.
2. 비트마스킹으로 부분 집합 열거, DP 방문 상태를 표현하는 코드를 구현할 수 있다.
3. 1D·2D 구간 합 전처리와 O(1) 쿼리를 구현하여 누적 합 문제를 풀 수 있다.

---

## 핵심 개념

### 1. 투 포인터 (Two Pointer)

#### 기본 아이디어
두 인덱스(포인터) `lo`, `hi`를 조건에 따라 이동하여 O(n) 에 탐색.

**반대 방향형** (정렬 배열에서 두 수의 합):
```python
lo, hi = 0, n - 1
while lo < hi:
    s = arr[lo] + arr[hi]
    if s == target:
        # 찾음
    elif s < target:
        lo += 1
    else:
        hi -= 1
```

**같은 방향형** (부분 합 ≥ target):
```python
lo = total = 0
for hi in range(n):
    total += arr[hi]
    while total >= target:
        # [lo, hi] 구간 처리
        total -= arr[lo]
        lo += 1
```

| 항목 | 반대 방향 | 같은 방향 |
|------|-----------|-----------|
| 초기 | lo=0, hi=n-1 | lo=hi=0 |
| 조건 | 정렬 필요 | 양수 값 가정 |
| 이동 | 한 쪽씩 | hi 항상 전진, lo 조건부 전진 |
| 시간 | O(n) | O(n) |

### 2. 슬라이딩 윈도우 (Sliding Window)

#### 고정 크기 창 (길이 k):
```python
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, n):
    window_sum += arr[i] - arr[i - k]  # 오른쪽 추가, 왼쪽 제거
    max_sum = max(max_sum, window_sum)
```

#### 덱(deque)으로 최솟값/최댓값 O(n):
```python
from collections import deque
dq = deque()   # 인덱스 저장 (단조 덱)
for i in range(n):
    while dq and arr[dq[-1]] >= arr[i]:  # 단조 증가 덱
        dq.pop()
    dq.append(i)
    if dq[0] <= i - k:   # 창 밖으로 나간 인덱스 제거
        dq.popleft()
    if i >= k - 1:
        print(arr[dq[0]])  # 창의 최솟값
```

### 3. 비트마스킹 (Bitmask)

#### 주요 비트 연산

| 연산 | 코드 | 의미 |
|------|------|------|
| i번째 비트 ON | `mask \| (1 << i)` | i 포함 |
| i번째 비트 OFF | `mask & ~(1 << i)` | i 제외 |
| i번째 비트 확인 | `mask >> i & 1` | i 포함 여부 |
| 모든 부분집합 | `for s in range(1 << n)` | O(2ⁿ) |
| 최하위 비트 | `mask & (-mask)` | 가장 낮은 1비트 |
| 비트 개수 | `bin(mask).count('1')` | popcount |

#### 방문 상태 DP (TSP):
```python
# dp[mask][v] = mask 집합을 방문하고 v에 있을 때 최소 비용
dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] = 0   # 출발점 0만 방문

for mask in range(1 << n):
    for u in range(n):
        if dp[mask][u] == INF:
            continue
        for v in range(n):
            if mask >> v & 1:  # 이미 방문
                continue
            new_mask = mask | (1 << v)
            dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])
```

### 4. 구간 합 (Prefix Sum)

#### 1D 구간 합 (O(n) 전처리, O(1) 쿼리):
```python
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

# [l, r] 구간 합 (0-indexed)
def query(l, r):
    return prefix[r + 1] - prefix[l]
```

#### 2D 구간 합 (O(nm) 전처리, O(1) 쿼리):
```python
# ps[i][j] = 좌상단 (0,0) ~ (i-1,j-1) 합
ps = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ps[i][j] = (arr[i-1][j-1]
                    + ps[i-1][j] + ps[i][j-1]
                    - ps[i-1][j-1])

# (r1,c1) ~ (r2,c2) 구간 합 (0-indexed 원본)
def query2d(r1, c1, r2, c2):
    return (ps[r2+1][c2+1] - ps[r1][c2+1]
            - ps[r2+1][c1] + ps[r1][c1])
```

**2D 구간 합 시각화:**
```
ps[i][j] 는 포함-배제 원리 적용:
┌─────────────┐
│     A       │  ps[i-1][j]
├────┬────────┤
│ B  │ target │  target = arr[i-1][j-1]
│    │        │
└────┴────────┘
   ps[i][j-1]

ps[i][j] = arr + ps_위 + ps_왼쪽 - ps_대각선위왼쪽
```

---

## 예제로 보기

| 파일 | 내용 | 핵심 개념 |
|------|------|-----------|
| `src/01_two_pointer.py` | 투 포인터 패턴 3종 | 정렬 후 두 수의 합, 부분 합, 중복 제거 |
| `src/02_sliding_window.py` | 슬라이딩 윈도우 | 고정 창 최대 합, 가변 창, deque 최솟값 |
| `src/03_bitmask.py` | 비트마스킹 | 부분 집합 열거, 방문 상태 DP, TSP |
| `src/04_prefix_sum.py` | 구간 합 | 1D/2D 전처리 + O(1) 쿼리 |

```bash
python src/01_two_pointer.py
python src/02_sliding_window.py
python src/03_bitmask.py
python src/04_prefix_sum.py
```

---

## 자주 하는 실수

1. **투 포인터 무한 루프**: `lo < hi` 조건 없이 루프 작성 시 무한 루프.  
   같은 방향형에서는 `hi`가 반드시 전진해야 합니다.

2. **슬라이딩 윈도우 덱 범위 초과**: 덱에서 꺼낸 인덱스가 창 밖인지 확인 후 `popleft()`.  
   `while dq and dq[0] <= i - k: dq.popleft()`

3. **비트마스크 1-indexed 혼동**: 비트마스크는 보통 0-indexed.  
   1-indexed 입력을 받으면 내부에서 `-1` 변환을 통일합니다.

4. **구간 합 off-by-one**: `prefix[r+1] - prefix[l]` vs `prefix[r] - prefix[l-1]`  
   인덱스 시작과 prefix 정의를 통일하세요.

5. **2D 구간 합 포함-배제 부호 오류**: `+ps[r1][c1]` 을 빼는 실수.  
   공식: `ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]`

---

## 정리

```
실전 패턴 요약
━━━━━━━━━━━━━━━━━━━━━
투 포인터      : O(n),  두 인덱스 이동
슬라이딩 윈도우: O(n),  창 이동 + deque O(n) min/max
비트마스킹     : O(2ⁿ), 집합/상태 표현, TSP
구간 합        : O(n) 전처리, O(1) 쿼리, 2D 포함-배제
```

---

## 직접 해 보기

1. 백준 2003 (수들의 합 2)을 투 포인터로 직접 풀어 보세요.
2. 백준 11003 (최솟값 찾기)을 `collections.deque`로 풀어 보세요.
3. 백준 11659 (구간 합 구하기 4)를 전처리 후 O(1) 쿼리로 풀어 보세요.
4. 백준 2098 (외판원 순회)를 비트마스크 DP로 풀어 보세요.

---

## 과제

→ [homework/README.md](homework/README.md)

---

## 다음 단계

축하합니다! **27단원을 모두 완료**했습니다.

이제 아래 단계로 실력을 더욱 높여 보세요:

```
1. 백준 워크북 도전
   - 각 Part별 추천 문제 5개를 반드시 직접 풀기
   - 골드 IV~II 문제를 목표로 업솔빙 진행

2. 프로그래머스 Lv.3 도전
   - 카카오 블라인드, PCCP 기출 문제 풀기

3. 실전 모의 코딩 테스트
   - Codeforces Round (Div.2), Atcoder ABC 참가
   - 시간 제한(2시간) 안에 4문제 풀기 목표

4. 취약 단원 재학습
   - 틀린 유형을 노트에 정리하고 반복 학습
   - 시간 복잡도와 공간 복잡도를 항상 먼저 계산

5. 코드 최적화 연습
   - PyPy 제출 가능 문제는 Python 최적화 먼저
   - sys.stdin.readline, 출력 버퍼링 기법 숙지
```

> **기억하세요**: 알고리즘은 이해 → 구현 → 반복의 사이클로 익혀집니다.
> 한 번 풀었다고 끝이 아니라, 다시 처음부터 구현할 수 있어야 진짜 실력입니다.
