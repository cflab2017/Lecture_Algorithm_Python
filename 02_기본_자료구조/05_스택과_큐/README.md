# 05. 스택과 큐 (Stack & Queue)

## 소개

스택(Stack)과 큐(Queue)는 선형 자료구조의 양대 산맥입니다.
두 자료구조는 **데이터 접근 순서**가 다르며, 이 차이가 전혀 다른 알고리즘을 만들어냅니다.

- **스택 (Stack)**: LIFO (Last In, First Out) -- 마지막에 넣은 것을 먼저 꺼낸다.
  - 실세계 예시: 책 더미, 브라우저 뒤로 가기, 함수 호출 스택, Ctrl+Z (실행 취소)
- **큐 (Queue)**: FIFO (First In, First Out) -- 먼저 넣은 것을 먼저 꺼낸다.
  - 실세계 예시: 줄 서기, 프린터 작업 대기열, BFS 탐색, OS 프로세스 스케줄링

백준 문제에서 스택은 괄호 검사, 수식 변환에, 큐는 BFS 탐색에 자주 등장합니다.

---

## 학습 목표

1. 스택(list)과 큐(deque)의 동작 원리와 시간 복잡도 차이를 이해한다.
2. 괄호 매칭 알고리즘을 스택으로 구현하고, 후위 표기식을 평가할 수 있다.
3. BFS/DFS에서 큐/스택이 어떻게 활용되는지 파악하고 직접 구현한다.

---

## 핵심 개념

### 1. 스택 (Stack) -- Python list

```
         PUSH ->  [  5  ]  <- TOP
                  [  3  ]
                  [  1  ]
                  +-----+
                   STACK

PUSH 5: [1, 3, 5]    TOP = 5
POP   : [1, 3]       반환 5
PEEK  : 3            TOP 확인 (제거 안 함)
```

| 연산 | Python | 시간 복잡도 |
|------|--------|------------|
| push | `stack.append(x)` | O(1) 균상 |
| pop  | `stack.pop()` | O(1) |
| peek | `stack[-1]` | O(1) |
| isEmpty | `len(stack) == 0` | O(1) |

---

### 2. 큐 (Queue) -- collections.deque

```
  ENQUEUE ->  [ 앞 | 1 | 2 | 3 | 4 | 뒤 ]  <- ENQUEUE
  DEQUEUE <-  [ 앞 ]                          꺼내기

  list.pop(0)     -> O(n)  <- 모든 원소를 앞으로 이동!
  deque.popleft() -> O(1)  <- 양쪽 끝 O(1) 보장
```

**왜 deque를 써야 하는가?**

| 연산 | list | deque |
|------|------|-------|
| `append(x)` (오른쪽) | O(1) | O(1) |
| `pop()` (오른쪽) | O(1) | O(1) |
| `insert(0, x)` (왼쪽) | O(n) | O(1) |
| `pop(0)` (왼쪽) | O(n) | O(1) |

큐는 왼쪽에서 꺼내므로 반드시 `deque`를 사용해야 합니다.

---

### 3. 괄호 매칭 알고리즘

```
입력: { [ ( ) ] }

처리 과정:
  '{' -> push      스택: ['{']
  '[' -> push      스택: ['{', '[']
  '(' -> push      스택: ['{', '[', '(']
  ')' -> pop '('   쌍 확인: '(' == '(' OK   스택: ['{', '[']
  ']' -> pop '['   쌍 확인: '[' == '[' OK   스택: ['{']
  '}' -> pop '{'   쌍 확인: '{' == '{' OK   스택: []
  빈 스택 -> 유효한 괄호!
```

---

### 4. 후위 표기식 (Postfix / Reverse Polish Notation)

```
중위: 3 + 4 * 2 = 11
후위: 3 4 2 * +

평가 과정 (스택 사용):
  토큰 3 -> push  스택: [3]
  토큰 4 -> push  스택: [3, 4]
  토큰 2 -> push  스택: [3, 4, 2]
  토큰 * -> pop 4,2 -> 4*2=8 push  스택: [3, 8]
  토큰 + -> pop 3,8 -> 3+8=11 push 스택: [11]
  결과: 11
```

---

## 예제로 보기

| 파일 | 내용 | 핵심 개념 |
|------|------|----------|
| `src/01_stack_basic.py` | 스택 push/pop/peek | list 기반, 언더플로 처리 |
| `src/02_queue_basic.py` | 큐 deque vs list | BFS 시뮬레이션, 속도 비교 |
| `src/03_bracket_matching.py` | 괄호 매칭 ()[]{}  | 스택 응용 |
| `src/04_postfix_eval.py` | 후위 표기식 평가 | 연산자 처리 |

---

## 다른 시각으로 보기

| 자료구조 | 비유 | 특징 |
|----------|------|------|
| 스택 | 책 더미 | 맨 위에서만 꺼낸다 |
| 큐 | 줄 서기 | 먼저 온 사람이 먼저 나간다 |
| 우선순위 큐 | 응급실 | 중요도 순서로 처리 |
| 덱(deque) | 양방향 줄 서기 | 앞뒤 양쪽에서 삽입/삭제 |

---

## 자주 하는 실수

### 실수 1: 큐에서 list.pop(0) 사용 -- O(n)

```python
# 잘못된 방법 -- O(n)
queue = [1, 2, 3]
queue.pop(0)   # 앞에서 꺼낼 때마다 모든 원소 이동!

# 올바른 방법 -- O(1)
from collections import deque
queue = deque([1, 2, 3])
queue.popleft()   # O(1)
```

### 실수 2: 스택 언더플로 미처리

```python
stack = []
# 확인 없이 pop
val = stack.pop()   # IndexError!

# 항상 비어있는지 확인
if stack:
    val = stack.pop()
```

### 실수 3: 괄호 매칭 시 스택 비어있는지 확인 누락

```python
# 잘못된 예
for ch in s:
    if ch in ")]}":
        top = stack.pop()   # 스택이 비어있으면 IndexError!

# 올바른 예
for ch in s:
    if ch in ")]}":
        if not stack:
            return False   # 매칭될 여는 괄호가 없음
        stack.pop()
```

### 실수 4: deque를 인덱스로 접근 -- O(n)

```python
from collections import deque
d = deque([1, 2, 3])
print(d[1])   # 가능하지만 O(n) -- 큐는 인덱스 접근이 주 목적이 아님
```

### 실수 5: 후위 표기식에서 피연산자 순서 역전

```python
# 잘못된 예: a - b 를 계산할 때
b = stack.pop()
a = stack.pop()
result = b - a   # 순서 반대!

# 올바른 예
b = stack.pop()
a = stack.pop()
result = a - b   # 먼저 push된 a가 왼쪽 피연산자
```

---

## 정리

| 개념 | 핵심 포인트 |
|------|------------|
| 스택 | LIFO, Python list로 O(1) push/pop |
| 큐 | FIFO, deque 사용으로 O(1) enqueue/dequeue |
| 괄호 매칭 | 여는 괄호 push, 닫는 괄호에서 pop 후 쌍 확인 |
| 후위 표기식 | 숫자 push, 연산자에서 두 개 pop 후 계산 |
| DFS | 스택(재귀 또는 명시적) |
| BFS | 큐(deque) |

---

## 직접 해 보기

1. `src/01_stack_basic.py` 를 실행하고 DFS 시뮬레이션 결과를 손으로 확인하세요.
2. `src/02_queue_basic.py` 에서 list와 deque의 속도 차이를 실제로 측정해 보세요.
3. `src/03_bracket_matching.py` 에 `<>` 괄호도 지원하도록 수정해 보세요.
4. `src/04_postfix_eval.py` 에서 중위 -> 후위 변환 함수도 구현해 보세요.
5. `homework/README.md` 의 과제를 풀어 보세요.

---

## 다음 단원

[06. 해시](../06_해시/README.md)
