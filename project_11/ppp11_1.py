def read_col(filename,col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[0].split(",")]#header 왜추가?
        #print(header)
        col_idx=header.index(col_name)

        #print(col_name,col_idx)
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset
def longest_rainday(rainfall):
    rain_event=[]
    prev_rain_count=0
    for rain in rainfall:
        if rain ==0:
            if prev_rain_count >0:
                rain_event.append(prev_rain_count)
            prev_rain_count = 0
        else:
            prev_rain_count+=1

    return max(rain_event)

def max_rainfall_event(rainfall):
    rain_event=[]
    prev_rain_count=0
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
def top_rank(values,limit):

    return sorted(values)[-limit:][::-1]
def sumifs(rainfall,months,conditions):
    total=0
    for i in range(len(rainfall)):
        rain=rainfall[i]
        month= months[i]
        if month in conditions:
            total += rain
    return total
def get_dat_ifs(values,conditions,criteria):
    dataset=[]
    for rain,year in zip(values,conditions):
        if year ==criteria:
            dataset.append(rain)
    return dataset
def read_col_year(weather_filename,col_name,year):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]  # header 왜추가?
        # print(header)
        col_idx = header.index(col_name)
        # print(col_name,col_idx)
        for line in lines[1:]:
            tokens = line.split(",")
            y=int(tokens[0])
            if y ==year:
                dataset.append(float(tokens[col_idx]))

    return dataset

def main():
    rainfall =read_col("weather(146)_2022-2022.csv",'rainfall')
    months_float=read_col("weather(146)_2022-2022.csv",'month')
    months=[int(x)for x in months_float]

    #tmax = read_col('weather(146)_2022-2022.csv''tmax')


    print(f"최장연속강우일수는{longest_rainday(rainfall)}일입니다.")
    print(f"비가 연속으로 올 떄 최대강수량은{max_rainfall_event(rainfall):.1f}입니다.")
    #print(f"가장더운날 top3는 {top_rank(tmax,3)}mm입니다.")
    print(f"2022년 6,7,8월 여름철 총 강수량은{sumifs(rainfall,months,[6,7,8]):.1f}mm 입니다")

    rainfall_all=read_col('weather(146)_2001-2022.csv','rainfall')
    year_all=read_col_year('weather(146)_2001-2022.csv','year')
    rainfall_2021=get_dat_ifs(rainfall_all,year_all,2021)

    rainfall_2021=read_col_year('weather(146)_2001-2022.csv','rainfall',2011)
    print(f"2021,2022년의 총 강수량은{sum(rainfall_2021):1f}mm입니다")

if __name__=="__main__":
    main()

