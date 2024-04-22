#2. 2001년부터 2022년까지 각 해마다 5월부터 9월까지 적산온도를 구하시오.  ㅋ
def real_col(filename,col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[0].split(',')]
        col_idx=header.index(col_name)
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset
def get_dat_ifs(values,conditions,criteria):
    dataset = []
    for rain,year in zip(values,conditions):
        if year == criteria:
            dataset.append(rain)
    return dataset
def gdd_season(tavg,month):
    total_gdd=0
    for temp,months in zip(tavg,month):
        if months in [5,6,7,8,9]:
            eff_temp = temp - 5
            if eff_temp < 0:
                eff_temp = 0
            total_gdd += eff_temp
            #total_gdd=sum([temp-5 if temp>5 else 0 for temp,month in zip (tavg,month) if month in [5,6,7,8,9]])

    return total_gdd
def main():
    tavg=real_col('weather(146)_2001-2022.csv','tavg')
    month=real_col('weather(146)_2001-2022.csv','month')



    print(f"GDD={gdd_season(tavg,month)}")

if __name__=="__main__":
    main()