import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://python123.io/ws/demo.html"
    try:
        r = requests.get(url,timeout=5)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        date = r.text
        soup = BeautifulSoup(date, "html.parser")
        # print(soup)
        for sibling in soup.a.previous_siblings:
            print(sibling)

    except:
        print("Error")
