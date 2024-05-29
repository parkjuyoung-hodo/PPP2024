#2) ASCII 코드를 이용하여 카이사르 암호(Caesar cipher)를 구현하시오. 카이사르
# 암호는 그림과 같이 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 대치
# 하는 방법으로 3칸을 옮겼을 때, 오른쪽 아래 그림과 같다.

def caesar_encode(text: str, shift: int = 3) -> str:
    code = ""
    for item in text:
        code += (chr(ord(item) + shift) )
    return code

def caesar_decode(text: str, shift: int = -3) -> str:
    return "".join([chr(ord(item) + shift) for item in text])

def main():
    check = int(input("암호를 만들고 싶다면 1을, 해독하고 싶다면 0을 입력해주세요"))
    if check == 1:
        text = input("바꾸고 싶은 문자를 입력하세요:")
        print(f"{text} = > {caesar_encode(text)}")
    else:
        code = input("해독하고 싶은 암호를 입력하세요")
        print(f"{code} = > {caesar_decode(code)}")


if __name__ == "__main__":
    main()
