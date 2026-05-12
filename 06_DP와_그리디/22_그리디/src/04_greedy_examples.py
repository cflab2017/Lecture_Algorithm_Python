# 주제: 그리디 예제 모음 — 거스름돈, 최대 곱, 배열 합 최대화
# 다양한 그리디 패턴 연습

import heapq


def min_coins_korean(amount: int) -> int:
    """한국 동전으로 거스름돈 최소 개수 (그리디 최적).

    Time:  O(1) — 동전 종류 고정
    Space: O(1)
    """
    coins = [500, 100, 50, 10, 5, 1]
    count = 0
    for coin in coins:
        count += amount // coin
        amount %= coin
    return count


def max_product_of_two(arr: list[int]) -> int:
    """배열에서 두 수의 최대 곱.

    경우: 가장 큰 두 양수 곱 vs 가장 작은 두 음수 곱 (음수×음수=양수)

    Time:  O(n)
    Space: O(1)
    """
    if len(arr) < 2:
        return 0

    max1 = max2 = float("-inf")   # 가장 큰 두 수
    min1 = min2 = float("inf")    # 가장 작은 두 수 (음수)

    for x in arr:
        if x >= max1:
            max1, max2 = x, max1
        elif x > max2:
            max2 = x

        if x <= min1:
            min1, min2 = x, min1
        elif x < min2:
            min2 = x

    return max(max1 * max2, min1 * min2)


def maximize_array_sum_with_swaps(
    arr: list[int], b: list[int], k: int
) -> int:
    """배열 arr의 합을 최대화 — b의 원소로 k번 교체 가능.

    전략: arr에서 작은 것, b에서 큰 것을 교체

    Time:  O(n log n)
    Space: O(n)
    """
    arr_sorted = sorted(arr)
    b_sorted = sorted(b, reverse=True)

    for i in range(k):
        if arr_sorted[i] < b_sorted[i]:
            arr_sorted[i] = b_sorted[i]
        else:
            break

    return sum(arr_sorted)


def gas_station(gas: list[int], cost: list[int]) -> int:
    """주유소 문제: 한 바퀴 돌 수 있는 출발점 찾기.

    그리디: 총 연료 >= 총 비용이면 반드시 해 존재
    출발점 = 탱크가 음수가 된 직후 다음 지점

    Time:  O(n)
    Space: O(1)
    """
    total_tank = 0
    current_tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_tank += diff
        current_tank += diff

        if current_tank < 0:
            start = i + 1
            current_tank = 0

    return start if total_tank >= 0 else -1


def jump_game(nums: list[int]) -> bool:
    """점프 게임: 첫 위치에서 마지막까지 도달 가능?

    그리디: 현재 도달 가능한 최대 위치를 계속 갱신

    Time:  O(n)
    Space: O(1)
    """
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True


def jump_game_min_jumps(nums: list[int]) -> int:
    """최소 점프 횟수로 마지막까지.

    Time:  O(n)
    Space: O(1)
    """
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break

    return jumps


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== 한국 동전 거스름돈 ===")
    for amt in [4860, 1260, 1000, 5]:
        n = min_coins_korean(amt)
        print(f"  {amt:5d}원 → {n}개")

    print("\n=== 두 수의 최대 곱 ===")
    test_arrs = [
        [1, 5, 3, 2, 4],
        [-10, -3, 5, 2, -1],
        [-5, -4, 1, 2],
        [0, -1, -2, 3],
    ]
    for arr in test_arrs:
        mp = max_product_of_two(arr)
        # 전수 확인
        brute = max(arr[i] * arr[j] for i in range(len(arr)) for j in range(i+1, len(arr)))
        assert mp == brute, f"{arr}: {mp} vs {brute}"
        print(f"  {arr}: 최대 곱 = {mp}")
    print("  모두 전수 검증 통과 ✓")

    print("\n=== 배열 합 최대화 (k번 교체) ===")
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]
    for k in range(6):
        result = maximize_array_sum_with_swaps(a, b, k)
        print(f"  k={k}: {result}")

    print("\n=== 주유소 문제 ===")
    gas_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        ([2, 3, 4], [3, 4, 3]),
    ]
    for g, c in gas_cases:
        start = gas_station(g, c)
        print(f"  gas={g}, cost={c} → 출발점: {start}")

    print("\n=== 점프 게임 ===")
    jump_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 3, 0, 1, 4], True),
    ]
    for nums, expected in jump_cases:
        can = jump_game(nums)
        min_j = jump_game_min_jumps(nums) if can else -1
        print(f"  {nums}: 가능={can} (예상={expected}), 최소점프={min_j}")
