# 강의 21 과제: DP 심화

## 문제 1: 백준 9251 — LCS (Gold V)

**링크**: https://www.acmicpc.net/problem/9251

### 문제 요약
두 문자열의 LCS 길이를 구하라.

### 핵심 접근법
- 2D DP: dp[i][j] = A[0:i]와 B[0:j]의 LCS 길이
- A[i-1] == B[j-1]: dp[i][j] = dp[i-1][j-1] + 1
- A[i-1] != B[j-1]: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

### 시간/공간 복잡도
- Time: O(n × m), Space: O(n × m)

---

## 문제 2: 백준 11053 — 가장 긴 증가하는 부분 수열 (Silver II)

**링크**: https://www.acmicpc.net/problem/11053

### 핵심 접근법
- O(n²) DP: dp[i] = arr[i]로 끝나는 LIS 길이
- n ≤ 1000이므로 O(n²) 충분

### 시간/공간 복잡도
- Time: O(n²), Space: O(n)

---

## 문제 3: 백준 12865 — 평범한 배낭 (Gold V)

**링크**: https://www.acmicpc.net/problem/12865

### 문제 요약
N개의 물건(무게, 가치)과 배낭 용량 K가 주어질 때 최대 가치를 구하라.

### 핵심 접근법
- 0/1 배낭 1D DP: dp[w] = 용량 w에서 최대 가치
- 역방향 순회로 같은 물건 중복 방지

### 시간/공간 복잡도
- Time: O(N × K), Space: O(K)

---

## 풀이 파일

- `answer/boj_9251.py`
- `answer/boj_11053.py`
- `answer/boj_12865.py`
