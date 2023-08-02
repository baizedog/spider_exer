import requests
import os

if __name__ == '__main__':
    root = "F://sss//"
    url = "https://wx2.sinaimg.cn/mw690/006qpfgmly1hca2js6tabj321a31ye82.jpg"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                r = requests.get(url)
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已经存在")
    except:
        print("发生异常")

