import requests
import re
url = "https://www.beqege.cc/robots.txt"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36 Edg/115.0.1901.188 '

}
r = requests.get(url, headers=headers)
# r = requests.get(url)
print(r.status_code)
