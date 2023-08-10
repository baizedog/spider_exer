import random
import requests
import re
import time
import bs4

# 更换了url
table_url = 'https://www.biqu789.com/226/226104/73073228.html'
# table_url = 'https://www.biqu789.com/226/226104/'
base_url = 'https://www.beqege.cc/'
# headers = {
#       'User-Agent': '',
#       'Referer': 'https://cn.bing.com/',
#       # 'Sec-Ch-Ua': "'Not/A)Brand';v='99', 'Microsoft Edge';v='115', 'Chromium';v='115'",
#       'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
#       'Sec-Ch-Ua-Mobile': '?0',
#       'Sec-Ch-Ua-Platform': '"Windows"',
#       'Sec-Fetch-Dest': 'document',
#       'Sec-Fetch-Mode': 'navigate',
#       'Sec-Fetch-Site': 'cross-site',
#       'Sec-Fetch-User': '?1',
#       'Upgrade-Insecure-Requests': '1'
# }

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.beqege.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}


# 重写user-agent 增加随机性
UA = ["Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
      "Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot;Gecko/20100101 Firefox/38.0",
      "Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0",
      "Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
      "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
      "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
      "Mozilla/5.0 (Windows NT 6.1; rv:17.0) Gecko/20100101 Firefox/20.6.14",
      "Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
      "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
      "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
      "Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; Gecko/20100101 Firefox/38.0",
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96"
      " Safari/537.36 Edg/88.0.705.50",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 "
      "Edg/115.0.1901.188"
      ]

headers["User-Agent"] = random.choice(UA)

cookies = {
      'cf_clearance': '0Y25O94UlPpGvJWiJL4a38Q2yIZO2Cm_p8PPU2q0sI0-1691542071-0-1-7d988eb8'
                      '.dec96c3b.921f17c7-0.2.1691542071'
}


response_1 = requests.get(table_url, headers=headers, cookies=cookies)
# response_1 = requests.get(table_url)
response_1.encoding = response_1.apparent_encoding
soup = bs4.BeautifulSoup(response_1.content, "html.parser")
# print(soup.select("#content"))
print(response_1.text)
# 有简单的反爬
# print(response_1.request.headers)
print(response_1.status_code)
# 每一个章节的链接
# <dd><a href="/55869/744921.html">1、Chapter 1</a></dd>

# 前面 .表示任意字符 *表示这个任意字符重复任意次
# regex = "<dd><a href='(.*)'>"
# 获取html标签列表
# chapter_html_list = re.findall(regex, response_1.text)
# 存储章节url
# chapter_url_list = []
# for i in chapter_html_list:
#     url = base_url + i
#     chapter_url_list.append(url)
# print(chapter_url_list[0])
