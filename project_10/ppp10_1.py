#수업시간 제시한 코드 혹은 본인이 작성한 코드를 활용하여, 칼로리 계산 프로 그램을 완성하시오. 식품별 칼로리 정보를 파일에서 읽어서 처리

def total_calorie(fruits_eat,fruits_cal_dic):
    total=0
    for fruit_name in fruits_eat:
        total += fruits_eat[fruit_name]*fruits_cal_dic[fruit_name] / 100
    return total

def read_cal_db(filename):
    database={}
    with open(filename,encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines[1:]:
            tokens = line.split(",")
            fruit_name = tokens[0]
            fruit_cal = int(tokens[1])
            database[fruit_name] = fruit_cal

    return database

def main():
    fruits_chose = {"쌈추": 100, '밀': 100}
    fruits_cal_dic=read_cal_db('calorie_db.csv')

    print(total_calorie(fruits_chose,fruits_cal_dic))

if __name__=="__main__":
    main()

