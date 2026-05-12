# =============================================================================
# 파일명: 04_choosing_structure.py
# 설명  : 상황별 적절한 자료구조 선택 가이드 — 실용 예제
# 시간복잡도: 각 예제별 주석 참고
# 공간복잡도: O(n) — 데이터 크기에 비례
# =============================================================================

import heapq
from collections import deque, Counter, defaultdict


# ---------------------------------------------------------------------------
# 상황 1: 중복 제거 + 빠른 멤버십 검사 → set
# ---------------------------------------------------------------------------
def scenario_dedup_membership() -> None:
    """중복 제거와 멤버십 검사가 필요한 상황. 자료구조: set"""
    print("\n[상황 1] 중복 제거 + 빠른 멤버십 검사 → set")
    print("-" * 50)

    # 방문한 노드 추적 (그래프 탐색)
    visited = set()  # list 대신 set 사용!

    nodes = [1, 3, 2, 5, 3, 2, 7, 1]
    for node in nodes:
        if node not in visited:   # O(1) 평균
            visited.add(node)     # O(1) 평균

    unique = sorted(visited)
    print(f"  입력: {nodes}")
    print(f"  방문 노드 (set): {unique}")
    print(f"  시간복잡도: O(n) — n번 O(1) 연산")

    # 두 집합의 교집합 (공통 원소)
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    print(f"\n  교집합 a & b = {a & b}")
    print(f"  합집합 a | b = {a | b}")
    print(f"  차집합 a - b = {a - b}")


# ---------------------------------------------------------------------------
# 상황 2: 빈도 세기 → Counter / defaultdict
# ---------------------------------------------------------------------------
def scenario_frequency_count() -> None:
    """빈도 세기가 필요한 상황. 자료구조: Counter 또는 defaultdict"""
    print("\n[상황 2] 빈도 세기 → Counter / defaultdict")
    print("-" * 50)

    # 단어 빈도 세기
    text = "the quick brown fox jumps over the lazy dog the fox"
    words = text.split()

    # Counter 사용 — O(n)
    cnt = Counter(words)
    top3 = cnt.most_common(3)
    print(f"  상위 3개 단어: {top3}")

    # defaultdict 사용 — O(n)
    freq = defaultdict(int)
    for w in words:
        freq[w] += 1
    print(f"  'the' 등장 횟수: {freq['the']}")

    # 배열에서 과반수 원소 찾기
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 5, 3, 4, 5]
    num_cnt = Counter(nums)
    most_common = num_cnt.most_common(1)[0]
    print(f"\n  배열에서 가장 많은 수: {most_common[0]} ({most_common[1]}번)")


# ---------------------------------------------------------------------------
# 상황 3: 순서가 중요한 큐 (BFS) → deque
# ---------------------------------------------------------------------------
def scenario_bfs_queue() -> None:
    """BFS 큐가 필요한 상황. 자료구조: deque"""
    print("\n[상황 3] BFS 큐 → deque")
    print("-" * 50)

    # 미로 탐색 예제
    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    # 0: 통과 가능, 1: 벽
    rows, cols = len(maze), len(maze[0])
    start, end = (0, 0), (4, 4)

    def bfs_maze(start: tuple, end: tuple) -> int:
        """BFS로 최단 경로 길이를 반환합니다. O(V)"""
        queue = deque([(start, 0)])  # (위치, 거리)
        visited = {start}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            (r, c), dist = queue.popleft()  # O(1)
            if (r, c) == end:
                return dist
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and maze[nr][nc] == 0
                        and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))
        return -1  # 경로 없음

    dist = bfs_maze(start, end)
    print(f"  시작 {start} → 끝 {end}: 최단 거리 = {dist}")


# ---------------------------------------------------------------------------
# 상황 4: 우선순위 처리 → heapq
# ---------------------------------------------------------------------------
def scenario_priority_queue() -> None:
    """우선순위 큐가 필요한 상황. 자료구조: heapq"""
    print("\n[상황 4] 우선순위 큐 → heapq")
    print("-" * 50)

    # 최솟값 힙 (min-heap)
    heap = []
    tasks = [(3, '보고서 작성'), (1, '긴급 전화'), (2, '회의 준비')]

    for priority, task in tasks:
        heapq.heappush(heap, (priority, task))  # O(log n)

    print("  작업 처리 순서 (우선순위 낮을수록 먼저):")
    while heap:
        p, t = heapq.heappop(heap)  # O(log n)
        print(f"    우선순위 {p}: {t}")

    # 최댓값 힙 — 음수 변환 트릭
    max_heap = []
    scores = [85, 92, 78, 95, 88]
    for s in scores:
        heapq.heappush(max_heap, -s)  # 음수로 저장

    print(f"\n  점수 목록: {scores}")
    print(f"  최고 점수 3개: ", end="")
    top3 = []
    for _ in range(3):
        top3.append(-heapq.heappop(max_heap))
    print(top3)


# ---------------------------------------------------------------------------
# 상황 5: 키-값 매핑 → dict
# ---------------------------------------------------------------------------
def scenario_mapping() -> None:
    """키-값 매핑이 필요한 상황. 자료구조: dict"""
    print("\n[상황 5] 키-값 매핑 → dict")
    print("-" * 50)

    # 학생 성적 관리
    grades = {'Alice': 95, 'Bob': 82, 'Charlie': 90}

    # 두 합이 target이 되는 쌍 찾기 (Two Sum 문제)
    def two_sum(nums: list, target: int):
        """O(n) 해법 — dict로 보완값 저장"""
        seen = {}  # {값: 인덱스}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:   # O(1) 조회
                return (seen[complement], i)
            seen[num] = i
        return None

    nums = [2, 7, 11, 15]
    result = two_sum(nums, 9)
    print(f"  Two Sum [2,7,11,15], target=9: 인덱스 {result}")
    print(f"  시간복잡도: O(n) — dict 덕분에 O(n²) → O(n)")


def main():
    print("=" * 55)
    print("  상황별 자료구조 선택 가이드")
    print("=" * 55)

    scenario_dedup_membership()
    scenario_frequency_count()
    scenario_bfs_queue()
    scenario_priority_queue()
    scenario_mapping()

    print("\n" + "=" * 55)
    print("  자료구조 선택 요약")
    print("=" * 55)
    print("  중복 제거 / 멤버십 검사 → set      O(1)")
    print("  빈도 세기               → Counter  O(n)")
    print("  BFS 큐 (양방향)         → deque    O(1) 양끝")
    print("  우선순위 처리           → heapq    O(log n)")
    print("  키-값 매핑              → dict     O(1)")
    print("  인덱스 접근 / 슬라이싱 → list     O(1) / O(k)")


if __name__ == "__main__":
    main()
