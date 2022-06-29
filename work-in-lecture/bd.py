print("당신이 태어난 년도를 입력하세요")
bd = int(input())
age = 2022 - bd + 1 

if age > 27:
    print("학생이 아닙니다")
elif age > 19:
    print("대학생")
elif age > 16: 
    print("고등학생")
elif age > 13: 
    print("중학생")
elif age > 7: 
    print("초등학생")    
else:
    print("학생이 아닙니다.")