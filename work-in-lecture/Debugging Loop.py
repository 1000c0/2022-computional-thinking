from unicodedata import decimal


print("input decimal number: ",)
decimal = int(input())
result = ""
loop_counter = 0
while (decimal > 0):
    temp_decimal_input = decimal
    temp_result_input = result

    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result 


    
   # print("----------", loop_counter, "loop value check----------")      # 18줄 19줄은 같은 기능함 
    print(f"---------- {loop_counter} loop value check----------")        # f-string으로 구현
    print("Initial decimal:", temp_decimal_input, 
    ", Remainder:", remainder,
    ", Initial result", temp_result_input)
    print("Output decimal:", decimal,
    "Output result:", result)
    print("-----------------------------------------------------")
    print("")

    loop_counter += 1
print("Binary number is", result)

