# Topic : 후위 표기식(Postfix / RPN) 평가 및 중위->후위 변환
# Time  : O(n) -- 토큰 수에 비례
# Space : O(n) -- 스택 크기

OPERATORS = set("+-*/^")
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def evaluate_postfix(expression: str) -> float:
    """후위 표기식을 계산한다 -- Time O(n), Space O(n).

    예: '3 4 2 * +' -> 3 + (4*2) = 11.0
    """
    stack: list[float] = []
    tokens = expression.split()

    for token in tokens:
        if token in OPERATORS:
            if len(stack) < 2:
                raise ValueError(f"피연산자 부족: 스택={stack}, 연산자={token}")
            b = stack.pop()   # 오른쪽 피연산자
            a = stack.pop()   # 왼쪽 피연산자
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("나눗셈의 제수가 0")
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)
        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError(f"잘못된 표현식: 스택={stack}")
    return stack[0]


def infix_to_postfix(expression: str) -> str:
    """중위 표기식을 후위 표기식으로 변환 -- Shunting-Yard 알고리즘.

    Time O(n), Space O(n).
    """
    output: list[str] = []
    op_stack: list[str] = []
    tokens = expression.split()

    for token in tokens:
        if token not in OPERATORS and token not in "()":
            # 피연산자: 바로 출력
            output.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            # 매칭되는 '('까지 pop
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            if op_stack:
                op_stack.pop()  # '(' 제거
        else:
            # 연산자: 우선순위 비교
            while (
                op_stack
                and op_stack[-1] != "("
                and op_stack[-1] in PRECEDENCE
                and PRECEDENCE[op_stack[-1]] >= PRECEDENCE[token]
            ):
                output.append(op_stack.pop())
            op_stack.append(token)

    # 남은 연산자 모두 출력
    while op_stack:
        output.append(op_stack.pop())

    return " ".join(output)


if __name__ == "__main__":
    print("=" * 55)
    print("후위 표기식 평가")
    print("=" * 55)

    postfix_cases = [
        ("3 4 +",                7.0),    # 3+4
        ("3 4 2 * +",           11.0),   # 3 + 4*2
        ("5 1 2 + 4 * + 3 -",  14.0),   # 5+((1+2)*4)-3
        ("2 3 ^",                8.0),   # 2^3
        ("10 2 /",               5.0),   # 10/2
    ]

    print(f"{'후위 표기식':30} {'예상':8} {'결과':8}")
    print("-" * 50)
    for expr, expected in postfix_cases:
        result = evaluate_postfix(expr)
        ok = "OK" if abs(result - expected) < 1e-9 else "NG"
        print(f"{expr:30} {expected:8.1f} {result:8.1f} {ok}")

    print()
    print("=" * 55)
    print("중위 -> 후위 변환 (Shunting-Yard)")
    print("=" * 55)

    infix_cases = [
        "3 + 4",
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "5 + ( 1 + 2 ) * 4 - 3",
    ]

    for expr in infix_cases:
        postfix = infix_to_postfix(expr)
        value = evaluate_postfix(postfix)
        print(f"중위: {expr:30} -> 후위: {postfix:25} = {value}")
