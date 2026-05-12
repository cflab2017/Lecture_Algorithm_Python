# 15강 과제: BFS

> BFS 최단 경로와 다중 시작점을 실전 문제에 적용합니다.

---

## 문제 목록

| # | 문제 | 티어 | 핵심 기술 |
|---|------|------|----------|
| 1 | [백준 1260 – DFS와 BFS](https://www.acmicpc.net/problem/1260) | Silver II | 그래프 BFS |
| 2 | [백준 2178 – 미로 탐색](https://www.acmicpc.net/problem/2178) | Silver I | 격자 BFS 최단 경로 |
| 3 | [백준 7576 – 토마토](https://www.acmicpc.net/problem/7576) | Gold V | 다중 시작점 BFS |

---

## 문제 1: 백준 1260 – DFS와 BFS (Silver II)

이전 과제 (13강)와 동일 문제.
이번에는 BFS 부분에 집중합니다.

### 접근법
```python
from collections import deque

queue = deque([start])
visited[start] = True
while queue:
    node = queue.popleft()
    print(node)
    for nxt in sorted(graph[node]):
        if not visited[nxt]:
            visited[nxt] = True
            queue.append(nxt)
```

---

## 문제 2: 백준 2178 – 미로 탐색 (Silver I)

### 문제 설명
NxM 미로에서 (1,1) → (N,M) 최단 거리 (이동 횟수).
'1' = 지나갈 수 있음, '0' = 벽.

### 입력 형식
```
4 6
101111
101010
111010
000110
```

### 접근법
- BFS로 (0,0) → (N-1,M-1) 최단 거리
- `dist[0][0] = 1` (시작점 포함)

### 주의사항
- 거리를 1부터 시작 (시작점 포함해서 셈)
- 문자열 입력 → 각 문자가 '1'인지 확인

---

## 문제 3: 백준 7576 – 토마토 (Gold V)

### 문제 설명
MxN 상자에서 익은 토마토(1)가 하루에 인접 토마토를 익힘.
모든 토마토가 익는 최소 일수 출력.
불가능이면 -1.

### 접근법
**다중 시작점 BFS**:
```python
queue = deque()
for r in range(n):
    for c in range(m):
        if grid[r][c] == 1:
            queue.append((r, c))
            dist[r][c] = 0
```

### 주의사항
- 0 = 안 익은 토마토, 1 = 익은 토마토, -1 = 빈 칸
- 시작부터 모든 토마토가 익어있으면 0 출력
- 빈 칸(-1)은 탐색하지 않음

---

## 제출 전 체크리스트

- [ ] 1260: 인접 노드 정렬 후 BFS?
- [ ] 2178: dist 초기값 1 (시작점 포함)?
- [ ] 2178: 범위 체크 올바른가?
- [ ] 7576: 다중 시작점 모두 큐에 넣었는가?
- [ ] 7576: 빈 칸(-1) 통과 못하도록 처리?
- [ ] 7576: 시작부터 전부 익은 경우 0 출력?

---

## 모범 답안

`answer/` 폴더 참조
