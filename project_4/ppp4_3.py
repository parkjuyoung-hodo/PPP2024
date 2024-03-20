#딕셔너리 이용해서 칼로리 계산 프로그램
calories={'한라봉':0.5,'딸기':0.34,'바나나':0.77}

big_orange_weight=float(input("한라봉 먹은 g수를 압력하시오:"))
strawberry_weight=float(input("딸기 먹은 g수를 입력하시오:"))
banana_weight=float(input('바나나 먹은 g수를 입력하시오:'))


eat_big_orange=calories['한라봉']*big_orange_weight
eat_strawberry=calories['딸기']*strawberry_weight
eat_banana=calories['바나나']*banana_weight

total_calories=eat_big_orange+eat_strawberry+eat_banana

print('총 섭취한 칼로리는:{}'.format(total_calories))
