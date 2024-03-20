# 두 지점 사이 구하기

x1=int(input("x1좌표를 입력하시오:"))
x2=int(input("x2좌표를 입력하시오:"))
y1=int(input("y1좌표를 입력하시오:"))
y2=int(input("y2좌표를 입력하시오:"))

import math
two_line=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("두 지점 사이의 길이는={}".format(round(two_line)))