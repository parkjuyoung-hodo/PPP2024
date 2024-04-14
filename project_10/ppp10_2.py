#기상자료를 받아서 연 평균 기온(일평균 기온의 연평균), 5mm이상 강우일수, 총 강우량을 구하시오.
def read_year_temp(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            tavg=float(tokens[4])
            results.append(tavg)
    return results

def read_rain_day(filename):
    results=[]
    with open(filename) as f:  # 5mm 이상 강우일 수
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            rainfall=float(tokens[-3])
            rainfall >5 == results.append(rainfall)


    return results

def read_total_rain(filename):
    result=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:    #강우량
            tokens=line.split(",")
            rainfalls=float(tokens[-3])
            result.append(rainfalls)
    return result

def main():

    tavg=read_year_temp('weather(146)_2022-2022.csv')
    rainfall=read_rain_day('weather(146)_2022-2022.csv')
    rainfalls=read_total_rain('weather(146)_2022-2022.csv')
    print(f'연평균 기온은 {sum(tavg)/len(tavg):1f}입니다.')
    print(f'5mm이상 강우 일수는 {len(rainfall)}일입니다')
    print(f'총 강우량은 {sum(rainfalls)}mm 입니다.')



if __name__=="__main__":
    main()




