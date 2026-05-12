# 강의 20 과제: DP 기초

## 문제 1: 백준 2579 — 계단 오르기 (Silver III)

**링크**: https://www.acmicpc.net/problem/2579

### 문제 요약
계단마다 점수가 있을 때, 최대 점수를 구하라.  
규칙: 연속으로 3칸 연속 밟으면 안 됨, 마지막 계단은 반드시 밟아야 함.

### 점화식
```
dp[i][0] = i번째를 혼자(i-2에서 점프) 밟았을 때 최대
dp[i][1] = i번째를 연속으로(i-1에서 왔을 때) 밟았을 때 최대

dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + score[i]
dp[i][1] = dp[i-1][0] + score[i]
```

### 시간/공간 복잡도
- Time: O(n), Space: O(n) → O(1) 최적화 가능

---

## 문제 2: 백준 1463 — 1로 만들기 (Silver III)

**링크**: https://www.acmicpc.net/problem/1463

### 문제 요약
정수 n을 다음 세 연산으로 1로 만들 때 최소 연산 횟수:
1. n이 3으로 나누어지면 3으로 나눔
2. n이 2로 나누어지면 2로 나눔
3. 1 뺌

### 점화식
```
dp[i] = i를 1로 만드는 최소 연산 수
dp[1] = 0
dp[i] = dp[i-1] + 1
dp[i] = min(dp[i], dp[i//2] + 1)  if i % 2 == 0
dp[i] = min(dp[i], dp[i//3] + 1)  if i % 3 == 0
```

### 시간/공간 복잡도
- Time: O(n), Space: O(n)

---

## 문제 3: 백준 11726 — 2×n 타일링 (Silver III)

**링크**: https://www.acmicpc.net/problem/11726

### 문제 요약
2×n 직사각형을 1×2, 2×1 타일로 채우는 방법 수를 10007로 나눈 나머지.

### 점화식
```
dp[i] = 2×i 직사각형 채우는 방법 수
dp[1] = 1  (세로 1개)
dp[2] = 2  (세로 2개 or 가로 2개)
dp[i] = dp[i-1] + dp[i-2]  (mod 10007)
```

### 시간/공간 복잡도
- Time: O(n), Space: O(n)

---

## 풀이 파일

- `answer/boj_2579.py`
- `answer/boj_1463.py`
- `answer/boj_11726.py`
