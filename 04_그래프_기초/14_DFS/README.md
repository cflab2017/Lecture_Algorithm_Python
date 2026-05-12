# 14강: DFS (깊이 우선 탐색)

> **Part 04 – 그래프 기초** | 난이도: ⭐⭐⭐☆☆

---

## 소개: 깊이 우선 탐색

DFS(Depth-First Search)는 현재 노드에서 **갈 수 있는 가장 깊은 곳**까지 먼저
탐색한 뒤 돌아오는 방식입니다.

**활용 분야:**
- 연결 요소(Connected Components) 탐색
- 사이클 탐지
- 백트래킹(완전 탐색)
- 위상 정렬 (DFS 기반)
- 트리 순회

---

## 학습 목표

1. 재귀 DFS와 스택 DFS를 구현하고 방문 순서의 차이를 설명한다.
2. visited 배열을 올바른 시점에 갱신하여 무한 루프를 방지한다.
3. 격자(Grid) DFS로 섬/영역 탐색 문제를 해결한다.

---

## 핵심 개념

### DFS 탐색 순서 다이어그램

```
그래프:
  1 ─── 2 ─── 5
  │     │
  3 ─── 4

DFS(시작=1) 탐색 순서:
  방문: 1 → 2 → 5 (막힘, 역추적) → 4 → 3 (막힘, 역추적)
  결과: [1, 2, 5, 4, 3]

스택 시뮬레이션:
  push(1)
  stack=[1]         → pop=1, 방문[1], push(3,2)
  stack=[3,2]       → pop=2, 방문[2], push(5,4)
  stack=[3,5,4]     → pop=4, 방문[4]
  stack=[3,5]       → pop=5, 방문[5]
  stack=[3]         → pop=3, 방문[3]
  결과: [1,2,4,5,3]  ← 재귀와 순서 다를 수 있음
```

### 재귀 DFS vs 스택 DFS

| 항목 | 재귀 DFS | 스택 DFS |
|------|---------|---------|
| 코드 간결성 | 간결 | 명시적 스택 필요 |
| 스택 오버플로우 | 위험 (깊이 제한) | 없음 |
| 방문 순서 | 인접 리스트 순서 그대로 | 역순으로 push 필요 |
| 실제 문제 | 주로 재귀 사용 | 재귀 불가 시 사용 |

### visited 설정 시점

```python
# 올바른 방법: 방문 처리 후 탐색
def dfs(node):
    visited[node] = True      # ← 여기서
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

# 스택 DFS에서 흔한 실수:
# pop 할 때 visited → 같은 노드 여러 번 push될 수 있음
# push 할 때 visited → 올바름
```

### 시간/공간 복잡도

- 시간: **O(V + E)** — 모든 노드와 간선 한 번씩 방문
- 공간: **O(V)** — visited 배열 + 재귀 스택 (최악 O(V))

---

## 예제로 보기

| 파일 | 내용 |
|------|------|
| `src/01_recursive_dfs.py` | 재귀 DFS 템플릿, 방문 순서 |
| `src/02_stack_dfs.py` | 스택 기반 DFS, 재귀와 비교 |
| `src/03_connected_components.py` | 연결 요소 개수 세기 |
| `src/04_dfs_grid.py` | 격자 DFS, 4방향 이동 |

---

## 자주 하는 실수 5가지

1. **visited 표시를 재귀 호출 후에 하는 실수**
   ```python
   def dfs(node):
       for nxt in graph[node]:
           if not visited[nxt]:
               dfs(nxt)
       visited[node] = True    # ← 잘못됨! 무한 루프 가능
   ```

2. **재귀 깊이 초과 (RecursionError)**
   - 그래프가 선형(체인) 구조면 DFS 깊이 = 노드 수
   - `sys.setrecursionlimit(10**6)` 으로 늘려야 함
   - 또는 스택 기반 DFS로 전환

3. **스택 DFS에서 방문 시점 오류**
   ```python
   # 잘못된 방법: pop 후 visited
   while stack:
       node = stack.pop()
       if visited[node]: continue
       visited[node] = True    # pop 후 방문 처리 (중복 push 발생)
   # 올바른 방법: push 시 visited
   stack.append(start)
   visited[start] = True
   while stack:
       node = stack.pop()
       for nxt in graph[node]:
           if not visited[nxt]:
               visited[nxt] = True
               stack.append(nxt)
   ```

4. **격자 탐색에서 범위 체크 누락**
   ```python
   for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
       nr, nc = r + dr, c + dc
       # 반드시 범위 체크!
       if 0 <= nr < rows and 0 <= nc < cols:
           ...
   ```

5. **비연결 그래프에서 시작점만 탐색**
   - 모든 노드를 커버하려면 전체 노드를 순회하며 미방문 노드에서 DFS 시작
   ```python
   for node in range(1, n + 1):
       if not visited[node]:
           dfs(node)
   ```

---

## 정리

| 목적 | 코드 패턴 |
|------|---------|
| 단순 방문 순서 | 재귀 DFS |
| 연결 요소 개수 | for 루프 + DFS |
| 격자 섬 탐색 | 4방향 DFS |
| 재귀 한계 극복 | 스택 DFS |

---

## 직접 해 보기

1. 5×5 격자에서 `1` 이 연결된 섬의 개수를 DFS로 세어 보세요.
2. 재귀 DFS와 스택 DFS가 같은 방문 순서를 출력하도록 스택 DFS를 수정하세요.
3. 다음 그래프의 DFS 방문 순서를 손으로 계산하세요: `1-2, 1-3, 2-4, 3-4, 4-5`

---

## 과제

`homework/README.md` 참조

---

## 다음 단원

**15강: BFS** → 너비 우선 탐색, 최단 경로, 다중 시작점 BFS
