# 1-n까지 리스트를 돌려주는 함수를 만드시오. 함수는 get_range_list(n)
def get_range_list(first,n):
    first=1
    list=[]
    for i in range(0,n):
        list.append(i+1)

    return list

def main():
    n=int(input("리스트에 들어갈 마지막 정수 n을 입력해주세요:"))
    print(get_range_list(0,n))
if __name__=='__main__':
    main()
