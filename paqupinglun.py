import requests
import time
import re

class Taobaospider(object):
    def __init__(self):
        self.url = 'https://chaoshi.detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.4b2f33a4jY0mLg&id=589539133369&areaId=350200&user_id=725677994&cat_id=2&is_b=1&rn=b66601690b72450353a83d8bcba42f21'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        self.offset = 1

    def start_request(self):
        print('正在爬取第%d页...' % self.offset )
        content = requests.get(self.url,headers=self.headers).content.decode('gbk')
        time.sleep(1)
        self.content_re(content)
        print(content)

    def content_re(self,content):
        rateDate = re.findall(r'"tm-rate-date":"(.*?)"',content)
        rateContent = re.findall(r'"tm-rate-fulltxt":"(.*?)"',content)
        print(rateDate,rateContent)

if __name__ == '__main__':
    spider = Taobaospider()
    spider.start_request()
