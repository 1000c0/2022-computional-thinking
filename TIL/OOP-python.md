# Object-Oriented Programming
- 주체들의 행동과 데이터를 중심으로 프로그램 작성 후 연결
- 객체 : 속성(Attribute)과 행동(method)을 가짐
- 속성은 변수로 행동은 함수로 표현
- class와 실제 구현체인 instance로 나뉜다
- class 예약어, class 이름, 상속받는 객체명으로 구성
- 함수와 변수는 snake_case로 
- class 명은 CamelCase
#
 ## class 구현하기
  ```python
  class Laptop(object):
      def __init__(self, name, size, color): #Attribute
          self.name = name
          self.size = size
          self.color = color
      def change_color(self, new_color):  #method
          print("laptop 색상을 변경합니다 : %d -> %d" % (self.color, new_color)) 
          self.color = new_color
  ```
#
 ## Attribute 추가
  - __ __init__ __ , self로 추가
  - __ __init__ __ 는 객체 초기화 함수
  - __ __str__ __ 는 print 할 때 필요 
    ```python
    class Laptop(object):
      def __str__(self):
        return "My laptop is %s, I like %s color."% (self.name, self.color)
      
    macbook = Laptop("Macbook Air", 13, "silver")
    print(macbook)
    ```


#
## method 구현
- __self__ 를 반드시 추가해야 함
  ```python
  class Laptop(object):
    def change_color(self, new_color):
      print("laptop 색상을 변경합니다 : %d -> %d" % (self.color, new_color)) 
      self.color = new_color
  ```
#
## object(instance) 사용
- Object 이름 선언과 함께 초기값 입력하기
- 객체명, class명, __ __init__ __함수 interface, 초기값 구성
  ```python
  macbook = Laptop("Macbook Air", 13, "silver")
  #객체명   class명  __init__ 함수 interface,  초기값
  
  class Laptop(object):
    ~~~~
   
   macbook = Laptop("Macbook Air", 13, "silver")
   print("현재 laptop의 색상은 :", macbook.color)
     #==> 현재 laptop의 색상은 : silver
  
   macbook.change_color("space gray")
   print("현재 laptop의 색상은 :", macbook.color)
     #==> 현재 laptop의 색상은 : space gray
  ```
#
## Characteristic
  - ### Inheritance(상속)
    - 부모 클래스로부터 속성과 method를 물려받은 자식 클래스를 생성하는 것
     ```python
    class Person(object):
      def __init__(self, name, age):
        self.name = name
        self.age = age
   
    class Korean(Person):
      pass
    II = korean("me", 19)
    print(II.name)  #==> me
     ```

  - ### Polymorphism(다형성)
    - 같은 이름 메소드의 내부 로직을 다르게 작성
     ```python
     class Animal:
       def __init__(self, name):
         self.name = name
    
       def talk(self):
         raise NotImplementedError("Subclass must implement abstract method")
    
     class Cat(Animal):
       def talk(self):
         return 'Meow!'
    
     class Dog(Animal):
       def talk(self):
         return 'Woof!'     
     
     animals = [Cat('Navy'), Dog('Doji')]
     for ani in animals:
       print(ani.name + ':' + ani.talk())
     #==> Navy : Meow!
     #==> Doji : Woof!
     ```
  - ### Visibility(가시성)
    - 객체의 정보를 볼 수 있는 레벨을 조절 
    - 아무나 정보 수정할 수 없도록 하는 것
    - Encapsulation
      - 정보 은닉
      - class간 간섭/정보공유 최소화
      - 인터페이스만 알아서 써야 함
    - ex_1)
      - product 객체만 inventory에 들어감
      - inventory에 product 개수 확인
      - product items는 접근 불가
       ```python
       class Product(object):
         pass
       class Inventory(object):
         def __init__(self):
           self.__itmes = []  #__ 때문에 타객체가 접근 불가능
         
         def add_new_item(self, product):
           if type(product) == Product:
             self.__items.append(product)
             print("new items.added")
         
           else:
             raise ValueError("Invalid Item")
         
         def get_number_of_items(self):
           return len(self.__items)
       ```
    - ex_2)
      - product 객체를 inventory 객체에 추가
      - inventory에 product 개수 확인
      - Inventory에 Product items 접근 허용
      ```python
      class Inventory(object):
         def __init__(self):
           self.__itmes = []

         @property            #property decorator 숨겨진 변수 반환 가능
         def items(self):
           return self.__items
      
      my_inventory = Inventory()
      my_inventory.add_new_item(Product())
      print(my_inventory.get_number_of_items())

      itmes = my_inventory_items  #property decorator로 함수를 변수처럼 호출
      itmes.append(Product())
      print(my_inventory.get_number_of_items())
      ```
#
## __
- 특수 예약 함수나 변수, 함수명 변경(맨글링)으로 사용
- 예) __ __main__ __ , __ __add__ __ ,  __ __str__ __ , __ __eq__ __


#
## OOP Implementation Example
```python
class Note(object):
    def __init__(self, contents = None):
        self.contents = contents
    def write_contents(self, contents):
        self.contents = contents
    def remove_all(self):
        self.contents = ""
    def __str__(self):
        return self.contents
    

class Notebook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}
    
    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("페이지가 모두 채워졌다.")
    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("헤당 페이지는 존재하지 않는다.")
    def get_number_of_pages(self):
        return len(self.notes.keys())
```
