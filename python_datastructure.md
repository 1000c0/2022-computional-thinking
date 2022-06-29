# Python datastructure

## stack(스택)
- ### LIFO : Last in First Out
- 데이터의 입력은 push, 출력은 pop
- 리스트를 사용하여 스택 구조 구현
- push : append()
- pop : pop()
```python
a = [1, 2, 3]
a.append(10)   #==> [1, 2, 3, 10]
a.append(20)   #==> [1, 2, 3, 10, 20]
a.pop()  #==> 20
a.pop()  #==> 10
```
ex) 글자를 역순으로 출력
```python
word = input("Input a word : ")
word_list = list(word)
for i range(len(word_list)):
    print(word_list.pop())
```
#
## que
- ### FIFO : First in First Out
- 리스트를 사용하여 큐 구조 활용
- put : append()
- get : pop(0)
```python
a = [1, 2, 3]
a.append(10)   #==> [1, 2, 3, 10]
a.append(20)   #==> [1, 2, 3, 10, 20]
a.pop(0)  #==> 1
a.pop(0)  #==> 2 
```
#
## tuple
- 값의 변경이 불가능한 리스트
- 선언시 "()" 사용
- 리스트의 연산, 인덱싱, 슬라이싱 사용

```python
t = (1, 2, 3)
print(t + t, t * 2)    #==> (1, 2, 3, 1, 2, 3) (1, 2, 3, 1, 2, 3)
len(t)   #==> 3
t[1] = 5    #==> 오류 튜플은 수정할 수 없다.
```
- 값이 하나인 Tuple은 반드시 , 를 붙여야 한다.
  ```python
  t = (1,)
  ```

#
## set
- 값을 순서없이 저장, 중복 불허하는 자료형
```python
s = set([1, 2, 3, 4, 1, 2, 3])
s  #==> {1, 2, 3}
s.add(1)  #==> {1, 2, 3}
s.removed(1) #==> {2, 3} 
s.upadte([1, 4, 5, 6, 7])
s  #==> {1, 2, 3, 4, 5, 6, 7}
s.discard(3)  #==> {1, 2, 4, 5, 6, 7}
s.clear()  #==> 원소 삭제
```
- 집합의 연산
  ```python
  s1 = ([1, 2, 3, 4])
  s2 = ([4, 5, 6])
  s1.union(s2)
  s1 | s2  # 합집합 {1, 2, 3, 4, 5, 6}
  s1.intersection(s2)
  s1 & s2  #교집합 {4}
  s1.difference(s2)
  s1 - s2  # s1과 s2의 차집합 {1, 2, 3}
  ```

#
## dict
- 데이터를 저장할 때 key와 value를 함께 저장
- ex) 주민등록번호, 제품 모델 번호
- 구분을 위한 고유 값을 key 또는 identifier 라고 함
```python
fruit = {1 : "apple", 2 : "banana", 3 : "peach"}
fruit[1] = 'apple'
```
- dict 다루기
  ```python
  fruit = {}  # dict 생성
  fruit = {1 : "apple", 2 : "banana"}
  fruit.itmes()   #==> Dict_itmes([(1,'apple'), (2, 'banana')])  Dict 데이터 출력
  fruit.keys()    #==> Dict_keys([1, 2])
  fruit.values()  #==> Dict_values(['apple', 'banana'])
  fruit[3] = "peach"   #==> Dict 추가
  fruit #==>  {1 : 'apple', 2 : 'banana', 3 : 'peach'}
  ```

#
##  Command Analyzer
- command : 사용자가 서버에 명령어를 입력한 명령어 
  
#
## collections
- list, Tuple, Dict에 대한 Python Built-in 확장 자료 구조(모듈)
- 편의성, 실행 효율 제공
  # 
  ## deque
  - stack과 Queue를 지원하는 모듈
  - List에 비해 효율적인(빠른) 자료 저장 방식/메모리 구조 지원 -> 처리 속도 향상
  - rotate, reverse 등 Linked List의 특성을 지원
  - 기존 list 형태의 함수를 모두 지원
  ```python
  from collections import deque
  
  deque_list = deque()
  for i in range(5):
    deque_list.append(i)
    print(deque_list)
  ```
  #
  ## OrderedDict
  - 데이터 입력한 수서를 보장
  - But python 3.6부터 dict도 순서 보장
  ```python
  from collections import Ordereddict
  ```
  #
  ## defaultdict
  - Dict type 기본 값을 지정, 신규값 생성시 사용
  ```python
  from collections import defaultdict:
  
  d = defaultdict(object)  # Default Dictionary 생성
  d = defaultdict(lambda : 0)  #Default 값을 0으로 설정
  print(d["first"])
  ```
  - 하나의 지문에 각 단어들의 개수 세고 싶은 경우
  
  #
  ## Counter
  - sequence type의 data element들의 개수를 dict 형태로 반환
  - Dict type, keyword parameter 등도 처리 가능
  - set 연산자 지원
  - word counter 기능 쉽게 제공
  ```python
  from collections import Counter
  
  c = Counter('gallahad')
  text = "gallaha"
  print(c)   #==> Counter({'a' : 3, 'l' : 2, 'g' : 1, 'd' : 1, 'h' : 1})
  print(Counter(text)["a"])   #==> 3 아마도 print(c["a"])로 구혀가능 할 거라 생각
  ```
  #
  ## nametuple
  - Tuple 형태로 Data 구조체를 저장하는 방법
  - 저장되는 data의 variable을 사전에 지정해서 저장
  ```python
  from collections import namedtuple

  Point = namedtuple('Point', ['x', 'y'])
  p = Point(11, y = 22)
  print(p[0] + p[1])  #==> 33


  x, y = p
  print(x, y)   #==> 11, 22
  print(p.x + p.y)   #==> 33
  print(Point(x = 11, y = 22))   #==> Point(x = 11, y = 22)
  ``` 
