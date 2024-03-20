#BMI 계산
weight=float(input("체중을 입력하시오:"))
height=float(input("키(cm)를 입력하시오:"))
BMI=weight/(height*0.01)**2

if BMI>=23 and BMI<=24.9:
    print("비만 전 단계 입니다")

elif BMI>=25 and BMI<=29.9:
    print("비만 1단계 입니다")

elif BMI>=30 and BMI<=34.9:
    print("비만 2단계 입니다")

elif BMI>=35:
    print("비만 3단계 입니다")

else:
    print("비만이 아닙니다")
