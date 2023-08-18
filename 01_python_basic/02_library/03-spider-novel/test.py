import requests
import bs4
import os

base_url = 'https://m.blwenku123.org/61/61264_'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}
page_num = 1
max_page = 9
file_path = '1.txt'
dir_url = 'https://m.blwenku123.org/61/61264_1'
re = requests.get(dir_url)
re.encoding = re.apparent_encoding
print(re.text)

'''
soup = bs4.BeautifulSoup(re.content, 'html.parser')
links = soup.select('li')
while page_num <= max_page:
    dir_url = f'{base_url}{page_num}'
    re = requests.get(dir_url, headers=headers)
    re.encoding = re.apparent_encoding
    soup = bs4.BeautifulSoup(re.content, 'html.parser')
    links = soup.select('.chapters li a')
    try:
        with open(file_path, 'w') as file:
            for link in links:
                file.write(link['href'] + '\n')
    except Exception as e:
        print(e)
    page_num = page_num + 1
'''
