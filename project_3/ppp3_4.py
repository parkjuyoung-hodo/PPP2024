#사다리꼴을 구하는 공식

lower=int(input('사다리꼴 밑면의 길이를 입력하시오:'))
upper=int(input("사다리꼴 윗변의 길이를 입력하시오:"))
height=int(input('사다리꼴 높이의 길이를 입력하시오:'))

trapezoid_area=(lower+upper)*height/2

print('사다리꼴의 넓이={}'.format(trapezoid_area))