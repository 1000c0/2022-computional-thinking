# Python data handling

## CSV(Comma Seperate Values)
- 필드를 쉼표로 구분한 텍스트 파일
- 엑셀 양식의 테이처를 프로그램에 상관없이 쓰기 위한 데이터 형식
- 탭, 빈칸으로 구분하기도 함, 각각 TSV와 SSV
- 파일 읽기 예제
  ```python
  line_counter = 0  # 파일의 총 줄수를 세는 변수
  data_header = []  # data의 필드값을 저장하는 list
  customer_list = []  # cutomer 개별 List를 저장하는 List

  with open("customers.csv") as customer_data:  # customer.csv 파일을 customer_data 객체에 저장

      while 1:
        data = customer_data.readline()  # customer.csv에 한줄씩 data 변수에 저장
        if not data:
            break  # 데이터가 없을 때, Loop 종료
        if line_counter == 0:  # 첫번째 데이터는 데이터의 필드
            data_header = data.split(
                ","
            )  # 데이터의 필드는 data_header List에 저장, 데이터 저장시 “,”로 분리
        else:
            customer_list.append(
                data.split(",")
            )  # 일반 데이터는 customer_list 객체에 저장, 데이터 저장시 “,”로 분리
        line_counter += 1

  print("Header :\t", data_header)  # 데이터 필드 값 출력
  for i in range(0, 10):  # 데이터 출력 (샘플 10개만)
      print("Data", i, ":\t\t", customer_list[i])
  print(len(customer_list))  # 전체 데이터 크기 출력
  ```
- 파일 쓰기 예제
  ```python
  line_counter = 0
  data_header = []
  employee = []
  customer_USA_only_list = []
  customer = None

  with open("customers.csv", "r") as customer_data:
      while 1:
          data = customer_data.readline()
          if not data:
              break
          if line_counter == 0:
              data_header = data.split(",")
          else:
              customer = data.split(",")
              if customer[10].upper() == "USA":  # customer 데이터의 offset 10번째 값
                  customer_USA_only_list.append(customer)  # 즉 country 필드가 “USA” 것만
          line_counter += 1  # sutomer_USA_only_list에 저장

  print("Header :\t", data_header)
  for i in range(0, 10):
      print("Data :\t\t", customer_USA_only_list[i])
  print(len(customer_USA_only_list))

  with open("customers_USA_only.csv", "w") as customer_USA_only_csv:
      for customer in customer_USA_only_list:
            customer_USA_only_csv.write(",".join(customer).strip("\n") + "\n")
            # cutomer_USA_only_list 객체에 있는 데이터를 customers_USA_only.csv 파일에 쓰기
  ```

- ### 객체로 CSV 처리
  - Text파일 형채로 데이처 처리시 문장 내에 들어가 있는 쉼표 등에 대해 전처리 과정 필요

- ### CSV 객체 활용
  ```python
  import csv

  reader = csv.reader(f, delimeter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)  
  ```
  Attribute | Default | 의미 |
  |------|-----|-----|
  |delimeter | , | 글자를 나누는 기준 |
  |lineterminator | \r\n | 줄 바꿈 기준 |
  |quotechar | " | 문자열을 둘러싸는 신호 문자 |
  |quoting | QUOTE_MINIMAL | 데이터 나누는 기준이 quotechar에 의해 둘러싸인 레벨 |

  ```python
  import csv

  seoung_nam_data = []
  header = []
  rownum = 0

  with open("korea_foot_traffic_data.csv", "r", encoding="cp949") as p_file:
    csv_data = csv.reader(p_file)  # csv 객체를 이용해서 csv_data 읽기
    for row in csv_data:  # 읽어온 데이터를  한 줄씩 처리
        if rownum == 0:
            header = row  # 첫 번째 줄은 데이터 필드로 따로 저장
            location = row[7]
            # “행정구역”필드 데이터 추출, 한글 처리로 유니코드 데이터를 cp949로 변환
        if location.find(u"성남시") != -1:
            seoung_nam_data.append(row)
        # ”행정구역” 데이터에 성남시가 들어가 있으면 seoung_nam_data List에 추가
        rownum += 1

  with open("seoung_nam_foot_traffic_data.csv", "w", encoding="utf8") as s_p_file:
    writer = csv.writer(s_p_file, delimiter="\t", quotechar="'", quoting=csv.QUOTE_ALL)
    # csv.writer를 사용해서 csv 파일 만들기 delimiter 필드 구분자
    # quotechar는 필드 각 데이터는 묶는 문자, quoting는 묶는 범위
    writer.writerow(header)  # 제목 필드 파일에 쓰기
    for row in seoung_nam_data:
        writer.writerow(row)  # seoung_nam_data에 있는 정보 list에 쓰기
  ```

#
## Web
- 데이터 송수신을 뒤한 http 프로토콜 사용
- 데이터를 표시하기 위해 HTML 형식 사용


### HTML(Hyper Text Markup Language)
- 웹 상의 정보를 구조적으로 표현하기 위한 언어
- 제목, 단락, 링크 등의 요소 표시를 위해 Tag 사용  
- 모든 요소들은 <> 안에 둘러 쌓여 있음 
- 트리 모양의 포함 관계
- 웹 페이지의 HTML 소스파일은 컴퓨터가 다운 받은 후 웹 브라우저가 해석/표시
- html 구조
  ```
  <html> - <head> - <title> - <body> - <p> 구조
 
  <!doctype html>
   <html>
    <head>
     <title> Hello </title> # 모든 요소들은 <> 안에 둘러싸인다
     <body>
      <p>Hello World!</p>
     </body>
   </html>  
  ```

### 정규식(regular expression)
- 정규 표현식, regexp 또는 regex라고 불림
- 복잡한 문자열 패턴을 정의하는 문자 표현 공식
- 특정한 규칙을 가진 문자열의 집합을 추출
- 기본 문법
  - 문자 클래스 [] : [와 ] 사이의 문자들과 매치
    ex) [abc] 해당 글자에 a, b, c 중 하나가 있다. "a", "before", "mac"
  - " - " : 사용 범위를 지정 
    ex) [a-zA-Z]는 알파벳 전체, [0-9]는 숫자 전체
  - 메타 문자: 정규식 표현을 위해 다른 용도로 사용되는 문자
    ex) . ^ $ * + ? {} [] \ | ()
     - . : 줄바꿈 문자인 \을 제외한 모든 문자와 매치 ex) a[.]b
     - *: 앞에 있는 글자를 반복해서 나올 수 있음 ex) tomor*ow  
     - +: 앞에 있는 글자를 최소 1회 이상 반복
     - {m,n} : 반복횟수 지정
     - ? : 반복 횟수가 1회
     - | : or 
- 정규식 in python
  - re 모듈 사용
  - search 함수는 한개만 찾기
  - findall 함수는 전체 찾기  
  - 추출된 패턴은 tuple로 반환
  ```python
  import urllib.request  # urllib 모듈 호출
  import re

  url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"  # url 값 입력
  html = urllib.request.urlopen(url)  # url 열기
  html_contents = str(html.read().decode("utf8"))  # html 파일 읽고, 문자열로 변환

  url_list = re.findall(r"(http)(.+)(zip)", html_contents)
  for url in url_list:
    print("".join(url))  # 출력된 Tuple 형태 데이터 str으로 join
  ```

### XML(eXtensible Markup Language)
- 데이터 구조와 의미를 설명하는 TAG를 사용하여 표시하는 언어
- TAG와 TAG 사이에 값이 표시되고, 구조적인 정보 표현 가능
```
<?xml version="1.0"?> 
<고양이>
  <이름>나비</이름> 
  <품종>샴</품종>
  <나이>6</나이> 
  <중성화>예</중성화>
  <발톱 제거>아니요</발톱 제거> 
  <등록 번호>Izz138bod</등록 번호> 
  <소유자>이강주</소유자>
</고양이>
```
- beautifulsoup 모듈
  - 데이터 다운로드
    ```python
    from bs4 import BeautifulSoup

    with open("books.xml", "r", encoding="utf8") as books_file:
        books_xml = books_file.read()  # File을 String으로 읽어오기
    
    soup = BeautifulSoup(books_xml, "lxml")    # xml 모듈을 사용해서 데이터 분석
    
    for book_info in soup.find_all("author"):  # author가 들어간 모든 element 추출
        print(book_info)
        print(book_info.get_text())
    ```

### JSON(JavaScript Obiect Notation)
- 데이터 용량이 적고, code로의 전환이 쉬움
- json 모듈을 사용하여 손 쉽게 파싱 및 저장 가능
- 데이터 저장 및 읽기는 dict type과 상호 호환 가능

- JSON Read
  - JSON 파일 구조 확인 -> 읽어옴 -> Dict type처럼 처리
  - json 파일
    ```json
    {"employees":[
      {"firstName":"John", "lastName":"Doe"},
      {"firstName":"Anna", "lastName":"Smith"},
      {"firstName":"Peter", "lastName":"Jones"}
    ]}
    ```

  ```python
  import json

  with open("json_example.json", "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data["employees"])
  ```
- JSON Write
  - Dict Type으로 데이터 저장 -> json 모듈로 Write
   ```python
   import json

   dict_data = {'Name' : 'Zara', 'Age' : 7, 'Class' : 'First'}
   with open("data.json", "w") as f:
    json.dump(dict_data, f)
   ```
