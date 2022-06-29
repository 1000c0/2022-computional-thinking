# File Handling

## 파일의 종류
- ### Text 파일
   - 인간이 이해할 수 있는 문자열로 저장
   - 메모장으로 열면 내용 확인 가능
   - HTML, Python 파일 등
- ### Binary 파일
   -  컴퓨터만 이해할 수 있는 이진법 형식으로 저장
   -  메모장으로 열면 일반적으로 꺠짐
   -  엑셀, 워드 파일 등

#
## Python File I/O
- 파일 처리를 위해 "*open*" 키워드 사용
- ### 파일 열기 모드
   - r : 읽기 모드 - 파일 읽을 때
   - w : 쓰기 모드 - 파일에 내용 쓸 때
   - a : 추가 모드 - 파일 마지막에 새로운 내용 추가 
```python
f = open("<파일이름>", "접근모드")
f.close
```
#
- ### 파이썬의 File Read
  - ### read() : txt 파일 안에 있는 내용을 문자열로 반환
    ```python
    f = open("i_have_a_dream.txt", "r")
    contents = f.read()
    print(contents)
    f.close
    ```
  - ### with 구문과 함께 사용 
     - close() 필요 없음
     - (교수님은 사용 비추)
    
    ```python
    with open("i_have_a_dream.txt", "r") as my file:
        contents =  my_file_read()
        print(type(contents), contents)
    ```   
  - 한줄씩 읽어 List Type으로 반환
    ```python
    with open("i_have_a_dream.txt", "r") as my_file:
        content_list = my_file.readlines() 
        #readlines() : 파일 전체를 list로 반환 
        print(type(content_list))  # Type 출력
        print(content_list) #리스트 값 출력
    ```
  - 실행 할 때마다 한 줄씩 읽어 오기
    ```python
    with open("i_have_a_dream.txt", "r") as my_file:
        i = 0
        while True:
            line = my_file.readline()
            #readline() : 실행 할 때마다 한 줄씩 읽어 오기, 용량이 많아서 한번에 메모리에 올리지 못할 때 사용
            if not line:
                break
            print(str(i) + "===" + line.replace("\n","")) #한줄씩 값 출력
            i = i + 1
    ```
  - 단어 통계 정보 산출
    ```python
    with open("i_have_a_dream.txt", "r") as my_file:
        contents = my_file.read()
        word_list = contents.split(" ")
        line_list = contents.split("\n") # 한줄씩 값 분리하여 리스트
    
    print("Total Number of Characters :", len(contents))
    print("Total Number of Words:", len(word_list))
    print("Total Number of Lines:", len(line_list))
    ```
 #
- ### 파이썬의 File Write
  - mode 는 *"w"* , encoding = "utf8"
    ```python
    f = open("count_log.txt", 'w', encoding = "utf8")
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
    f.close()
    ```
  - mode *"a"* 는 기존 파일에 추가 
    ```python
    with open("count_log.txt", 'a', encoding = "utf8") as f:
        data = "%d번째 줄입니다.\n" % i
        f.write(data) 
- ### 파이썬의 directory 다루기
  - os module로 다루기
    ```python
    import os
    os.mkdir("log") #디렉토리 만들기
    ```
  
  - 디렉토리 유무 확인 
    ```python
    if not os.path.isdir("log"): #디렉토리 유무 확인
        os.mkdir("log")
    ```
  
  - pathlib 모듈
    - path를 객체로 다룸

  - Log 파일 생성
    1) 디렉토리 유무 확인
    2) 파일 유무 확인
    ```python
    import os
    
    if not os.path.isdir("log"):
        os.mkdir("log")  
    
    if not os.path.exists("log/count_log.txt"):
        f = open("log/count_log.txt", 'w', encoding = "utf8")
        f.write("기록이 시작됩니다\n")
        f.close
    
    with open("log/count_log.txt", 'a', encoding = "utf8") as f:
        import random, datetime
        for i in range(1, 11):
            stamp = str(datatime.datetime.now())
            value = random.random() * 1000000
            log_line = stamp + "\t" + str(value) + "값이 생성되었습니다" + "\n"
            f.write(log_line)
    ```
- ### Pickle
  - 파이썬의 객체를 영속화(persistence)하는 built-in 객체
  - 데이터, object 등 실행중 정보를 저장 -> 불러와서 사용
  - 파이썬에 특화된 binary 파일
   ```python
   import pickle

   f = open("list.pickle", "wb")   # wb : write binary
   test = [1, 2, 3, 4, 5]
   pickle.dump(test, f)  #dump : test를 f에 저장해라
   f.close() 

   f = open("list.pickle", "rb")   # rb : read binary
   test_pickle = pickle.load(f)  #load : f에 저장된거 풀기
   print(test_pickle)
   f.close()
   ```
   - class 에도 사용 가능
     ```python
     import pickle

     class Multiply(object):
      def __init__(self, multiplier):
          self.multiplier = multiplier
    
      def multiply(self, number):
          return number * self.multiplier
    
      muliply = Multiply(5)
      muliply.multiply(10)

      f = open("multiply_object.pickle", "wb")
      pickle.dump(multiply, f)
      f.close()

      f = open("multiply_object.pickle", "rb")
      multiply_pickle = pickle.load(f)
      multiply_pickle.multiply(5)
      ```
