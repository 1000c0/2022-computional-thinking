decimal = int(input("십진수를 입력하세요: "))
result = ""

while decimal > 0 :
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
    print(f" decimal value : {decimal}")
    
print(result)
