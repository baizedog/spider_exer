import requests

if __name__ == '__main__':
    ip = '58.211.2.79'
    url = "http://m.ip138.com/ip.asp?ip="
    print("hello")
    # kv = {'ip': ip, 'action': '2'}
    try:
        r = requests.get(url + ip, timeout=5)
        # print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[-500:])
    except:
        print("Error")

