#삼각형 별 그리기


n=int(input('별의 개수를 적어주세요:'))

for i in range(n):
    star="*"
    print(f"{(i+1)*(star)}")