#3) 초성 게임을 완성하시오. 유니코드를 이용하여, 주어진 단어 뭉치에서 단어를 하
# 나 선택하고, 초성을 제시한다. 사용자는 주어진 초성을 보고 주어진 단어를 맞추는
# 게임을 구현한다
import random
from tkinter import simpledialog

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="Test", prompt=text)
def get_chosung(text):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    chosung=[]
    for gulija in text:
        #print(gulija,(ord(gulija)))-ord("가")//588,CHOSUNG_LIST(ord(gulija)-ord('가'))
        chosung.append(CHOSUNG_LIST[(ord(gulija)- ord("가"))//588])

    return "".join(chosung)
def main():
    hidden_answer_list = ["내피땀눈물", "단팥빵", "호주","호두","주영"]
    num = random.randint(0,len(hidden_answer_list)-1)
    hidden_answer= hidden_answer_list[num]
    problem=get_chosung(hidden_answer)

    print(f"문제입니다, 주어진 초성은 {problem}입니다")

    answer = input("답은=>?")
    if answer == hidden_answer:
         print("정답입니다.")

    else:
         print("틀렸습니다")


if __name__=="__main__":
    main()