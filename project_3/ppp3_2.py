#BMI 구하는 공식

weight=float(input("몸무게(kg)를 입력하시오:"))
height=float(input("키(cm)를 입력하시오:"))
import math
BMI=weight/math.pow(height*0.01,2)

print('BMI는{}입니다'.format(round(BMI)))
