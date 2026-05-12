# 12강 과제: 매개변수 탐색

> 결정 함수와 이진 탐색을 결합해 최적화 문제를 풉니다.

---

## 문제 목록

| # | 문제 | 티어 | 핵심 기술 |
|---|------|------|----------|
| 1 | [백준 2805 – 나무 자르기](https://www.acmicpc.net/problem/2805) | Silver II | 최댓값 탐색 |
| 2 | [백준 2110 – 공유기 설치](https://www.acmicpc.net/problem/2110) | Gold IV | 최솟값의 최댓값 |

---

## 문제 1: 백준 2805 – 나무 자르기 (Silver II)

### 문제 설명
N개의 나무를 높이 H로 자를 때 M미터 이상 가져가려면 H의 최댓값은?

### 결정 함수 설계
```
feasible(H): H로 잘랐을 때 M미터 이상 수집 가능한가?
  = sum(max(0, tree - H) for tree in trees) >= M
```

### 단조성 확인
```
H가 클수록 수집량이 줄어든다
H=0: 전부 수집 (항상 ✅)
H=max: 수집 없음 (항상 ❌ if M > 0)
```

### 탐색 방향
```python
if feasible(mid):
    answer = mid
    left = mid + 1   # H를 높여 봄 (최댓값 탐색)
else:
    right = mid - 1  # H를 낮춰야 함
```

### 주의사항
- H=0 도 탐색 범위에 포함 (left=0)
- 수집량 계산 시 overflow 없음 (Python)

---

## 문제 2: 백준 2110 – 공유기 설치 (Gold IV)

### 문제 설명
N개의 집 중 C개에 공유기를 설치할 때,
인접한 공유기 사이 거리의 **최솟값**을 최대화.

### 결정 함수 설계
```
feasible(d): 최소 거리 d 이상 유지하며 C개 설치 가능한가?
  - 집을 정렬 후, 그리디하게 설치
  - 마지막 설치 위치로부터 d 이상 떨어진 첫 집에 설치
```

### 탐색 방향
```python
# 최솟값의 최댓값 → 최대화 탐색
if feasible(mid):
    answer = mid
    left = mid + 1   # 거리를 더 벌려 봄
else:
    right = mid - 1  # 거리를 줄여야 함
```

### 탐색 범위
- lo = 1 (최소 인접 거리)
- hi = 마지막 집 - 첫 번째 집 (정렬 후)

### 그리디 결정 함수 구현
```python
def feasible(d: int) -> bool:
    count = 1
    last = houses[0]  # 첫 집에 무조건 설치
    for h in houses[1:]:
        if h - last >= d:
            count += 1
            last = h
    return count >= c
```

---

## 공통 주의사항

- [ ] 탐색 범위를 충분히 크게 설정했는가?
- [ ] 결정 함수의 단조성을 확인했는가?
- [ ] 최댓값/최솟값 탐색 방향이 올바른가?
- [ ] answer 초기값을 설정했는가?
- [ ] 입출력 최적화(sys.stdin)를 사용했는가?

---

## 모범 답안

`answer/` 폴더 참조
