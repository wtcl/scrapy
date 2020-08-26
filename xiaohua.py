#coding:utf-8
import request
from bs4 import BeautifulSoup

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
}
for i in range(0,100):
    url = 'http://xiaohua.zol.com.cn/detail15/{}.html'.format(i)
    html = request.get(url, headers=headers)
    # html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'lxml')
    if html.status_code==200:

        title = soup.select(".article-title")[0].text.replace(' ', '')
        content = soup.select(".article-text")[0].text.replace(' ', '')
        with open('D:/desktop/xh.txt', 'a',encoding='utf-8') as f:
            f.write(title)
            f.write(content)
            f.write('\n\n')
            f.close()
        print(title, content)
    else:
        continue
