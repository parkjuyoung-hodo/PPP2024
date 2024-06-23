#ASCII 코드를 이용하여 입력받은 문자열을 대문자는 소문자로, 소문자는 대문자로 바꾸시오. 함수명은 toggle_text(text: str) -> st
def caesar_encode(text: str, shift: int = 3) -> str:
    code = ""
    for item in text:
        if "a" <= item <= "z":
            code += chr((ord(item) - ord("a") + shift) % 26 + ord("a")) # %는 몫을 구한 나머지를 구한 값 26은 알파벳 개수 그냥 수식이굼ㄴ,, 복잡한수학적ㅇㄴ,,
        elif "A" <= item <= "Z":
            code += chr((ord(item) - ord("A") + shift) % 26 + ord("A"))
        else:
            code += item
    return code
def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)

from tkinter import *
def process_text():
    input_original_text= str(original_text_input.get())
    input_encrypted_text= str(encrypted_text_input.get())
    encrypted_text_input.insert(0,str(caesar_encode(input_original_text,3)))
    original_text_input.insert(0,str(caesar_decode(input_encrypted_text,3)))
    return encrypted_text_input,original_text_input


window = Tk()
def main():
    global original_text
    global encrypted_text
    global original_text_input
    global encrypted_text_input

    window.title('서영언니가 도와준 Caesar cipher')

    original_text= Label(window, text ="문자")
    encrypted_text =Label(window, text ="암호")
    original_text.grid(row=0,column=0)
    encrypted_text.grid(row=1,column=0)

    original_text_input=Entry(window)
    encrypted_text_input=Entry(window)
    original_text_input.grid(row=0,column=1)
    encrypted_text_input.grid(row=1,column=1)

    original_button=Button(window, text="암호 설정",command=process_text)
    encrypted_button=Button(window, text="암호 해독",command=process_text)
    original_button.grid(row=2,column=0)
    encrypted_button.grid(row=2,column=1)

    window.mainloop()

if __name__=="__main__":
    main()
