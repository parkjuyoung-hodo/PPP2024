#숫자 n이 주어졌을 때, 1부터 n까지의 합을 구하시오. 함수명은 sum_n(n)
print("1부터 n까지의 합을 구해드리겠습니다.")
n=int(input("n에 들어갈 정수를 적어주세요:"))
def sum_n(n):
    for i in range(n):
        return(f"{(1+n)*(n/2)}")

print(f"1부터 {n}까지의 합은 {sum_n(n)}입니다")



