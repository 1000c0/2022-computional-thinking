# Logging Handling
- 프로그램 실행 중 일어나는 정보를 기록하기
- 실행 시점에 남겨야 핱는 기록, 개발 시점에 남겨야 하는 기록

#
## Logging Level
- 프로그램 진행 상황에 따라 다른 level의 Log 출력
- 개발 시점, 운영 시점 마다 다른 Log가 남을 수 있도록 지원
- 기본으로 세팅되있는 level은 warning

Level|개요|
|------|---|
|debug|개발시 처리 기록을 남겨야 하는 로그 정보 남김|
|info|처리가 진행되는 동안의 정보 남김|
|warning|사용자가 잘못 입력한 정보 또는 처리는 가능하나 의도치 않은 정보가 들어왔을 때 알림|
|error|잘못된 처리로 에러가 났지만 프로그램은 동작이 가능함을 알림|
|critical|잘못된 처리로 데이터 손실 또는 프로그램 동작 불가능을 알림|

```python
import logging

logger = logger.getLogger("main")         #Logger 선언 
stream_hander = logging.StreamHandler()   # Logger의 output 방법 선언
logger.addHandler(stream_hander)          #Logger의 output 등록

logger.setLevel(logging.DEBUG)            # level 설정을 DEBUG로 -> 5개 다 출력 
logger.debug("틀렸어")
logger.info("확인해")
logger.warning("조심해")
logger.error("에러났어")
logger.critical("망했다....")

logger.setLevel(logging.CRITICAL)          # level 설정을 CRITICAL로 -> "망했다"만 출력 
logger.debug("틀렸어")
logger.info("확인해")
logger.warning("조심해")
logger.error("에러났어")
logger.critical("망했다")
```

- basicConfig
  - 기본 level 설정하는 방식
  ```python
  import logging

  logger = logger.getLogger("main")  
  logging.basicCOnfig(level = logging.DEBUG)  #기본 level을 DEBUG로 설정
  logger.setLevel(logging.CRITICAL)           #set level을 바꾼다

  logger.debug("틀렸어")
  logger.info("확인해")
  logger.warning("조심해")
  logger.error("에러났어")
  logger.critical("망했다....")
  ```

#
## configparser
- 프로그램 실행 설정을 file에 저장
- Section, Key, Value 값의 형태로 설정된 설정 파일 이용
- 설정 파일을 Dict Type으로 호출 후 사용

- ### config file
  - Section은 대괄호[] 사용
  - 속성은 Key : Value 또는 Key = Value
  ```
  [SectionOne]      
  status : Single
  Name : Mac
  Value : Yes
  Age : 23
  Single : True

  [SectioTwo]
  FavoriteFood : steak

  [SectionThree]
  FavoriteColor : silver
  ```

- ### configparser file
  ```python
  import configparser
  config = configparser.ConfigParser()
  config.sections()

  config.read('example.cfg')
  config.sections()

  for key in config['SectionOne']:
    print(key)

  config['SectionOne']["status"]
  ```

## argparser
- Console 창에서 프로그램 실행시 Setting 정보를 저장
- Command-Line Option 이라고 부름
  
```python
import argparse

parser = argparse.ArgumentParser(description = 'Sum two integers.')

parser.add_argument('-a', "--a_value", dest = "A_value", help = "A integers", type = int)
              #짧은 이름--긴 이름-------표시명-------------Help 설명--------- Argument Type
parser.add_argument('-b', "--b_value", dest = "B_value", help = "B integers", type = int)

args = parser.parse_args()
print(args)
print(args.a)
print(args.b)
print(args.a + args.b)
'''
python arg_sum.py -a 10 -b 20
Namespace(a = 10, b = 20)
10
20
30
'''
```

#
## Logging 적용하기
- Logging formatter
  - Log의 결과값의 format 지정 가능
    ```python
    formatter = logging.Formatter ('%(asctime)s %(levelname)s %(process)d %(message)s')

    #==> 2018-01-18 22:47:04, 385 INFO 4439 HERE WE ARE
    #날짜와 시간(%(asctime)s) : 2018-01-18 22:47:04
    #LevelName(%(levelname)s) : INFO
    #프로세스 ID(%(process)d) : 4439
    #메세지(%(message)s) : HERE WE ARE
    ```
- Log config file
  - 사전에 setting 가능하다
  ```python
  logging.config.fileConfig('logging.conf')
  logger = logging.getLogger()
  ```  
