import requests

if __name__ == '__main__':
    try:
        url = "http://www.baidu.com/s"
        params = {'wd': '哔哩哔哩'}
        r = requests.get(url, params)
        r.encoding = r.apparent_encoding
        print(len(r.text))
    except:
        print("Error")
