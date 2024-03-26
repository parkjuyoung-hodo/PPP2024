#if __name__=="__main__"": 함수를 이용한 화씨를 섭씨로 바꾸는 프로그램

def main():
    temp_c = int(input("섭씨온도를 입력하세요:"))
    temp_f = (temp_c * 1.8) + 32
    print('{}℃=>{}℉'.format(temp_c, temp_f))
if __name__=="__main__":
    main()