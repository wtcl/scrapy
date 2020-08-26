#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
from urllib import parse
import os
import time

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
}

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

print("*****************************************************************")
print("**                                                             **")
print("**           公  众  号 ：分      享      儿                   **")
print("**                                                             **")
print("**                                                             **")
print("**          欢  迎  使  用  此  文  本  阅  读  器！           **")
print("**           （本软件版权归公众号分享儿所有！）                **")
print("**                                                             **")
print("**                                                             **")
print("**          欢  迎  关  注  公  众  号  分  享  儿！           **")
print("**                                                             **")
print("**                                                             **")
print("**                                                             **")
print("**                                                             **")
print("*****************************************************************")

name=input("请输入你所需要图片的关键字：")
name=parse.quote(name)
print("转码后："+name)
num=int(input("请输入你想要爬取的图片数（1表示30张，2表示60张..）:"))
path = input("请输入你想要存储图片的位置（如 D://desktop/图/）：")
mkdir(path)
i = 0

for j in range(num+1):
    url ='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=96&1598338162405='.format(
        name, name, j * 30)
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    pattern = re.compile(r'"thumbURL":"(.*?)\.jpg')
    urls = pattern.findall(str(soup))
    # print(urls)

    for u in urls:
        u = u.replace("amp;", '')
        html = requests.get(u, headers=headers)
        with open(path + '/' + str(i) + '.jpg', 'wb') as f:
            f.write(html.content)
            f.close()
            print(str(i) + ".jpg已下载完成！")
        i = i + 1
        if i%10==0:
            time.sleep(5)
