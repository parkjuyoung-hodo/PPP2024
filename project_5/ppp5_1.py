#입력받은 숫자로 구구단 출력하는 프로그램 만들기

dan=int(input("몇 단 을 원하십니까?"))

for i in range(9):
    print(f'{dan}*{i+1}={dan*(i+1)}')