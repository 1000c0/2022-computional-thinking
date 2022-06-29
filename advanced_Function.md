# 함수 호출 방식
- 값에 의한 호출(Call by Value)
     - 함수에 인자를 넘길 때 값만 넘김
     - 함수 내에 인자 값 변경 시, 호출자에게 영향을 주지 않음
- 참조의 의한 호출(Call by Reference)
     - 함수에 인자를 넘길 때 메모리 주소를 넘김  
     - 함수 내에 인자 값 변경 시, 호출자의 값도 변경됨
## 객체 참조에 의한 호출(Call by Object Reference)
- 파이썬의 함수 호출 방식
- 전달된 객체를 참조하여 변경 시 호출자에게 영향을 줌
- 그렇지만 새로운 객체를 만들 경우 호출자에게 영향을 주지 않음
  ```python
  def spam(eggs):
      eggs.append(1)    # 기존 객체의 주소값에 [1] 추가
      eggs = [2, 3]     # 새로운 객체 생성
    
  ham = [0]
  spam(ham)
  print(ham)
    #>>> [0, 1]
  ```


#
## swap
- 함수를 통해 변수 값을 교환(swap)하는 함수
- Call by XXXX를 설명하기 위한 전통적인 함수 예시


swap 일어나지 않는 함수

a = [1, 2, 3, 4, 5]

```python
def swap_value(x, y):
    temp = x
    x = y
    y = temp
a
#>>> [1, 2, 3, 4, 5]
```
x와 y가 가르치는 메모리의 주소만 바뀌고 리스트는 건드리지 않음

swap 일어나는 함수

```python
def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp
swap_offset(1, 2)
#>>> [1, 3, 2, 4, 5]
```
a리스트의 전역 변수 값을 직접 변경

```python
def swap_reference(list, offset_x, offset_y):
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp
swap_reference(a, 1, 2)
#>>> [1, 3, 2, 4, 5]
```
a리스트의 객체 주소 값을 받아 값을 결정

#

## 변수의 범위 (Scoping Rule)
- 변수가 사용되는 범위 (함수 또는 메인 프로그램)
- 지역 변수(Local variable) : 함수내에서만 사용
- 전역 변수(Global variable) : 프로그램 전체에서 사용

```python
def test(t):
    print(x)
    t = 20
    print("In Function :", t)
x =10
test(x)
print(t)
# 10
# In Function : 20
# NameError: name 't' is not defined
```
t는 함수 밖에서 정의 되지 않았기 때문이다.

```python
def test(t):
    t = 20
    print ("In Function :", t)

x = 10
print("Before :", x)    #10
test(x)                 # 함수 호출
print("After :", x)     

# Before : 10
# In Function : 20
# After : 10
```
10 함수 내부의 t는 새로운 주소값을 가진다.



### Global variable
- 전역변수는 함수에서 사용 가능
- But, 함수 내에 전역 변수와 같은 이름의 변수를 선언하면 새로운 지역 변수가 생김
  
```python
def f():
    s = "I love London!"
    print(s)
s = "I love Paris!"
f()
print(s)
# I love London!
# I love Paris!
```
함수 내 s 와 함수 밖의 s 는 서로 다르다.

```python
def f():
    global s
    s = "I love London!"
    print(s)
s = "I love Paris!"
f()
print(s)
# I love London!
# I love London!
```
global s 때문에 안과 밖의 s가 같아짐.

### Test
```python
def calculate(x, y):
    total = x + y
    print("In Function")
    print("a:", str(a), "b:", str(b), "a+b:", str(a+b), "total :", str(total))
    return total
a = 5
b = 7
total = 0

print("In Program - 1") 
print("a:", str(a), "b:", str(b), "a+b:", str(a+b))

sum = calculate(a,b)
print("After Calculation")
print("Total :", str(total), "Sum:", str(sum))

# In Program - 1
# a: 5 b: 7 a+b: 12
# In Function
# a: 5 b: 7 a+b: 12 total : 12
# After Calculation
# Total : 0 Sum: 12

```
지역함수는  전역함수에 영향을 주지 않는다.

#
## recursive function
- 자기 자신을 호출하는 함수
- 점화식과 같은 재귀적 수학 모형을 표현할 때 사용
- 재귀 종료 조건 존재, 종료 조건까지 함수호출 반복
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(int(input("Input Number for Factorial Calculation: "))))
```

#

## function type hints
- 파이썬은 dynamic typing -> 처음 함수를 사용하는 사용자가 interface를 알기 어려움

   -> python 3.5 버전 이후로는 PEP 484에 기반하여 typr hints 제공   
- 형식
   ```python
   def do_function(var_name: var_type) -> return_type:
       pass
   ```
- 예시  
   ```python
   def type_hint_example(name: str) -> str:
       return f"Hello, {name}"
   ```

- 장점
     - 사용자에세 interface를 명확히 알릴 수 있다.
     - 함수의 문서화시 parameter에 대한 정보를 명확히 알 수 있다.
     - mypy 또는 IDE, linter 등을 통해 코드의 발생 가능한 오류를 사전에 확인
     - 시스템 전체적인 안정성을 확보할 수 있다.

#
## docstring
- 파이썬 함수에 대한 상세스펙을 사전에 작성 -> 함수 사용자의 이행도 UP
- 세개의 따옴표로 docstring 영역 표시(함수명 아래)
  
#
## 함수 작성 가이드 라인
- 함수는 가능하면 짧게 작성
- 함수 이름에 함수의 역할과 의도를 명확히 들어낼 것
  ```python
  def print_hello_world():
      print("Hello, World")
  
  def get_hello_world():
      return "Hello, World"
  ```
- 하나의 함수에는 유사한 역할을 하는 코드만 포함
  ```python
  def add_variables(x, y):
      return x + y
  
  def add_variables(x, y):
      print(x, y)    # 갑자기 출력 하라면 읽는 이가 햇갈릴 수 있다.
      return x + y
  ```
- 인자로 받은 값 자체를 바꾸진 말 것(임시변수 선언)
  ```python
  def count_word(string_variable): 
      string_variable = list(string_variable) 
      return len(string_variable)
  ```
  가 아닌
  ```python
   def count_word(string_variable): 
       return len(string_variable)
  ```
  로 하는 것이 좋다.

  ### 함수는 언제 만드는가?
  - 공통적으로 사용되는 코드는 함수로 변환
  - 복잡한 수식과 조건 -> 식별 가능한 이름의 함수로 변환
  - 공통 코드는 함수로
  