# 05. 스택과 큐 -- 과제

## 제출 전 체크리스트

- [ ] 스택은 list, 큐는 deque를 사용했나요?
- [ ] 빈 스택/큐에서 pop 할 때 처리를 했나요?
- [ ] 시간 복잡도를 주석으로 명시했나요?

---

## 문제 1: 백준 9012 -- 괄호 (Silver IV)

**링크**: https://www.acmicpc.net/problem/9012

### 문제 설명
괄호 문자열(PS, Parenthesis String)이 주어졌을 때, 그것이 올바른 괄호 문자열인지 아닌지를 알아보려고 한다.
`()`, `(())` 는 VPS(Valid Parenthesis String)이지만, `)(`, `(()` 는 VPS가 아니다.

### 입력
```
6
(()())
(()((()))
(()([])
([
([)]
(()()
```

### 출력
```
YES
YES
NO
NO
NO
NO
```

### 힌트
- `(` push, `)` 에서 스택이 비어있으면 NO, 아니면 pop
- 처리 후 스택이 비어있으면 YES, 아니면 NO
- **Time O(n), Space O(n)**

---

## 문제 2: 백준 10845 -- 큐 (Silver IV)

**링크**: https://www.acmicpc.net/problem/10845

### 문제 설명
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령 목록: push X, pop, size, empty, front, back

### 힌트
- `collections.deque` 사용 필수
- 빠른 입력을 위해 `sys.stdin.readline` 사용
- **Time O(N), Space O(N)**

---

## 문제 3: 백준 10828 -- 스택 (Silver IV)

**링크**: https://www.acmicpc.net/problem/10828

### 문제 설명
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령 목록: push X, pop, size, empty, top

### 힌트
- Python list 사용
- 빠른 입력을 위해 `sys.stdin.readline` 사용
- **Time O(N), Space O(N)**

---

## 정답 파일

- `answer/boj_9012.py`
- `answer/boj_10845.py`
- `answer/boj_10828.py`
