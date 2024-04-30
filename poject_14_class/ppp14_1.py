import requests

def submit(day: str, locate: float, avg_diff: str, min_diff: float, max_diff: str) -> None:
    URL = 'https://ieilms.jbnu.ac.kr/mypage/data/dataDown.jsp?user_id=82943&id=481763&group_id=63250'
    PARAMS = {
        '날짜': day,
        '지점': locate,
        '평균기온(℃)': avg_diff,
        '최저기온(℃)': min_diff,
        '최고기온(℃)': max_diff,
    }

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    if r.status_code != 200:
        print("과제가 정상적으로 제출되지 않았습니다.")


if __name__ == "__main__":
    submit("박주영", 340.1, "2011-08-04", 25.2, "1978-01-04")