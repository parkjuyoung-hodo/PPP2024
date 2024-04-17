def read_col(filename,col_name):
    dataset=[]
    with open(filename) as f:
        lines  =f.readlines()
        header = [x.strip() for x in lines[0].split(",")]#header 왜추가?
        #print(header)
        col_idx = header.index(col_name)
        #print(col_name,col_idx)
        for line in lines[1:]:
            tokens=line.split(",")
            rainfall=float(tokens[-3])  #근데 이래도 괜챃은가...? 인식 안할 것 같은뎀
            dataset.append(float(tokens[col_idx]))
    return dataset
def longest_rainday(rainfall):
    rain_event=[]
    prev_rain_count=0
    for rain in rainfall:
        if rain == 0:   #이건 0이면 ...?? 아 이게 해당 되면 prev_rain_count=0이 된다는 말인가..?
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count += 1
    return max(rain_event)
#rainfall float(token[-3])안 정의해도 괜찮은가
def max_rainfall_event(rainfall):   #비가 연속으로 올때 가장 많은 강수량
    rain_event = []
    prev_rain_count = 0
    for rain in rainfall:
        if rain == 0:
            if prev_rain_count > 0:
                rain_event.append(prev_rain_count)
            prev_rain_count=0
            prev_rain = 0
        else:
            prev_rain_count += 1
            prev_rain += 1  # prev_rain += rainfall ㅇ라고 적ㅇ
    return max(rain_event)
def top_rank(tmax,limit):
    return sorted(tmax)[-limit:][::-1]  #이 limits는 값은 이해할 수 없다
def sumifs(rainfall,months,conditions):
    total=0
    for i in range(len(rainfall)):
        rain=rainfall[i] # 이 i의 값에 6 7 8 이 반복적으로 들어가서 total값 출력..?
        month= months[i]
        if month in conditions:    #근데 rain이랑 month는 어떻게 아는겨..?
            total += rain
    return total
def get_dat_ifs(values,conditions,criteria):  #이거는 진짜 뭐지
    dataset = []
    for rain,year in zip(values,conditions):  #zip함수는  list1과 list2의 동일한 인덱스에 있는 요소들이 튜플로 묶여 변수에 할당되어 출력됩니다.
        if year == criteria:
            dataset.append(rain)
    return dataset
def read_col_year(weather_filename,col_name,year):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]  # header 왜추가?
        #print(header)  애를 print하면 왜 weather파일의 첫번째 줄만 출력되는가?
        col_idx = header.index(col_name)  #index가 문자열을 만들어주는건가?
        #print(col_name,col_idx)      #weather파일을 index로 읽은 다음에 그 index로 정의한 col_idx를 출력하는건가? #rainfall 9c출력
        for line in lines[1:]:
            tokens = line.split(",")
            y=int(tokens[0])
            if y == year:
                dataset.append(float(tokens[col_idx]))

    return dataset

def main():
    rainfall =read_col("weather(146)_2022-2022.csv",'rainfall')  #index때문에 token[-3]같은거 안써도 괜ㅊ낳은건ㄴ가
    months_float=read_col("weather(146)_2022-2022.csv",'month')
    months=[int(x)for x in months_float]
    tmax = read_col('weather(146)_2022-2022.csv','tmax')


    print(f"최장연속강우일수는{longest_rainday(rainfall)}일입니다.")
    print(f"비가 연속으로 올 떄 최대강수량은{max_rainfall_event(rainfall):.1f}입니다.")
    print(f"가장더운날 top3는 {top_rank(tmax,3)}mm입니다.")
    print(f"2022년 6,7,8월 여름철 총 강수량은{sumifs(rainfall,months,[6,7,8]):.1f}mm 입니다")

    rainfall_all=read_col('weather(146)_2001-2022.csv','rainfall')
    #year_all=read_col_year('weather(146)_2001-2022.csv','year')
    #rainfall_2021=get_dat_ifs(rainfall_all,year_all,2021)

    rainfall_2021=read_col_year('weather(146)_2001-2022.csv','rainfall',2011)
    print(f"2021,2022년의 총 강수량은{sum(rainfall_2021):1f}mm입니다")

if __name__=="__main__":
    main()

