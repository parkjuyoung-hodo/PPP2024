#1. 2001년부터 2022년까지 각각 최대일교차가 난 날짜와 일교차를 표시하시오
def read_col(filename,col_name):
    dataset = []
    with (open(filename) as f):
        lines = f.readlines()
        header = [x.strip() for x in lines[0].split(",")]
        col_idx = header.index(col_name)
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))

        return dataset


def main():
    tmax=read_col('weather(146)_2001-2022.csv','tmax')
    tmin=read_col('weather(146)_2001-2022.csv','tmin')
    year=read_col('weather(146)_2001-2022.csv','year')
    month=read_col('weather(146)_2001-2022.csv','month')
    day=read_col('weather(146)_2001-2022.csv','day')

    temp_diff=[tx-tn for tx,tn in zip(tmax,tmin)]   # 최대 일교차

    max_idx=0
    max_diff_temp = 0
    i=0

    for td in temp_diff:
        if max_diff_temp < td:
            max_diff_temp = td
            max_idx = i
        i += 1

    print(f"일교차가 가장 큰 날짜는 , 최대 일교차는 {max(temp_diff):.1f}C입니다")
    max_idx = temp_diff.index(float(max(temp_diff)))
    print(f" 일교차가 가장 큰 날짜는 {year[max_idx]}/{month[max_idx]:02d}/{day[max_idx]},최대 일교차는 {max(temp_diff):.1f}")

if __name__=="__main__":
    main()