# 23학번 임서영언니 도움으로 16과제를 해결 하였습니다..
#늦게 과제 제출해서 죄송합니다..
def toggle_text(text:str)->str:
    toggle =""
    for item in text:
        if item>="a" and item <= "z":
            toggle += chr(ord(item)-32)
        elif item >= "A" and item <= "Z":
            toggle += chr(ord(item)+ 32)
        else:
            toggle += item
    return toggle

def main():
    text= input("문자열을 입력하세용")
    print(toggle_text(text))

if __name__ =="__main__":
    main()


