#늦게 과제 제출해서 죄송합니다..
def bigchange_text(list):

    changelist = ord(list)
    newlist = changelist + 32
    return(chr(newlist))

def smallchange_text(list):
    changelist = ord(list)
    newlist= changelist - 32
    return(chr(newlist))


def main():
    while True:
        try:

            bigtext = ["A", "B", "C", "D", 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            smalltext =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
                            't','u'',v','w','x','y','z']
            a=input(str("영문자 한 개를 입력하시오"))



            if a in bigtext:
                    print(bigchange_text(a))

            elif a in smalltext:
                    print(smallchange_text(a))
        except:
            print("한개의 문자열이 아닙니다.")


if __name__=="__main__":
    main()



