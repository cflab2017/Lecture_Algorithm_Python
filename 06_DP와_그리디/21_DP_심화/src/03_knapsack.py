# 주제: 0/1 배낭 문제 (Knapsack)
# Time: O(n × W)   Space: O(n × W) → O(W) 최적화

from typing import NamedTuple


class Item(NamedTuple):
    weight: int
    value: int
    name: str = ""


def knapsack_2d(items: list[Item], capacity: int) -> int:
    """0/1 배낭 2D DP.

    dp[i][w] = 처음 i개 물건을 고려하고, 용량 w 이하로 담을 때 최대 가치

    점화식:
      물건 i를 담지 않으면: dp[i][w] = dp[i-1][w]
      물건 i를 담으면:      dp[i][w] = dp[i-1][w - items[i].weight] + items[i].value
                            (단, items[i].weight ≤ w)

    Time:  O(n × W)
    Space: O(n × W)
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]   # 담지 않음
            if item.weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - item.weight] + item.value)

    return dp[n][capacity]


def knapsack_1d(items: list[Item], capacity: int) -> int:
    """0/1 배낭 1D DP (공간 최적화).

    핵심: w를 역방향(capacity → weight)으로 순회
    → 같은 물건을 두 번 사용하는 것을 방지

    Time:  O(n × W)
    Space: O(W)
    """
    dp = [0] * (capacity + 1)

    for item in items:
        # 역방향! (capacity → item.weight)
        for w in range(capacity, item.weight - 1, -1):
            dp[w] = max(dp[w], dp[w - item.weight] + item.value)

    return dp[capacity]


def knapsack_reconstruct(items: list[Item], capacity: int) -> tuple[int, list[Item]]:
    """0/1 배낭 — 실제 선택한 물건 복원.

    Time:  O(n × W)
    Space: O(n × W)
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if item.weight <= w:
                val = dp[i - 1][w - item.weight] + item.value
                if val > dp[i][w]:
                    dp[i][w] = val

    # 역추적
    selected: list[Item] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(items[i - 1])
            w -= items[i - 1].weight

    return dp[n][capacity], list(reversed(selected))


def unbounded_knapsack(items: list[Item], capacity: int) -> int:
    """무제한 배낭 (각 물건을 여러 번 사용 가능).

    1D DP, 정방향 순회 (역방향이면 0/1 배낭)

    Time:  O(n × W)
    Space: O(W)
    """
    dp = [0] * (capacity + 1)

    for w in range(1, capacity + 1):
        for item in items:
            if item.weight <= w:
                dp[w] = max(dp[w], dp[w - item.weight] + item.value)

    return dp[capacity]


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    items = [
        Item(2, 6, "사과"),
        Item(2, 10, "바나나"),
        Item(3, 12, "포도"),
        Item(1, 4, "딸기"),
        Item(4, 15, "수박"),
    ]
    capacity = 7

    print("=== 배낭 문제 ===")
    print(f"용량: {capacity}")
    print(f"{'물건':>6} | {'무게':>4} | {'가치':>4}")
    print("-" * 22)
    for item in items:
        print(f"{item.name:>6} | {item.weight:>4} | {item.value:>4}")

    ans_2d = knapsack_2d(items, capacity)
    ans_1d = knapsack_1d(items, capacity)
    max_val, selected = knapsack_reconstruct(items, capacity)

    print(f"\n최대 가치 (2D): {ans_2d}")
    print(f"최대 가치 (1D): {ans_1d}")
    print(f"선택한 물건: {[i.name for i in selected]}")
    print(f"총 무게: {sum(i.weight for i in selected)}")
    assert ans_2d == ans_1d == max_val

    print("\n=== 0/1 vs 무제한 배낭 비교 ===")
    simple_items = [Item(1, 1, "A"), Item(2, 4, "B"), Item(3, 5, "C")]
    for cap in range(1, 8):
        v01 = knapsack_1d(simple_items, cap)
        vub = unbounded_knapsack(simple_items, cap)
        print(f"  용량={cap}: 0/1={v01}, 무제한={vub}")

    print("\n=== dp 테이블 시각화 (작은 예시) ===")
    small_items = [Item(2, 6, "A"), Item(2, 10, "B"), Item(3, 12, "C")]
    W = 5
    n = len(small_items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        item = small_items[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if item.weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - item.weight] + item.value)

    header = f"{'물건':>5}" + "".join(f"{j:>5}" for j in range(W + 1))
    print(f"  {header}")
    labels = ["(없음)"] + [f"물건{i}({small_items[i-1].name})" for i in range(1, n+1)]
    for i, row in enumerate(dp):
        print(f"  {labels[i]:>12}" + "".join(f"{v:>5}" for v in row))
