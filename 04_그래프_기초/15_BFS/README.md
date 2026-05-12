# 15강: BFS (너비 우선 탐색)

> **Part 04 – 그래프 기초** | 난이도: ⭐⭐⭐☆☆

---

## 소개: 최단 경로를 보장하는 탐색

BFS(Breadth-First Search)는 시작점에서 **가까운 노드부터** 탐색합니다.
가중치 없는 그래프에서 **최단 경로**를 보장하는 유일한 간단한 알고리즘입니다.

**DFS vs BFS 언제 쓸까?**

| 목적 | 추천 |
|------|------|
| 최단 경로 (가중치 없음) | **BFS** |
| 연결 요소 / 백트래킹 | DFS |
| 재귀 구현 편의 | DFS |
| 레이어별 탐색 필요 | **BFS** |

---

## 학습 목표

1. `collections.deque` 를 이용한 BFS를 구현한다.
2. 거리 배열(dist[])로 최단 거리를 기록하고 경로를 재구성한다.
3. 다중 시작점 BFS와 격자 BFS를 구현한다.

---

## 핵심 개념

### BFS 레이어별 탐색

```
그래프:
  1 ─── 2 ─── 5
  │     │
  3 ─── 4

BFS(시작=1) 탐색 순서:
  레이어 0: [1]           거리 0
  레이어 1: [2, 3]        거리 1
  레이어 2: [5, 4]        거리 2

deque 상태:
  [1]       → pop=1, push(2,3)
  [2,3]     → pop=2, push(5,4)
  [3,5,4]   → pop=3, (이미 4 있음)
  [5,4]     → pop=5
  [4]       → pop=4
```

### BFS 최단 거리 다이어그램

```
격자 미로 (0=길, 1=벽, S=시작, E=끝):
  S 0 1 0 0
  0 0 1 0 1
  1 0 0 0 0
  0 1 0 1 0
  0 0 0 0 E

최단 거리:
   0  1  ∞  6  7
   1  2  ∞  5  ∞
  ∞  3  4  4  5  (벽 제외)
   ∞  ∞  5  ∞  6
   ...    ...  8

최단 거리 = 8
```

### visited vs dist 배열

```python
# 방법 1: visited 배열
visited[node] = True   # 방문 여부만

# 방법 2: dist 배열 (거리 기록 + 방문 여부 겸용)
dist = [-1] * (n + 1)
dist[start] = 0
if dist[nxt] == -1:    # -1 = 미방문
    dist[nxt] = dist[node] + 1
```

### 시간/공간 복잡도

- 시간: **O(V + E)**
- 공간: **O(V)** — 큐 + visited 배열

---

## 예제로 보기

| 파일 | 내용 |
|------|------|
| `src/01_bfs_basic.py` | BFS 기본 템플릿, 탐색 순서와 거리 |
| `src/02_bfs_shortest_path.py` | 최단 경로 dist 배열, 경로 재구성 |
| `src/03_bfs_grid.py` | 격자 BFS: 미로 최단 경로 |
| `src/04_bfs_multi_source.py` | 다중 시작점 BFS |

---

## 자주 하는 실수 5가지

1. **visited를 큐에서 꺼낼 때(dequeue) 설정하는 실수**
   ```python
   # 잘못된 방법: pop 후 visited
   while queue:
       node = queue.popleft()
       if visited[node]: continue
       visited[node] = True
       # → 같은 노드가 큐에 여러 번 들어갈 수 있음

   # 올바른 방법: push 시 visited
   queue.append(start)
   visited[start] = True
   while queue:
       node = queue.popleft()
       for nxt in graph[node]:
           if not visited[nxt]:
               visited[nxt] = True
               queue.append(nxt)
   ```

2. **`list.pop(0)` 사용 (O(n) 연산)**
   - 리스트는 앞에서 빼면 O(n) → 큐 전체가 O(n²)
   - 반드시 `collections.deque` 의 `popleft()` 사용

3. **격자 범위 체크 누락**
   - `nr, nc = r + dr, c + dc` 후 항상 범위 체크

4. **시작점 거리를 0이 아닌 1로 초기화**
   - 시작점은 이미 있는 곳이므로 거리 0
   - `dist[start] = 0`

5. **다중 시작점 BFS에서 모든 시작점을 큐에 넣지 않음**
   ```python
   # 잘못: 시작점 하나씩 별도 BFS
   # 올바른: 처음부터 모든 시작점을 큐에 넣기
   queue = deque()
   for src in sources:
       queue.append(src)
       dist[src] = 0
   ```

---

## 정리

| 목적 | BFS 패턴 |
|------|---------|
| 단순 방문 순서 | deque + visited |
| 최단 거리 | deque + dist[] |
| 격자 탐색 | 4방향 + 범위 체크 |
| 다중 시작점 | 초기 큐에 모두 삽입 |
| 레이어 구분 | 큐 크기로 레이어 경계 |

---

## 직접 해 보기

1. 5×5 미로에서 BFS로 최단 거리를 구하고 경로를 역추적해 보세요.
2. 다중 시작점 BFS로 "여러 불씨에서 번지는 불"을 시뮬레이션하세요.
3. BFS를 이용해 이분 그래프 여부를 판별하는 코드를 작성하세요.

---

## 과제

`homework/README.md` 참조

---

## 다음 단원

**16강: 위상 정렬** → DAG에서 선후 관계 순서 결정, Kahn's 알고리즘
