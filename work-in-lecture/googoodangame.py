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
