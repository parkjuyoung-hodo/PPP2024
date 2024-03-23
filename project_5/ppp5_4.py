#삼각함수 표 만들기

#0,15,30,45,60,75,90,105,120,135,150,165,180
import math
for i in range(13):
    c=i*15
    a_sin=math.sin((math.pi*((c)/180)))
    a_cos=math.cos((math.pi*((c)/180)))
    a_tan=math.cos((math.pi*((c)/180)))

    print(f'sin{c}:{round(a_sin,4)}\ncos{c}:{round(a_cos,4)}\ntan{c}:{round(a_tan,4)}')
