import requests

'''
Response对象的属性：
r.status_code 状态码
r.text http 响应内容的字符串形式
r.encoding 从http header中猜测的编码方式
r.apparent_encoding 从内容中分析出的编码方式
r.content http 响应内容的二进制形式
'''


def get_code(url):
    # r = requests.get(url, params=null, **kwargs)
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.exceptions:
        return "产生异常"


if __name__ == '__main__':
    print(get_code("https://www.baidu.com"))
