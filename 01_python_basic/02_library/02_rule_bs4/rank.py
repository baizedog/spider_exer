import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_univ_list(html, ulist):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            name = ''
            tds = tr('td')
            for td in tds:
                a_tag = td.find('a', class_='name-cn')
                if a_tag:
                    name = a_tag.get_text(strip=True)
            ulist.append([tds[0].string, name, tds[4].string])


def printlist(ulist, num):
    print("{:^10}\t{:^10}\t{:^10}".format("排名", "名称", "分数"))
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^10}\t{:^10}".format(u[0].strip(), u[1].strip(), u[2].strip()))


def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = get_html_text(url)
    fill_univ_list(html, uinfo)
    printlist(uinfo, 20)


if __name__ == '__main__':
    main()
