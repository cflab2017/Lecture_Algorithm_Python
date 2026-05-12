# Topic : 괄호 매칭 -- (), [], {}
# Time  : O(n) -- 문자열 길이 n
# Space : O(n) -- 최악의 경우 스택에 n/2개 저장


def is_valid_brackets(s: str) -> bool:
    """괄호 문자열이 유효한지 검사한다.

    알고리즘:
      - 여는 괄호 ( [ { 는 스택에 push
      - 닫는 괄호 ) ] } 가 나오면:
          1. 스택이 비어있으면 -> False (매칭 짝 없음)
          2. 스택 top과 짝이 맞지 않으면 -> False
          3. 맞으면 stack.pop()
      - 모든 처리 후 스택이 비어있으면 -> True
    """
    match = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def bracket_balance_detail(s: str) -> str:
    """유효하지 않은 경우 어떤 문제인지 설명을 반환."""
    match = {")": "(", "]": "[", "}": "{"}
    stack: list[tuple[str, int]] = []   # (괄호, 인덱스)

    for i, ch in enumerate(s):
        if ch in "([{":
            stack.append((ch, i))
        elif ch in ")]}":
            if not stack:
                return f"위치 {i}: '{ch}' 에 대응하는 여는 괄호 없음"
            top_ch, top_idx = stack[-1]
            if top_ch != match[ch]:
                return (
                    f"위치 {i}: '{ch}' 가 위치 {top_idx}의 '{top_ch}' 와 매칭 안 됨"
                )
            stack.pop()

    if stack:
        ch, idx = stack[-1]
        return f"위치 {idx}: '{ch}' 에 대응하는 닫는 괄호 없음"
    return "유효"


def count_min_removals(s: str) -> int:
    """최소 제거 횟수로 유효한 괄호 만들기 -- O(n)."""
    open_count = 0   # 매칭 못 한 '(' 수
    close_count = 0  # 매칭 못 한 ')' 수

    for ch in s:
        if ch == "(":
            open_count += 1
        elif ch == ")":
            if open_count > 0:
                open_count -= 1   # 매칭 성공
            else:
                close_count += 1  # 매칭 실패한 ')'

    return open_count + close_count


if __name__ == "__main__":
    print("=" * 55)
    print("괄호 매칭 검사")
    print("=" * 55)

    test_cases = [
        ("()",         True),
        ("()[]{}",     True),
        ("(]",         False),
        ("([)]",       False),
        ("{[]}",       True),
        ("",           True),
        ("(((", False),
        (")))", False),
        ("{[()]}",     True),
        ("([{}])",     True),
    ]

    print(f"{'입력':15} {'예상':6} {'결과':6} {'상태'}")
    print("-" * 40)
    for s, expected in test_cases:
        result = is_valid_brackets(s)
        status = "OK" if result == expected else "NG"
        print(f"{s!r:15} {str(expected):6} {str(result):6} {status}")

    print()
    print("=" * 55)
    print("상세 오류 분석")
    print("=" * 55)
    detail_cases = ["(]", "([)]", "(((", "{[]}", ")))"]
    for s in detail_cases:
        print(f"{s!r:10} -> {bracket_balance_detail(s)}")

    print()
    print("=" * 55)
    print("최소 제거 횟수")
    print("=" * 55)
    removal_cases = ["()))(" , "((("]
    for s in removal_cases:
        print(f"{s!r:10} -> 최소 제거 {count_min_removals(s)}회")
