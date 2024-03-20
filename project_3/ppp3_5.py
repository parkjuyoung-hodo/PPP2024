#과일마다 섭취g 받아서 칼로리 출력하기

big_orange_weight=float(input('한라봉을 먹은 양(g)은?:'))
strawberry_weight=float(input("딸기를 먹은 양(g)은?:"))
banana_weight=float(input("바나나를 먹은 양(g)은?:"))

print("과일을 먹은 총 칼로리(kal)={}".format((big_orange_weight*0.5)+(strawberry_weight*0.34)+(banana_weight*0.77)))

