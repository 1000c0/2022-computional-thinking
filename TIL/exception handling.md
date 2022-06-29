# Exception Handling
- 예상 가능한 예외는 if문으로 처리
- 예상 불가능한 예외(=인터프리터 과정에서 발생하는 예외)는 Exception Handling으로 처리

#
## exception의 종류
- ### built in Error
  - IndecError : List의 Index 범위를 넘어갈 때
  - NameError : 존재하지 않는 변수를 호출할 때
  - ZeroDIvisionError : 0으로 숫자를 나눌 때
  - ValueError : 변환할 수 없는 문자/숫자 를 변환할 때
  - FileNotFoundError : 존재하지 않는 파일을 호출할 때

#
## try ~ except 문법
```python
try:
    예외 발생 가능한 코드
except <Exception Type>:
    예외 발생시 대응하는 코드
```


###  예시
- 0으로 숫자를 나눌 때 예외 처리하기
  ```python
  for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError:
        print("Not divided by 0")
  ```
- 예외 정보 표시하기
  ```python
  for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError as e:
        print(e)
        print("Not divided by 0")
  ```
#
## try ~ except ~ else 문법
```python
try:
    예외 발생 가능한 코드
except <Exception Type>:
    예외 발생시 대응하는 코드
else:
    예외가 발생하지 않을 때 동작하는 코드
```
### 예시
- 0으로 나누지 않을 때 동작
  ```python
  for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError:
        print("Not divided by 0")
    else:
        print(10 / i)
  ```

#
## try ~ except ~ finally
```python
try:
    예외 발생 가능한 코드
except <Exception Type>:
    예외 발생시 대응하는 코드
finally:
    예외 발생 여부와 상관없이 실행됨
```
### 예시
- 프로그램 종류를 알림
  ```python
  try:
    for i in range(10):
        result = 10 // i
        print(result)
  
  except ZeroDivisionError:
    print("Not divided by 0")
  
  finally:
    print("종료되었습니다.")
  ```

#
## raise 구문
- 필요에 따라 강제로 Exception을 발생
```python
raise <Exception Type> (예외정보)
```
- 예시
  ```python
  while True:
    value = input("변환할 정수 값을 입력하세요")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않으셨습니다.")
    print("정수 값으로 변형된 숫자 -", int(value))
  ```

#
## assert 구문
- 특정 조건에서 만족하지 않을 경우 예외 발생시킨다.
- 조건문이 True 가 아닐 경우 예외를 일으킨다.
- 조건식이 False인 경우, AssertionError예외가 발생한다.

```python
assert 예외조건
```

- 예시
  ```python
  def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int)
    return bin(decimal_number) 
    #bin() : 전달 받은 int자료형의 값을 이진수로 바꿔주는 함수
  
  print(get_binary_number(10))
  ```

#
## cf) inistance()
- isinstance(확인하고자 하는 데이터 값, 확인하고자 하는 데이터 타입)
- 인스턴스와 타입이 같으면 True 반환, 다르면 False 반환
