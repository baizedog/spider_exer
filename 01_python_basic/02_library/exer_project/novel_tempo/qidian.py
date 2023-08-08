import requests
import re
import bs4
# 爬取起点文学
url = 'https://www.qidian.com/book/1037435401/'

r = requests.get(url)
r.encoding = r.apparent_encoding
soup = bs4.BeautifulSoup(r.content, 'html.parser')
book_list = []
for title in soup.select('.chapter-name'):
    name = title.text
    chapter_url = title['href']
    book_list.append({name: chapter_url})

for book in book_list:
    print(book.keys())
    print(book.values())
