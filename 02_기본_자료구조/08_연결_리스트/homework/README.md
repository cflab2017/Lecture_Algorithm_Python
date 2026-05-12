# 08. 연결 리스트 -- 과제

## 제출 전 체크리스트

- [ ] 포인터 조작 순서가 올바른가요? (None 체크, prev 포인터 등)
- [ ] deque 기반 풀이의 시간 복잡도를 주석으로 명시했나요?
- [ ] 엣지 케이스 (빈 리스트, 단일 원소)를 처리했나요?

---

## 문제 1: 백준 1406 -- 에디터 (Gold V)

**링크**: https://www.acmicpc.net/problem/1406

### 문제 설명
한 줄로 된 간단한 에디터를 구현하시오.
- `L`: 커서를 왼쪽으로 한 칸 이동
- `D`: 커서를 오른쪽으로 한 칸 이동
- `B`: 커서 왼쪽의 문자를 삭제
- `P $`: $ 문자를 커서 왼쪽에 삽입

### 입력
```
abcd
3
P x
L
P y
```

### 출력
```
abcdyx
```

### 힌트 -- deque 두 개(left/right) 방법

```
커서를 기준으로 왼쪽 deque(left)과 오른쪽 deque(right)으로 분리.

초기: left=[a,b,c,d], right=[]  (커서는 맨 오른쪽)

P x: left=[a,b,c,d,x], right=[]
L  : left=[a,b,c,d], right=[x]
P y: left=[a,b,c,d,y], right=[x]

결과: left+reversed(right) = abcdyx
```

- L: `right.append(left.pop())`
- D: `left.append(right.pop())`
- B: `left.pop()` (비어있으면 무시)
- P: `left.append(char)`
- **Time O(N + M), Space O(N + M)**

---

## 문제 2: 백준 5397 -- 키로거 (Gold V)

**링크**: https://www.acmicpc.net/problem/5397

### 문제 설명
비밀번호를 입력하는 키로거를 구현한다.
- `<`: 커서를 왼쪽으로
- `>`: 커서를 오른쪽으로
- `-`: 커서 왼쪽 문자 삭제
- 나머지: 해당 문자를 커서 왼쪽에 삽입

### 힌트
- 백준 1406과 동일한 deque 두 개 방법 사용
- `<` = L 연산, `>` = D 연산, `-` = B 연산
- **Time O(N), Space O(N)**

---

## 정답 파일

- `answer/boj_1406.py`
- `answer/boj_5397.py`
