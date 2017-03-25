import requests
from bs4 import BeautifulSoup
import re
import sendMail
import WorkInTime
import time
from datetime import datetime

class item:
    def __init__(self, name, min, url):
        self.__name = name
        self.__min = min
        self.__url = url

    def update(self, min):
        self.__min = min

    def minPrice(self):
        return self.__min

    def url(self):
        return self.__url

    def name(self):
        return self.__name


def checkToday(item):  #
    login_seesion = requests.Session()
    #url = 'https://www.amazon.cn/gp/goldbox/ref=gbps_ftr_s-4_0925_page_1?gb_f_GB-SUPPLE=enforcedCategories:2127215051,dealTypes:LIGHTNING_DEAL,sortOrder:BY_PRICE_ASCENDING&pf_rd_p=6b65ba24-2cb9-4da9-ab4e-05f723100925&pf_rd_s=slot-4&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=ZEJN83825GMPTYDYDCF4'
    #z 秒杀

    #SanDisk 64G
    print(item.url())
    f = login_seesion.get(item.url())
    #print(f.content.decode())

    soup = BeautifulSoup(f.content.decode(), "html.parser")
    #print(soup.prettify())
    #span class="a-size-medium a-color-price"
    min = 9999
    for price in soup.findAll(attrs={"class": "a-size-medium a-color-price"}):
        priceNow = float(price.text.split('￥')[1].replace(',',''))
        if min > priceNow:
            min = priceNow

    if min < item.minPrice():
        item.update(min)
        sub = item.name() + '现价: ' + str(item.minPrice())
        sendString = item.url() + '\n'
        #sendMail.sendMail(sub, sendString)
        print(sub)
    #
    #print(checkReaded)
    '''
    charpName = ''
    links = url+'/book/2705.html\n'
    #print(soup.body.table)
    newFlag = False
    for td in soup.findAll(attrs={"class": "time"}):
        if int(td.text[-2:]) < datetime.now().day:
            # 第一行更新小于当前时间，表面没更新
            break
        else:#更新了
            newFlag = True
            break
    if newFlag:
        numOneCharp = True
        links = url+'/book/2705.html\n'
        for charp in soup.findAll(rel=re.compile(r'dealDetails')):
            if numOneCharp:
                numOneCharp = False
                if gzr.isNew(charp.text):   #找到更新章节名字
                    gzr.update(charp.text)
                else:   #跟新过了
                    break
            if not gzr.isNew(charp.text):   #最新章节
                links += url+charp['href']+'\n'
                pass
            else:                           #到了旧章节
                sendMail.sendMail(gzr.newCharp(), links)
                print(gzr.newCharp())
                print(links)
                break
    #print('well done')
    '''

print("zms正在运行")
sd64Url = 'https://www.amazon.cn/gp/product/B0199IZ9VS/ref=ox_sc_act_title_1?ie=UTF8&psc=1&smid=A1AJ19PSB66TGU'
sd64 = item('闪迪64Gtf', 110, sd64Url)
sd128Url = 'https://www.amazon.cn/gp/product/B00KAPYN58/ref=ox_sc_act_title_1?ie=UTF8&psc=1&smid=A1AJ19PSB66TGU'
sd128 = item('闪迪128Gtf', 210, sd128Url)
timeB = [['8:00', '22:00']]
timeWork = WorkInTime.WorkInTime(timeB, 60*60, 0)
'''
zturl = 'https://www.amazon.cn/gp/product/B01NBKTV5N/ref=ox_sc_act_title_1?ie=UTF8&psc=1&smid=A2QTCD7YRPQM71'
zt = item('zt', 311, zturl)
'''
while True:
    timeWork.relax()
    checkToday(sd64)
    checkToday(sd128)
