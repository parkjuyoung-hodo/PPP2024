def median(nums):
    sorted_nums= sorted(nums)
    return median(nums)

def minmax(nums):
    return min(nums), max(nums)

def average(nums):
    return sum(nums)/len(nums)

def main():
    input_text = " 5,10,3,4,7"
    tokens = input_text.split(",")
    nums=[]
    sorted_nums=sorted(nums)
    for token in tokens:
        nums.append(int(token))
    median=nums[3]

    mn = minmax(nums)[0]
    mx = minmax(nums)[1]
    print("최솟값은",mn)
    print("최댓값은",mx)
    print("주어진 리스트는",sorted(nums))
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median))

if __name__=="__main__":
    main()


