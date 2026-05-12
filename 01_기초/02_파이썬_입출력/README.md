# 02. 파이썬 입출력 최적화 (Python I/O Optimization)

## 소개

파이썬에서 `input()` 함수는 사용하기 편리하지만, **반복 호출 시 매우 느립니다**.
백준 15552번처럼 10만 번 이상 입력을 받아야 하는 문제에서는 `input()` 사용 시
시간 초과가 발생할 수 있습니다. `sys.stdin.readline()`을 사용하면 같은 작업을
수십 배 빠르게 처리할 수 있습니다. I/O 최적화는 알고리즘 자체와 무관하지만,
경쟁 프로그래밍에서 통과/실패를 가르는 핵심 기술입니다.

---

## 학습 목표

1. `sys.stdin.readline()`이 `input()`보다 빠른 이유를 설명할 수 있다.
2. 다양한 입력 패턴(단일 값, 공백 구분, 여러 줄, EOF)을 처리하는 코드를 작성할 수 있다.
3. 출력 최적화 기법(`sys.stdout.write`, `'\\n'.join()`)을 적용할 수 있다.

---

## 핵심 개념

### 1. input() vs sys.stdin.readline() 속도 비교

| 방법 | 내부 동작 | 10만 줄 처리 시간 (예상) | 특징 |
|------|-----------|--------------------------|------|
| `input()` | 매번 flush, 프롬프트 처리 포함 | ~2~5초 | 편리하지만 느림 |
| `sys.stdin.readline()` | 버퍼에서 직접 읽기 | ~0.2~0.5초 | 빠르지만 `\n` 포함 |
| `sys.stdin.read()` | 전체를 한 번에 읽기 | ~0.05~0.1초 | 가장 빠름, 파싱 필요 |

> **핵심**: `input()`은 매번 시스템 콜을 발생시키는 반면,
> `sys.stdin.readline()`은 내부 버퍼를 활용합니다.

### 2. sys.stdin.readline() 주의사항: 개행 문자(\\n)

```python
import sys

line = sys.stdin.readline()   # '42\n' ← 뒤에 \n 포함!
line = sys.stdin.readline().strip()  # '42'  ← 올바른 사용
n = int(sys.stdin.readline())  # int() 변환 시 \n 자동 무시
```

**가장 흔한 실수**: 문자열로 받을 때 `.strip()`을 빠뜨려 비교 오류 발생.

### 3. 자주 쓰는 입력 패턴

```python
import sys
input = sys.stdin.readline  # input()을 덮어쓰기 (가장 흔한 패턴)

# 정수 하나
n = int(input())

# 공백으로 구분된 두 정수
a, b = map(int, input().split())

# 정수 리스트 한 줄
arr = list(map(int, input().split()))

# n줄 입력
lines = [input().strip() for _ in range(n)]

# 전체를 한 번에 읽기 (대용량)
data = sys.stdin.read().split()  # 공백/개행으로 분리된 토큰 리스트
```

### 4. sys.stdout.write vs print()

| 방법 | 10만 줄 출력 시간 | 특징 |
|------|-------------------|------|
| `print()` | ~1~3초 | 편리, 자동 개행, 느림 |
| `sys.stdout.write()` | ~0.1~0.5초 | 빠름, `\n` 직접 추가 필요 |
| `'\n'.join()` + 1회 출력 | ~0.05~0.1초 | 가장 빠름, 리스트 모아서 출력 |

```python
import sys

# 느린 방법 — print() 반복 호출
for x in results:
    print(x)

# 빠른 방법 — 한 번에 출력
sys.stdout.write('\n'.join(map(str, results)) + '\n')

# 또는
print('\n'.join(map(str, results)))
```

### 5. EOF(End of File) 처리

입력 줄 수가 정해지지 않은 문제에서 파일 끝까지 읽어야 할 때:

```python
import sys

# 방법 1: try/except (가장 안전)
try:
    while True:
        line = input()  # 또는 sys.stdin.readline().strip()
        if not line:
            continue
        # 처리...
except EOFError:
    pass

# 방법 2: for line in sys.stdin (파이써닉)
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # 처리...

# 방법 3: 전체 읽기 후 파싱
data = sys.stdin.read().split()
```

---

## 예제로 보기

### 예제 1: input() vs readline() 속도 비교 (`src/01_input_comparison.py`)

가상 데이터로 두 방법의 속도를 직접 측정합니다.

```bash
python src/01_input_comparison.py
```

```
[예상 출력]
input() 모사            : 0.4523초
sys.stdin.readline() 모사: 0.0321초
sys.stdin.read().split(): 0.0089초
```

### 예제 2: 경쟁 프로그래밍 I/O 템플릿 (`src/02_fast_io_template.py`)

실전에서 바로 쓸 수 있는 I/O 패턴을 정리합니다.

```bash
python src/02_fast_io_template.py
```

### 예제 3: 출력 최적화 (`src/03_output_optimization.py`)

`print()` vs `sys.stdout.write()` vs 버퍼 모아서 출력을 비교합니다.

```bash
python src/03_output_optimization.py
```

### 예제 4: EOF 처리 (`src/04_eof_handling.py`)

EOF까지 읽는 다양한 패턴을 보여줍니다.

```bash
python src/04_eof_handling.py
```

---

## 자주 하는 실수

1. **`sys.stdin.readline()`의 `\n` 미제거**
   ```python
   # 잘못된 코드
   s = sys.stdin.readline()  # '42\n'
   if s == '42':  # False! '42\n' != '42'
       ...
   # 올바른 코드
   s = sys.stdin.readline().strip()  # '42'
   ```

2. **`input = sys.stdin.readline` 덮어쓰기 후 `.strip()` 누락**
   ```python
   input = sys.stdin.readline
   n = int(input())     # OK — int() 변환 시 \n 무시
   s = input().strip()  # OK — 문자열은 반드시 strip()
   s = input()          # 위험 — \n 포함된 문자열
   ```

3. **출력을 한 줄씩 print() — 출력 횟수가 많을 때 TLE**
   - 백준 15552번은 입력 최적화뿐 아니라 출력도 최적화해야 합니다.
   - `'\n'.join(map(str, results))`로 한 번에 출력하세요.

4. **sys.stdin.read().split() 후 인덱스 오류**
   ```python
   data = sys.stdin.read().split()
   # data[0], data[1], ... 순서로 파싱해야 합니다.
   # 인덱스 계산 실수 주의!
   ```

5. **EOF 없이 무한 루프**
   ```python
   # 잘못된 코드 — stdin이 파이프일 때 무한 루프
   while True:
       line = sys.stdin.readline()
       # line이 빈 문자열('')이면 EOF
       if not line:  # 이 체크가 없으면 무한 루프!
           break
   ```

---

## 정리

| 상황 | 권장 방법 |
|------|-----------|
| 입력 횟수가 많을 때 | `sys.stdin.readline()` 또는 `sys.stdin.read()` |
| 단순한 1~2줄 입력 | `input()` 사용 무방 |
| 출력 횟수가 많을 때 | `'\n'.join(map(str, results))` + 1회 출력 |
| EOF까지 읽어야 할 때 | `for line in sys.stdin` |

---

## 직접 해 보기

1. `src/01_input_comparison.py`를 실행하고 실제 속도 차이를 확인하세요.
2. `homework/answer/boj_15552.py`를 작성하고 백준에 제출해 보세요.
3. 자신이 이전에 작성한 코드 중 `input()`을 많이 사용하는 코드를 찾아
   `sys.stdin.readline()`으로 개선해 보세요.

---

## 다음 단원

➡️ [03. 자료형 복잡도](../03_자료형_복잡도/README.md)

---

## 참고 자료

- [백준 15552번 — 빠른 A+B](https://www.acmicpc.net/problem/15552)
- [Python sys.stdin 공식 문서](https://docs.python.org/3/library/sys.html#sys.stdin)
