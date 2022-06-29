# Console in/out

- 콘솔 창에서 문자열을 입력 받는 함수
```python
print("Enter your name: ")
somebody = input()    #콘솔 창에서 입력한 값을 somebody에 저장
print("Hi", somebody, "How r u today?")
```
- 숫자 입력 받기
```python
Date = int(input("날짜를 입력하세요 :")) # 입력 즉시 형 변환
print(Date)
>>>날짜를 입력하세요 : 20
20
```

#
## cf) print문의 ,콤마
```python
print("apple", "banana") #실행 시 두 문장 연결
#>>> apple banana   
```
#

## Print Formatting
- 형식(format)에 맞춰서 출력할 때 필요
  
#

## Print 문을 활용해서 결과 Formatting하기
- print 문은 기본적인 출력 외에 출력 양식의 형식 지정 가능

(1) % string

(2) format 함수

(3) fstring
```python
print("%d %d %d" % (1, 2, 3))
print("{} {} {}" .format("a", "b", "c"))
#print(f"value is {value})  <">가 어디서 끝나는지 모르겠음
```
### <u> 일반적으로 %-format과 str.format() 함수 사용 </u>
```python
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', 'two'))
```
#

## %-format
- %datatype
- %(variable)


```python
print("I read %d books." %4)
print("I was sick for %s days." %three)

number = 4; day = "three"
print("I read %d books. I was sick for %s days." %(number, day))

print("Product: $s, Price per unit: %f." % ("Apple", 5.243))
```

```python
print("Art: %5d, Price per Unit: %8.2f" % (453, 59.058))
#>>>Art:  453, Price per Unit:      59.06
#5자리 맞춰서 띄우기, 8자리 맞춰서 띄우고 소수점 2자리까지 출력
```
### % type
- %s : string
- %c : character (문자 1개)
- %d : integer(정수)
- %f : floating-point
- %o : 8진수
- %x : 16진수
- % % : Literal% (문자 % 제외)
  
#

## str.format() 함수
- "....{datatype}....".format(argument)
```python
age = 36; name = doji
print("I'm {0} years old.".format(age))
print("My name is {0} and {1} years old.".format(name, age))

print(Product: {0}, Price per Unit: {1:.3f}.format("Apple", 5.243))
```
```python
print("Art: {0:5d}, Price per Unit: {1:8.2f}" % (453, 59.058))
#>>>Art:  453, Price per Unit:      59.06
#5자리 맞춰서 띄우기, 8자리 맞춰서 띄우고 소수점 2자리까지 출력 
```

#

## Padding
- 여유 공간을 지정하여 글자배열 + 소수점 자릿수 맞추기
```python
print("Product: %5s, Price per unit: %.5f." %("Apple", 5.243))

print("Product: {0:5s}, Price per unit: {1:.5f}." .format("Apple", 5.243))

#같은 결과// {0}은 5칸 맞추고, 5.243은 소수점 5자리까지
#>>>Product: Apple, Price per unit: 5.24300.
```

```python
print("Product: %10s, Price per unit: %10.3f." %("Apple", 5.243))

print("Product: {0:>10s}, Price per unit: {1:10.3f}." .format("Apple", 5.243))

#같은 결과// 둘다 10칸 맞추고, 5.243은 소수점 3자리까지
#>>>Product:      Apple, Price per unit:      5.243.
```

#

## Naming
- 해당 표시할 내용을 변수로 표시하여 입력
```python
print("Product: %(name)10s, Price per unit: %(price)10.5f." %{"name":"Apple", "price":5.243})

print("Product: {name:>10s}, Price per unit: {price:10.5f}." .format(name="Apple", price = 5.243))

#같은 결과// 둘다 10칸 맞추고, 5.243은 소수점 5자리까지
#>>>Product:      Apple, Price per unit:    5.24300.
```

#

## f-string

```python
name = "steve"
age = 20
print(f"Hello, {name}. U r {age}.")
#>>>Hello, steve. U r 20.
print(f'{name:20}')
#>>>steve                : 왼쪽부터 정렬, 빈칸 15개 
print(f'{name:>20}')
#>>>               steve : 오른쪽부터 정렬, 빈칸 15개
print(f'{name:*<20}')
#>>>steve*************** : 왼쪽부터 정렬, * 15개
print(f'{name:*>20}')
#>>>***************steve : 오른쪽부터 정렬, * 15개
print(f'{name:*^20}')
#>>>*******steve******** : 가운데 정렬, * 15개

number = 3.141592653589793
print(f'{number:.2f}')
#>>>3.14                 : 소수점 2자리까지 출력
```

#

## 섭씨-화씨 변환기
```python
def c():
    return 9/5*x +32

print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
print("변환하고 싶은 섭씨 온도를 입력해 주세요:", )
x = float(input()) 

print("섭씨온도 :", x)
print("화씨온도 :",f'{c():.2f}')
```
#

## 별피라미드
```python
print("          *")
print("         * *")
print("        * * *")
print("       * * * *")
print("      * * * * *")
print("     * * * * * *")
print("    * * * * * * *")
print("   * * * * * * * *")
print("  * * * * * * * * *")
print(" * * * * * * * * * *")
print("* * * * * * * * * * *")
```
```python
print()

star = "*"
for i in range(11) :
    print(f'{star:^21}')
    star += " *"
```