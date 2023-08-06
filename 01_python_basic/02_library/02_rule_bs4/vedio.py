import requests
import os

# 爬取不了 我猜测是反爬了

if __name__ == '__main__':
    url = "https://f.us.sinaimg.cn/000KWJn4lx07kX2cXSCs01040203N7910k030.mp4?label=mp4_720p&template=1280x720.28&media_id=845bab0689e52b9d836c2b108ea70570&tp=:YTkl0eM8&us=0&ori=1&bf=2&ot=h&lp=000038exa6&ps=mZ6WB&uid=7aBCdK&ab=11243-g12&Expires=1691027877&ssig=3FYDavQAUF&KID=unistore,video"

    root = "F://sss//"
    path = root + url.split('/')[-1]
    try:
        r = requests.get(url)
        # print(r.status_code)
        r.raise_for_status()
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("成功")
        else:
            print("文件已存在")
    except:
        print("Error")


