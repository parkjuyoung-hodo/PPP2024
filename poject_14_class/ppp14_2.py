import requests

URL="https://ieilms.jbnu.ac.kr/mypage/data/dataDown.jsp?user_id=82943&id=481763&group_id=63250"

data={'code':'mobile1'}

with open("C:\Users\user\OneDrive\문서\GitHub\ta_20240429021144 (3).csv", 'w', encoding="UTF-8") as f:
    res = requests.post(URL,data= data)
    res.encoding='UTF-8'
    f.write(res.text)
