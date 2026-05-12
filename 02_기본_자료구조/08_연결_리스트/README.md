# 08. 연결 리스트 (Linked List)

## 소개

Python의 `list`는 동적 배열로, 임의 접근이 O(1)이지만 중간 삽입/삭제는 O(n)입니다.
연결 리스트(Linked List)는 이와 반대로, **알려진 위치에서의 삽입/삭제가 O(1)**이지만 임의 접근은 O(n)입니다.

Python에서는 연결 리스트를 직접 구현할 일이 많지 않지만, 코딩 테스트에서 개념 이해와
포인터(참조) 조작 능력을 검증하는 문제가 자주 출제됩니다.

**포인터(참조) 개념:**
```
Node: [data | next] -> [data | next] -> [data | next] -> None
       head                                              tail
```

각 노드는 **다음 노드에 대한 참조(reference)** 를 가집니다.
Python에서 이것은 단순한 객체 참조입니다.

---

## 학습 목표

1. Node 클래스를 정의하고 단순/이중/원형 연결 리스트를 직접 구현한다.
2. 연결 리스트의 삽입/삭제 O(1), 탐색 O(n) 복잡도를 이해하고 Python list와 비교한다.
3. 역전(reverse), 사이클 감지(Floyd's), 중앙 노드 탐색 등 대표 문제를 풀 수 있다.

---

## 핵심 개념

### 1. Node 클래스

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # 다음 노드 참조
```

---

### 2. 단순 연결 리스트 (Singly Linked List)

```
head
 |
[1] -> [2] -> [3] -> [4] -> None
```

| 연산 | 시간 복잡도 | 설명 |
|------|------------|------|
| 맨 앞 삽입 | O(1) | head 포인터만 변경 |
| 맨 뒤 삽입 | O(n) or O(1) | tail 포인터 있으면 O(1) |
| 임의 위치 삽입 | O(n) | 탐색 후 포인터 변경 |
| 맨 앞 삭제 | O(1) | head 이동 |
| 임의 위치 삭제 | O(n) | 탐색 후 포인터 변경 |
| 탐색 | O(n) | 순차 탐색 |
| 인덱스 접근 | O(n) | 순차 탐색 |

---

### 3. 이중 연결 리스트 (Doubly Linked List)

```
head                                    tail
 |                                       |
[1] <-> [2] <-> [3] <-> [4] <-> None
```

각 노드가 `prev`와 `next` 두 포인터를 가진다.
임의 위치 삭제 시 이전 노드를 O(1)에 접근 가능 -> 삭제 O(1) (노드 참조가 있을 때).

---

### 4. 원형 연결 리스트 (Circular Linked List)

```
head
 |
[1] -> [2] -> [3] -> [4]
 ^                    |
 +--------------------+
```

마지막 노드가 head를 가리킨다. 순환 구조.

---

### 5. Python list vs 연결 리스트

| 연산 | Python list | 연결 리스트 |
|------|-------------|------------|
| 임의 접근 arr[i] | O(1) | O(n) |
| 맨 뒤 삽입 | O(1) 균상 | O(1) (tail 있을 때) |
| 맨 앞 삽입 | O(n) | O(1) |
| 중간 삽입 | O(n) | O(1) (노드 알 때) |
| 중간 삭제 | O(n) | O(1) (노드 알 때) |
| 탐색 | O(n) | O(n) |
| 메모리 | 연속 배열 (캐시 친화적) | 비연속 (포인터 오버헤드) |

---

## 예제로 보기

| 파일 | 내용 | 핵심 개념 |
|------|------|----------|
| `src/01_singly_linked_list.py` | 단순 연결 리스트 완전 구현 | append, prepend, delete, search |
| `src/02_doubly_linked_list.py` | 이중 연결 리스트 | prev/next 포인터 |
| `src/03_circular_linked_list.py` | 원형 연결 리스트 | 순환 구조 |
| `src/04_linked_list_problems.py` | reverse, cycle 감지, 중앙 노드 | Floyd's 알고리즘 |

---

## 다른 시각으로 보기 -- 기차 연결 비유

```
[기관차] -> [객차1] -> [객차2] -> [객차3] -> (끝)
  head       node       node       tail

중간에 객차 추가: 앞 객차의 연결만 바꾸면 됨 -> O(1)
중간 객차 제거: 앞 객차를 다음 객차에 직접 연결 -> O(1)
3번째 객차 찾기: 앞에서 순서대로 세어야 함 -> O(n)
```

---

## 자주 하는 실수

### 실수 1: None 체크 누락 -- NoneType 에러

```python
# 잘못된 예
def traverse(head):
    node = head
    while node:
        print(node.data)
        node = node.next   # node가 None이면 .next 접근 오류!

# 올바른 예
def traverse(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next
```

### 실수 2: 삭제 시 prev 포인터 관리

```python
# 잘못된 예 -- 이전 노드를 업데이트하지 않음
def delete_node(head, target):
    node = head
    while node:
        if node.data == target:
            node = node.next   # 이전 노드가 아직 삭제된 노드를 가리킴!
        node = node.next

# 올바른 예
def delete_node(head, target):
    if head.data == target:
        return head.next
    node = head
    while node.next:
        if node.next.data == target:
            node.next = node.next.next   # 이전 노드의 next를 건너뜀
            return head
        node = node.next
    return head
```

### 실수 3: 역전 시 포인터 순서

```python
# 잘못된 예 -- next를 먼저 변경하면 원래 next를 잃음
node.next = prev     # 원래 node.next 잃어버림!
prev = node
node = node.next     # None!

# 올바른 예
next_node = node.next   # 1. 먼저 저장
node.next = prev        # 2. 역전
prev = node             # 3. prev 이동
node = next_node        # 4. node 이동
```

### 실수 4: 사이클 감지에서 None 체크

```python
# 잘못된 예 -- slow/fast가 None일 수 있음
while slow != fast:
    slow = slow.next
    fast = fast.next.next   # fast가 None이면 AttributeError!

# 올바른 예
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # 사이클 있음
return False
```

### 실수 5: 이중 연결 리스트에서 양방향 포인터 모두 업데이트

```python
# 잘못된 예 -- next만 업데이트
new_node.next = current.next
current.next = new_node
# current.next.prev 업데이트 누락!

# 올바른 예
new_node.next = current.next
new_node.prev = current
if current.next:
    current.next.prev = new_node
current.next = new_node
```

---

## 정리

| 개념 | 핵심 포인트 |
|------|------------|
| 단순 연결 리스트 | next 포인터, 삽입/삭제 O(1) at 알려진 위치 |
| 이중 연결 리스트 | prev+next, 양방향 O(1) |
| 원형 연결 리스트 | 마지막 노드가 head 참조 |
| 역전 | 포인터 3개 (prev, cur, next) 사용 |
| 사이클 감지 | Floyd's 토끼와 거북이 알고리즘 |
| 중앙 노드 | 빠른/느린 포인터 |

---

## 직접 해 보기

1. `src/01_singly_linked_list.py` 에서 각 연산을 손으로 그림으로 추적해 보세요.
2. `src/04_linked_list_problems.py` 에서 Floyd's 알고리즘을 직접 시뮬레이션해 보세요.
3. 이중 연결 리스트로 백준 1406(에디터) 문제를 풀어 보세요.
4. `homework/README.md` 의 과제를 풀어 보세요.

---

## 다음 단원

[09. 정렬 알고리즘](../../03_정렬과_탐색/README.md)
