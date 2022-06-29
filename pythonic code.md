# Pythonic code
## list comprehension
- 포괄적인 list, 포함되는 list라는 의미로 사용됨
- 기본 list 사용
- 일반적으로 for + append 속도가 빠름
```python
result = [i for i in range(10)]
result    #==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result_1 = [i for i in range(10) if i % 2 == 0]
result_1  #==> [0, 2, 4, 6, 8]
```
```python
word_1 = "Hi"
world_2 = "six"

result = [i + j for i in word_1 for j in word_2]
result #==> ['Hs', 'Hi', 'Hx', 'is', 'ii', 'ix']

result = [i + j for i in word_1 for j in word_2 if not (i == j)]
result #==> ['Hs', 'Hi', 'Hx', 'is', 'ix']
```

```python
words = "I love apple".split()

stuff = [[w.upper(), w.lower(), len(w)] for w in words]

print(stuff)  #==> [['I', 'i', 1], ['LOVE', 'love', 4], ['APPLE', 'apple', 5]]
for i in stuff:
    print(i)  #==>['I', 'i', 1]
                 #['LOVE', 'love', 4]
                 #['APPLE', 'apple', 5]
```
- two dimensional
  ```python
  case_1 = ["a", "b", "c"]
  case_2 = ["d", "e", "a"]
  result = [[i + j for i in case_1] for j in case_2]
  result #==> [['ad', 'bd', 'cd'], ['ae', be', 'ce'], ['aa', 'ba', 'ca']]
  ```

#
## enumerate & zip
- enumerate : list의 element를 추출할 떄 번호를 붙여서 추출
  ```python
  for i, v in enumerate(['i', 'pad', 'pro']):
      print(i, v) #==> # 0, i
                       # 1, pad
                       # 2, pro
    ```
- zip : 두개의 list의 값을 병렬적으로 추출
  ```python
  al = ['a1', 'a2', 'a3']
  bl = ['b1', 'b2', 'b3']
  for a , b in zip(al, bl):
      print(a, b) #==> a1 b1
                    #  a2 b2
                    #  a3 b3
  ```
- 동시 사용
  ```python
  al = ['a1', 'a2', 'a3']
  bl = ['b1', 'b2', 'b3']
  for i, (a,b) in enumerate(zip(al, bl)):
      print(i, a, b)  #==> 0 a1 b1
                      #  1 a2 b2
                      #  2 a3 b3
  ```
#
## lambda & map & reduce
- lambda : 함수 이름 없이, 함수처럼 쓸 수 있는 익명 함수
  ```python
  f = lambda x, y: x + y
  print(f(3))
  
  p = lambda x: x / 2
  print(f(3))
  
  print((lambda x: x +1)(5))
  ```
  - 사용을 권장하지 않지만 많이 쓰기에 알아둬야 함

- map : 두번째 인자(리스트, 튜플)를 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 시행
   - if 필터도 사용 가능
   - list를 붙여줘야 list 사용 가능
  ```python
  ex = [1, 2, 3, 4]
  f = lambda x, y: x + y
  print(list(map(f, ex, ex)))   #==> [2, 4, 6, 8]
  print(list(map(lambda x: x + x, ex)))
  ```
- reduce : map function과 달리 list에 똑같은 함수를 누적하여 적용
  ```python
  from functools import reduce
  print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))   #==> 15
  ```
#
## iterable object
- sequence형 자료형에서 데이터를 순서대로 추출
  ```python
  for city in ["Seoul", "Busan", "Pohang"]:
    print(city, end="\t")
  
  for phone in ("iphone", "galaxy"):
    print(phone, end="\t")
  
  for char in "I love apple":
    print(char, end = " ")
    ```
- iter()와 next() 함수로 iterable 객체를 iterator object로 사용
  ```python
  corps = ["APPLE", "SAMSUNG", "LG"]
  iter_obj = iter(corps)
  print(next(iter_obj))  #==> APPPLE
  print(next(iter_obj))  #==> SAMSUNG
  print(next(iter_obj))  #==> LG
  next(iter_obj)  #==> ''붙어서 출력, 그러나 3번 호출 했기 떄문에 호출 할 것 없다
    ```
#
## generator
- element가 사용되는 시점에 값을 메모리에 반환
 - yield를 사용해 한번에 하나의 element만 반환
 ```python
 def generator_list(value):
   result = []
   for i in range(value):
     yield i
 ```
- list comprehension과 유사한 형태로 generator형태의 list 생성
- generator expression 이라는 이름으로도 부름
  ```python
  gen_ex = (n * n for n in range(500))
  print(type(gen_ex))   #==> <class 'generator'>
  ```
#
## function passing arguments 
- ### Keyword arguments
  - 함수에 사용되는 parameter의 변수명을 사용, arguments 넘김
    ```python
    def print_something(my_phone, your_phone):
      print("Hello {0}, My phone is {1}".format(your_phone, my_phone))
    
    print_something("iphone", "galaxy")
    print_something(your_phone = "galaxy", my_phone = "iphone")
    #==> Hello galaxy, My phone is iphone
    ```
- ### Default arguments
  - parameter의 기본 값을 사용, 입력하지 않을 경우 기본값 출력
    ```python
    def print_laptop(my_lap, your_lap = "Dell"):
      print("Hello {0}, My laptop is {1}".format(your_lap, my_lap))
    
    print_laptop("Mac", "Dell")
    print_laptop("Mac")
    #==> Hello Dell, My laptop is Mac
    ```
 - ## variable-length asterisk
  - 가변인자(variable-length)
    - 개수 정해지지 않은 변수를 parameter로 사용
    - argyments 추가 가능
    - ( * ) 기호로 표시
    - 입력된 값은 tuple로 사용
    - 가변인자는 마지막에 한 개만 사용 가능  
    ```python
    def asterisk_test(a, b, *args):
      return a + b + sum(args)  
    print(asterisk_test(1, 2, 3, 4, 5, 6))   #==> 21
    
    def asterisk_ex(*args):
      a, b, c = args    # tuple 타입으로 사용 가능 -> 언패킹 시행
      return a, b, c
    print(asterisk_ex(1, 2, 3))   #==> 1, 2, 3
    ```
  
  - 키워드 가변인자(keyword variable-length)
   - ( * ) 2개 사용
   - 입력된 값은 dict 타입으로 사용
     ```python
     def key_args_1(**kwargs):
       print(key_args)
       print("First value is {first}".format(**kwargs))
      
      def key_args_ex(a,b, c, *args, **kwargs):
        print(a + b + sum(args))
        print(kwargs)
      key_args_ex(1, 2, 3, 4, 5, 6, first = 1, second = 2, third = 3)
      #==> 21
      #==> {'first' : 1, 'second' : 2, 'third' : 3}
      ```
#
## asterisk *
 - 단순 곱셈, 제곱 연산, 가변인자로 활용
 - tuple, dict형 자료형에 들어가 있는 값을 unpacking
 - 함수의 입력값, zip등에 사용 가능
   ```python
   def asterisk_1(a, *args):  # 가변인자 의미
     print(a, *args)  # 풀어버린다
     print(a, args)
     print(type(args))
    
    test = (2, 3, 4, 5, 6)
    asterisk_1(1, *test)  # '*' 때문에 언패킹
    
    #==> 1, 2, 3, 4, 5, 6
    #==> 1, (2, 3, 4, 5, 6)
    #==> <class 'tuple'>
   ```
  - 시퀀스형 데이터 언패킹
     ```python
     a, b, c = ([1, 2], [3, 4], [5, 6])
     print(a, b, c)

     data = ([1, 2], [3, 4], [5, 6])
     print(*data)  # 언패킹

     #==> [1, 2] [3, 4] [5, 6]으로 결과 값이 같다.
     ```
  - dict 타입 데이터 언패킹
     ```python
     def asterisk(a, b, c, d):
       print(a, b, c, d)
      data = {"b" : 1, "c" : 2, "d" : 3}  # b = 1, c =2, d = 3 으로 언패킹됨
      asterisk(10, **data)
       #==> 10 1 2 3
     ```
  - zip으로 활용
    ```python
    for data in zip(*([1, 2], [3, 4], [5, 6])):
      print(data)
      #(1, 3, 5)
      #(2, 4, 6)
    ```
    