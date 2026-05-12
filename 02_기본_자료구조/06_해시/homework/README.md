# 06. 해시 -- 과제

## 제출 전 체크리스트

- [ ] dict/set/Counter 중 적합한 자료구조를 선택했나요?
- [ ] 시간 복잡도를 주석으로 명시했나요?
- [ ] 키로 사용하는 값이 해시 가능한지 확인했나요?

---

## 문제 1: 백준 1764 -- 듣보잡 (Silver IV)

**링크**: https://www.acmicpc.net/problem/1764

### 문제 설명
듣도 못한 사람 N명과 보도 못한 사람 M명의 이름이 주어졌을 때,
듣도 보도 못한 사람의 명단을 사전순으로 출력하시오.

### 입력
```
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
```

### 출력
```
2
baesangwook
ohhenrie
```

### 힌트
- 첫 번째 리스트를 set에 저장한다.
- 두 번째 리스트를 순회하며 set에 있으면 결과에 추가.
- **Time O(N+M), Space O(N)**

---

## 문제 2: 백준 10816 -- 숫자 카드 2 (Silver IV)

**링크**: https://www.acmicpc.net/problem/10816

### 문제 설명
상근이가 가지고 있는 숫자 카드의 개수를 세어서, M개의 숫자에 대해 각 숫자가 몇 개 있는지 출력하시오.

### 입력
```
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
```

### 출력
```
3 0 0 1 2 0 0 2
```

### 힌트
- Counter 또는 dict로 각 숫자의 등장 횟수를 저장한다.
- **Time O(N+M), Space O(N)**

---

## 문제 3: 백준 1302 -- 베스트셀러 (Silver V)

**링크**: https://www.acmicpc.net/problem/1302

### 문제 설명
오늘 하루 동안 팔린 책의 제목이 주어진다.
가장 많이 팔린 책의 제목을 출력하시오. 여러 개라면 사전순으로 앞서는 것을 출력한다.

### 입력
```
5
top
top
top
kimchi
kimchi
```

### 출력
```
top
```

### 힌트
- Counter로 각 책의 판매 횟수를 센다.
- max(key=...) 로 가장 많이 팔린 책을 찾는다.
- 동점이면 사전순으로 앞선 것 선택.
- **Time O(N log N), Space O(N)**

---

## 정답 파일

- `answer/boj_1764.py`
- `answer/boj_10816.py`
- `answer/boj_1302.py`
