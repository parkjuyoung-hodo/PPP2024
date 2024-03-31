#숫자 리스트를 매개변수로 받아서 평균을 구하시오. 함수는 average(nums)
def average(nums):
    x = int(input("리스트에 들어갈 첫번 쨰 정수를 적어주세요:"))
    z = int(input("리스트에 들어갈 두번 쨰 정수를 적어주세요:"))
    y = int(input("리스트에 들어갈 세번 쨰 정수를 적어주세요:"))
    average = (x + z + y) / 3

    return average
def main():
    nums = ['x', 'z', 'y']
    print(average(nums))
if __name__=="__main__":
    main()


