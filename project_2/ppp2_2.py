#h= int(input("키(cm)를 입력하시오:"))
#H= h*0.01
#w= int(input("몸무게(kg)을 입력하시오: "))
#bmi = w // (H**2)
#print("BMI:", bmi )
#if bmi >25:
    #import webbrowser
    #webbrowser.open("https://www.youtube.com/watch?v=3VouSaW_LPw")
    #print("BMI가 표준 이상입니다.")
#if bmi>=18.5 and bmi<=25:
    #print("BMI가 표준입니다.")
#if bmi<18.5:
    #print("BMI가 표준 이하입니다.")

weight=60
height=170
BMI = weight // ((height/100)*(height/100))
print('BMI={}'.format(BMI))