# Basic and Etc...

## Python
인터프리터 : 통역을 해주는 프로그램
[코드 -> os] ---> cpu, memory

파이썬 : 프로그래밍 언어 

파이썬 인터프리터 : 번역을 해주는 프로그램

. : 현재 폴더

.. : 이전 폴더

<u>동적 타이핑 언어(Dynamic Typing): 실행하는 시점에 프로그램이 사용해야 할 데이터에 대한 타입을 결정함.

따라서 사전에 메모리 공간을 확보하는 컴파일러 언어보다는 느리다.</u>

#

## Variables
ex) a = 100 선언 : 'a'라는 이름을 가진 메모리(ram) 주소에 8을 저장한다. 


#
## Memory(Ram)
- -5 ~ 256까지 메모리 주소는 같다.
- rkxdms 이름의 변수라도 서로 다르다. -> 메모리에 저장된 주소가 다르다.

## primitive data types
-int : integer

-float : floationg points

-str : string

-true/flase : boolean

-type() 함수 : 변수의 데이터 형을 확인

-int가 float 보다 메모리 공간 사용량 적다. 
=> int + float -> float :메모리 공간을 많이 쓰는 쪽에 맞춘다. 


#


## 연산자 및 기타
a +=1 : <a = a + 1>

a -=1 : <a = a - 1>

[0 : 10 : 2]는 [0]에서 시작해서 [10]을 끝으로 2개씩 건너뛰어라

#

## List
- 시퀀스 자료형
-int와 float 같은 다양한 데이터 타입 포함
```python
a = ["company", 1, 0.4]
company = ['apple', 'LG', 'google']
a[0] = color    #리스트 안에 리스트 입력 가능
print(a)        #[['apple', 'LG', 'google], 1, 0.4]
```


### Indexing
 - list 속 값들은 주소(offset)을 가짐 
  -> 주소 사용해 할당된 값 호출

 ```python 
 colors  = ['red', 'green', 'blue'] 
           # [0]      [1]     [2]
           # [-3]     [-2]    [-1]
 print(colors[0])                  #red
 print(len(colors))                #3, 
                                   #len은 list의 길이를 반환
```


### Slicing 
 - list 값들을 잘라서 쓰는 것
```python
fruits = ['사과', '바나나', '복숭아', '오렌지']
print(fruits[n:m])    #n부터 m-1까지
print(fruits[:])      #처음부터 끝까지
                      #범위를 넘어간다면 자동으로 최대범위 지정
print(fruits[::n], "AND", a[::-m])#n칸 단위로, 역으로 슬라이싱
```

### Packing and Unpacking
- 패킹 : 한 변수에 여러 데이터 넣는 것
- 언패킹 : 한 변수의 데이터를 각각의 변수로 변환
  
```python
t = [1, 2, 3]          #패킹
a, b, c = t            #1, 2, 3을 a, b, c에 언패킹
print(t, a, b, c)      #[1, 2, 3] 1 2 3
```

### 이차원 리스트
-리스트 안에 리스트를 만들어 행렬(Matrix) 생성
```python
kor_score = [92, 86, 93]
math_score = [96, 72, 88]
eng_score = [55, 80, 76]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score[0][2])                          #93 

# [0]"kor_score"의 [2]"93"를 출력하라는 것  
```

#
## % type
- %s : string
- %c : character (문자 1개)
- %d : integer(정수)
- %f : floating-point
- %o : 8진수
- %x : 16진수
- % % : Literal% (문자 % 제외)

#
## if-else
- 아무 값도 없으면 false, 어떤 값이 있으면 True


#

## 정렬
```python
a = [2, 44, 3, 56, 23, 2000]
b = a.sort()
print(b)
# ==> None    #sort()는 return 값이 없다. a만 정렬된다.
```
```python
a = [2, 44, 3, 56, 23, 2000]
b = sorted(a)
print(b)
# ==> [2, 3, 23, 44, 56, 2000]  #sorted는 return 값이 있다.
```

