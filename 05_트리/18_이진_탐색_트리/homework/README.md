# 강의 18 과제: 이진 탐색 트리

## 문제 1: 백준 5639 — 이진 검색 트리 (Gold V)

**링크**: https://www.acmicpc.net/problem/5639

### 문제 요약
BST의 전위 순회(preorder) 결과가 주어질 때, 후위 순회(postorder) 결과를 출력하라.

### 입력 형식
```
50
30
24
5
28
45
98
52
60
```

### 출력 형식
```
5
28
24
45
30
60
52
98
50
```

### 핵심 접근법
전위 순회: `[루트, 왼쪽 서브트리, 오른쪽 서브트리]`

- 첫 번째 값 = 루트
- 나머지에서 루트보다 작은 값들 = 왼쪽 서브트리
- 루트보다 크거나 같은 값들 = 오른쪽 서브트리
- 재귀적으로 후위 순회 계산

### 시간/공간 복잡도
- Time: O(n) — 인덱스 활용 (bisect)
- Space: O(n) — 재귀 스택

### 주의사항
- 입력 끝 처리: `try/except EOFError`
- 재귀 깊이: `sys.setrecursionlimit(20000)`

---

## 문제 2: 백준 2957 — 이진 탐색 트리 (Gold I)

**링크**: https://www.acmicpc.net/problem/2957

### 문제 요약
1~n의 순열로 BST를 순서대로 삽입할 때, 각 수를 삽입 시 비교 횟수(깊이)의 누적 합을 출력하라.

### 입력 형식
```
5
2
4
1
3
5
```

### 출력 형식
```
0
1
3
5
8
```
(삽입 비교 횟수 누적)

### 핵심 접근법
- SortedList(또는 직접 구현) 사용
- 삽입 위치의 전임자(predecessor)와 후임자(successor) 중 더 최근에 삽입된 것의 깊이 + 1
- Python `sortedcontainers.SortedList` 활용

### 시간/공간 복잡도
- Time: O(n log n)
- Space: O(n)

---

## 풀이 파일

- `answer/boj_5639.py`
- `answer/boj_2957.py`
