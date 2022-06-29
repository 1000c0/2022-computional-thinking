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


