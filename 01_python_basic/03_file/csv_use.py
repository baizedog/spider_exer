import csv
import time

import pandas
from lxml import etree
import requests


def write(file, text):
    csv_file = open(file, 'a', newline='', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(text)
    csv_file.close()


def request(url):
    response = requests.get(url, timeout=10)
    time.sleep(2)
    response.encoding = 'utf-8'
    text_data = response.text
    res_html = etree.HTML(text_data.encode('utf-8'))
    return res_html


def spider():
    # 写标题
    head_href = ''
    title = ['drug_name', 'drug_id', 'drug_code']
    # 可以修改成自己的路径
    file = 'drug_data.csv'
    write(file, title)
    # 官网
    base_url = "https://www.ncbi.nlm.nih.gov"
    # 起始目录页
    queue_href = ["/mesh/1000048"]
    # 已经爬取过的网页
    end_href = []
    # 统计写入的数据量
    num = 0
    # 标记错误链接的重试次数
    tag = 0
    start_time = time.time()
    while queue_href:
        try:
            # 从队头拿去网页url
            head_href = queue_href[0]
            # url拼接
            url = base_url + head_href
            # 获取网页
            html = request(url)
            # 从网页上获取下一级子节点
            xpath = '//*[@id="maincontent"]/div/div[5]/div//@href'
            href_data = html.xpath(xpath)
            if len(href_data) > 0:
                for link in href_data:
                    if link not in end_href and link not in queue_href and link[:6] == "/mesh/":
                        queue_href.append(link)
            data_text = []
            # 从网页上获取name
            name_xpath = '//*[@id="maincontent"]/div/div[5]/div/h1/text()'
            name_data = html.xpath(name_xpath)
            data_text.append(name_data[0])
            # 获取 id
            id_xpath = '//*[@id="maincontent"]/div/div[5]/div/p/text()'
            id_data = html.xpath(id_xpath)
            if len(id_data) > 0:
                for i in id_data:
                    if "MeSH Unique ID: " in i:
                        drug_id = i.replace("MeSH Unique ID: ", "")
                        data_text.append(drug_id)
            # 获取 code
            code_xpath = '//*[@id="maincontent"]/div/div[5]/div/p/text()'
            code_data = html.xpath(code_xpath)
            if len(code_data) > 0:
                for i in code_data:
                    if "Tree Number(s): " in i:
                        ids = i.replace("Tree Number(s): ", "")
                        data_text.append(ids)
            # 将获取得到的 name id code 写入csv文件中
            write(file, data_text)
            num += 1
            print("已写入第" + str(num) + "个数据")
            queue_href.remove(head_href)
            end_href.append(head_href)
            tag = 0
        except:
            # 重试次等于5次就将错误的href保存到error_log.txt
            if tag == 10:
                queue_href.remove(head_href)
                end_href.append(head_href)
                file = open('../../file/error_log.txt', 'a', encoding='utf-8')
                file.write(head_href + "\n")
                file.close()
                tag = 0
                print("*" * 30)
                print("数据错误，已保存至txt！！！！！！")
                print("*" * 30)
            tag += 1
            # 保存queue_href 和end_href
            pandas.to_pickle(queue_href, "queue_href.pkl")
            pandas.to_pickle(end_href, "end_href.pkl")
            # 读取queue_href 和end_href
            end_href = pandas.read_pickle("end_href.pkl")
            queue_href = pandas.read_pickle("queue_href.pkl")
            zTime = time.time()
            print("*" * 30)
            print("已经用时: " + str(zTime - start_time), "秒")
            print("发生错误，程序5秒后开始运行")
            print("*" * 30)
            time.sleep(5)


if __name__ == '__main__':
    # 运行前可以修改一下保存路径
    spider()
