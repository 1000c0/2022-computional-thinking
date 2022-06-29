# Function

## 함수 선언 문법
- 함수 이름, parameter, indention, return value(optional)

- 함수 선언 예시
 ```python
  def calculate_rectangle_area(x , y):
      return x * y         #4칸 들여쓰기
  
  rectangle_x = 10
  rectangle_y = 20
  print ("사각형 x의 길이: ", rectangle_x)
  print ("사각형 y의 길이: ", rectangle_y)

  #넓이를 구하는 함수 호출
  print ("사각형의 넓이: ", calculate_rectangle_area(rectangle_x, rectangle_y))
  ```

- 함수 수행 순서
   
   1) 메인 프로그램 수행(11줄~14줄)
   2) 함수 호출(17줄)
   3) 함수 수행(8줄~9줄)
   4) 메인 프로그램 수행
  
#

## 프로그래밍 함수와 수학의 함수의 차이

- 모두 입력 값과 출력 값으로 구성

```
f(x) = 2x + 7
g(x) = 2x

! x = 2
f(2) = 11 ,g(2) = 4, f(g(2)) = 15, g(f(2)) = 121
이들의 합은 11 + 4 + 15 + 121 = 151
```

```python
def f(x):
    return 2 * x  + 7
def g(x):
    return x ** 2
x = 2
print(f(2) + g(2) + f(g(2)) + g(f(2)))
```
#

## Parameter vs Argument
- parameter : 함수의 입력 값 인터페이스
- argument : 실제 Parameter에 <u>대입</u>된 값
```python
def f(x):
    return 2 * x + 7   #2, 7은 parameter 

print(f(2))            # 2는 argument
>>>11
```
#

## 함수 형태
 - parmeter과 반환 값(return vlaue) 유무에 따라 형태 다름
  
P(x), 반환 값(x) : 함수내 수행문만 수행

P(x), 반환 값(o) : P없이, 수행문 수행 후 결과 값 반환

P(o), 반환 값(x) : P사용, 수행문만 수행

P(o), 반환 값(o) : P사용해 수행문 수행 후 결과 값 반환