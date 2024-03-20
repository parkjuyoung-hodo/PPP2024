#원 면적,둘레 출력하는 프로그램(면적:소수점 2번쨰 ,둘레는 소수점 1번째)

radius=float(input("원 면적과 둘레를 구해드리겠습니다.반지름을 입력하시오:"))

circle_area=(radius**2)*3.14

circle_line=2*radius*3.14

print("원 면적={},원 넓이={}".format(round(circle_area,2),round(circle_line,1)))