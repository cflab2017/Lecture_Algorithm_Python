# 16강 과제: 위상 정렬

> Kahn's 알고리즘과 우선순위 큐를 활용한 위상 정렬 문제를 풉니다.

---

## 문제 목록

| # | 문제 | 티어 | 핵심 기술 |
|---|------|------|----------|
| 1 | [백준 2252 – 줄 세우기](https://www.acmicpc.net/problem/2252) | Gold III | 기본 위상 정렬 |
| 2 | [백준 1766 – 문제집](https://www.acmicpc.net/problem/1766) | Gold II | heapq + 위상 정렬 |
| 3 | [백준 9205 – 맥주 마시면서 걸어가기](https://www.acmicpc.net/problem/9205) | Silver I | BFS/DFS |

---

## 문제 1: 백준 2252 – 줄 세우기 (Gold III)

### 문제 설명
N명 학생에게 줄 세우는 순서 조건 M개 주어질 때,
가능한 한 가지 줄 순서 출력.

### 접근법
기본 Kahn's 위상 정렬.

```python
in_degree = [0] * (n + 1)
graph[a].append(b)
in_degree[b] += 1
```

### 주의사항
- 여러 가지 답이 가능 → 아무 순서나 출력
- 사이클 없음이 보장됨 (문제 조건)

---

## 문제 2: 백준 1766 – 문제집 (Gold II)

### 문제 설명
N개 문제 중 M개의 선수 조건.
항상 더 쉬운 문제(번호 작은 것) 먼저 풀기.

### 접근법
**heapq + 위상 정렬**:
- deque 대신 최소 힙 사용
- 선수 조건이 모두 완료된 문제 중 번호가 가장 작은 것 먼저

```python
import heapq
heap = [i for i in range(1, n+1) if in_degree[i] == 0]
heapq.heapify(heap)

while heap:
    prob = heapq.heappop(heap)
    result.append(prob)
    for nxt in graph[prob]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heapq.heappush(heap, nxt)
```

---

## 문제 3: 백준 9205 – 맥주 마시면서 걸어가기 (Silver I)

### 문제 설명
집에서 페스티벌까지 가는데,
50미터당 맥주 1병 소비, 한 번에 50병 소지 가능.
편의점을 경유하여 갈 수 있는지 판별.

### 접근법
두 지점 간 맨해튼 거리 ≤ 1000이면 이동 가능.
BFS/DFS로 집 → 페스티벌 도달 가능 여부 판별.

```python
def reachable(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) <= 1000

# 집, 편의점들, 페스티벌을 노드로 구성
# 이동 가능한 간선 생성 후 BFS
```

---

## 제출 전 체크리스트

- [ ] 2252: in-degree 배열 크기 n+1 (1-indexed)?
- [ ] 2252: 모든 M개 조건을 양방향이 아닌 단방향으로 추가?
- [ ] 1766: deque가 아닌 heapq 사용?
- [ ] 1766: 선수 조건 완료 후에만 힙에 삽입?
- [ ] 9205: 맨해튼 거리 ≤ 1000 조건으로 간선 구성?
- [ ] 9205: 테스트 케이스마다 초기화?

---

## 모범 답안

`answer/` 폴더 참조
