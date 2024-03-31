#딸기 300g, 한라봉 150g 섭취하였을 때, 입력자료를 사전형으로 전달하면, 총 칼
#로리를 계산하는 함수를 만드시오. fruits={“딸기”: 300, “한라봉”: 150},
#fruits_calorie_dic={"한라봉": 50, "딸기": 34, "바나나": 77}. 과제 #06-01 활용. 함
#수명은 total_calorie(fruits, fruits_calorie_dic)

def total_calorie(fruits, fruits_calorie_dic):
    fruit_calorie_dic = {'한라봉': 50, '딸기': 34}
    fruits = {'딸기': 300, '한라봉': 150}
    total_cal_1 = 0
    totla_cal_2 =0
    total_cal=0

    total_cal_1 = fruits['한라봉'] * fruit_calorie_dic['한라봉']
    total_cal_2 = fruits['딸기'] * fruit_calorie_dic['딸기']
    total_cal= total_cal_1 + total_cal_2
    return total_cal

def main():
    print(total_calorie('fruits','fruits_calorie_dic'))

if __name__=="__main__":
    main()










