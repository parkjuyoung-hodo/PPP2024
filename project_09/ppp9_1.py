def text2list(input_text):
    return [int(x) for x in input_text.split()]

def median(nums):
    sorted_nums =sorted(nums)
    return sorted_nums[len(nums)//2]


def average(nums):
    return sum(nums)/len(nums)

def main():
    with open('numbers1.txt') as f:
        lines=f.readlines()
        for line in lines:
            text = line.strip()
            nums=text2list(text)
            print("총개수는", len(nums))
            print('주어진 숫자의 평균{}'.format(average(nums)))
            print("주어진 숫자의 최댓값은", max(nums))
            print("주어진 숫자의 최솟값은", min(nums))
            print("주어진 숫자의 중앙값은 {}".format(median(nums)))
if __name__=="__main__":
    main()

