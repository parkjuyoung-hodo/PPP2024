#사분면 구별하기
x=int(input("x 좌표 정수를 입력하시오:"))
y=int(input("y 좌표 정수를 입력하시오:"))

if x>0  and y>0:
    print("제 1사분면 입니다.")

elif x<0 and y<0:
    print("제 3사분면 입니다.")

elif x<0 and y>0:
    print("제 2사분면 입니다.")

else:
    print("제 4사분면 입니다.")
