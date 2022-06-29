# Condition & Loop


## 무슨 학교 다니세요?
```python
print("당신이 태어난 년도를 입력하세요")
year = int(input())
age = 2022 - year +1

if age <= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 17 and age >= 14:
    print("중학생")
elif age < 14 and age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다")
```

#

## 구구단 계산기
```python
print("구구단 몇단을 계산할까요?")
level = int(input())

print(f"구구단 {level}단을 계산합니다.")

for i in range(1,10):
     print(f"{level} x {i} = {level * i}")
```

## 구구단 게임1
```python
print("구구단 몇단을 계산할까요?")

#level = int(input()) #5줄 대신에 여기 넣으면 무한루프 돌입
while True:              # while True문은 좋은 코드가 아님 무한 루프에 빠지기 쉽기 때문이다.
    level = int(input())
    if level >= 1 and level <=9:
        print(f"구구단 {level}단을 계산합니다.")
        for i in range(1,10):
            print(f"{level} x {i} = {level * i}")
    
    elif level == 0:
        print("구구단 게임을 종료합니다.")
        break

    else:
        print("잘못 입력하셨습니다.")
```

## 구구단 게임2
```python
print("구구단 몇 단을 계산할까요(1~9)?")

x = 1
while(x != 0):
    x = int(input())
    if x == 0: 
        print("구구단 게임을 종료합니다.")
        break

    if not(1 <= x <= 9):
        print("잘못 입력하셨습니다","1부터 9사이 숫자를 입력해주세요")
        continue
   
    else:
        print("구구단" + str(x) + "단을 계산 합니다")
        for i in range(1,10):
            print(str(x) + "X" + str(i) + "=" + str(x*i))
        print("구구단 몇 단을 계산할까요(1~9)?")
    
```

#
## 숫자 맞추기 게임
```python
import random

true_value = random.randint(1,100)
input_value =999999999
print("숫자를 맞춰보세요(1~100)")

while input_value != true_value:
    input_value = int(input())
    
    if input_value > true_value:
        print("숫자가 너무 큽니다.")
    elif input_value < true_value:
        print("숫자가 너무 작습니다.")
    else:
        break

print(f"정답입니다. 입력한 수치는 {true_value}입니다.")
```

#
## 문장 뒤짚기
```python
import re


sentence = "I love you"
reverse_sen = ""

for char in sentence:
    print("REVERSE #1", reverse_sen)
    reverse_sen = char + reverse_sen
    print("REVERSE #2", reverse_sen)
```
## 십진수 -> 이진수

```python
decimal = int(input("십진수를 입력하세요: "))
result = ""

while decimal > 0 :
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
    print(f" decimal value : {decimal}")
    
print(result)
```

```python
from unicodedata import decimal


print("input decimal number: ",)
decimal = int(input())
result = ""
loop_counter = 0
while (decimal > 0):
    temp_decimal_input = decimal
    temp_result_input = result

    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result 


    
   # print("----------", loop_counter, "loop value check----------")      # 18줄 19줄은 같은 기능함 
    print(f"---------- {loop_counter} loop value check----------")        # f-string으로 구현
    print("Initial decimal:", temp_decimal_input, 
    ", Remainder:", remainder,
    ", Initial result", temp_result_input)
    print("Output decimal:", decimal,
    "Output result:", result)
    print("-----------------------------------------------------")
    print("")

    loop_counter += 1
print("Binary number is", result)

```

## 평균 구하기
```python
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average
    )
```