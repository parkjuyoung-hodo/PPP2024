#칼로리 계산 프로그램(과제#04-03)를 수정하여, 총 칼로리를 계산하시오.(반복문, 사전 활용)

eat_gram=[10,20,30]
eat_fruit=['한라봉','딸기','바나나']

cal={'한라봉':5,'딸기':3,'바나나':7}

total_cal = 0

for eat_fruits in cal:
    total_cal_1=cal['한라봉']*eat_gram[0]

for eat_fruits in cal:
    total_cal_2=cal['딸기']*eat_gram[1]

for eat_fruits in cal:
    total_cal_3=cal['바나나']*eat_gram[2]

print(f"총 칼로리는 {total_cal_1+total_cal_2+total_cal_3}입니다")


