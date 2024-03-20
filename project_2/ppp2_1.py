#for i in range(1000):
    #c=int(input('섭씨 온도를 입력하세요:'))
    #F =c*1.8+32
    #print("화씨 온도는", F ,"입니다")

# 섭씨 30도와 0도를 화씨로 바꿀 수 있게 프로그램을 만드는 걸로 잘 못 이해했습니다
# 그래서 30도와 0도를 프로그램을 한 번 돌려도 구할 수 있게, 입력을 여러번 받기 위해 "for i in range():를 사용했습니다
# 다음 부터는 과제의도를 정확히 파악해서 제출하도록 하겠습니다.

temp_c=30
temp_f=(temp_c*1.8)+32
print("{}℃=>{}℉".format(temp_c,temp_f))


temp_c=0
temp_f=(temp_c*1.8)+32
print("{}℃=>{}℉".format(temp_c,temp_f))




