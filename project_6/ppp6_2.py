#if __name__=="main": 함수를 이용한 구구단 구하기

def main():
    dan= int(input("원하는 구구단 단을 적으시오:"))
    for i in range(9):
       print(f"{dan}*{(i + 1)}={dan * (i + 1)}")
if __name__=="__main__":
    main()





