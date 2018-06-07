'''
Created on 2018年3月16日

@author: Xiaopeng
这个脚本是从所有的网页中提取每首歌曲乐谱图所在网页的地址，存储到resource.txt文件中
从所有乐谱图所在网页提取所有乐谱图的地址，并且存储到imageurl.txt中
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from time import sleep
import time
from bs4 import BeautifulSoup
import re
class Reptile:
    def __init__(self,url,name,page):
        self.wholeurl = url
        self.page = page
        self.url = "http://www.qupu123.com/"
        self.dir = "/Users/xiaopeng/Music/"+name
    def builddriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--referer=http://www.qupu123.com/qiyue/jita')
        obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver',chrome_options=chrome_options) #加载网址

       # obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver')  # 加载网址
        print("浏览器最大化")
        obj.maximize_window()
        obj.get(self.wholeurl)
        self.obj = obj
    def destroy(self):
        self.obj.quit()
    #获取每一页的歌曲条目
    def getPageItems(self):
        #=========================================================================
        #操作一
        #此段代码是将267页的所有歌曲信息抓取下来，先存到resource.txt文件中，避免之后出现问题，若此段不用，
        #可注释掉，直接进行操作二
        #=========================================================================
        fin = open('resource.txt','w',encoding='utf-8')
        i = 0
        while i<self.page:
            pagesoup = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser');
            div = pagesoup.find(name = 'div',attrs={'class':'body'})
            tbody = div.find(name = 'tbody')
            trs = tbody.findAll(name = 'tr')
            pageitems = dict()
            #获取图片资源所在url
            for tr in trs:
                try:
                        name = tr.find(name = 'td',attrs={'class':'f1'})
                        atag = name.find(name = 'a')
                        songname = atag.getText()
                        suburl = atag['href']
                        author = tr.find(name = 'td',attrs={'class':'f3'}).getText()
                        singer = tr.find(name = 'td',attrs={'class':'f4'}).getText()
                        print('歌曲名:',songname)
                        print('作词/作曲:',author)
                        print('演唱:',singer)
                        print('资源地址',self.url+suburl)
                        infostr = songname +'-词/曲:'+author+'-演唱:'+singer
                        print(infostr)
                        resourceurl = self.url+suburl
                        print('\n')
                        pageitems[infostr] = resourceurl
                        fin.write(infostr+'\n')
                        fin.write(resourceurl+'\n')
                except:
                    continue
            try:
                f = self.obj.find_element_by_link_text('下一页')
                f.click()
            except:
                self.obj.close()

            i=i+1
        print(pageitems)
        fin.close()

        #=========================================================================
        #操作二
        #从刚才的文件中读取数据，获取所有歌曲的图片地址，存入文件imageurl.txt
        #若提供了文件imageurl.txt,此段也可进行注释
        #=========================================================================
        # image = open('imageurl.txt','w',encoding='utf-8')
        # f = open("resource.txt", "r")
        # lines = f.readlines()  # 读取全部内容
        # print(len(lines))
        # imglist = dict()
        # for i in range(int(len(lines)/2)):
        #     imglist[lines[2*i]] = lines[2*i+1]
        # for dic in imglist:
        #     try:
        #         splits = dic.split('-')
        #         self.obj.get(imglist[dic])
        #         try:
        #             # 模拟鼠标单击事件，由于存在图片不自动加载需要手动点击的情况
        #             self.obj.find_element_by_xpath('// *[ @ id = "look_all"]').click()
        #             # print(clickdiv)
        #             # ActionChains(self.obj).click(clickdiv)
        #
        #         except:
        #             print('没有div方块')
        #         newsoup = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser')
        #         status = 1
        #         imageList = newsoup.find(name='div', attrs={'class': 'imageList'})
        #         imgtags = imageList.findAll(name='img')
        #         try:
        #             frame = self.obj.find_element_by_xpath('//*[@id="get_all_iframe"]')
        #             self.obj.switch_to.frame('get_all_iframe')
        #             sleep(4)
        #             newsoup1 = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser')
        #             print(newsoup1)
        #             frameimglist = newsoup1.find(name='div', attrs={'id': 'imglist'})
        #             print(frameimglist)
        #             frameimagetags = frameimglist.findAll(name='img')
        #         except:
        #             status = 0
        #             print('没有frame')
        #         # print(self.obj.page_source)
        #         print(dic)
        #         image.write(dic)
        #         if status == 1:
        #             image.write(imglist[dic])
        #         for imgtag in imgtags:
        #             print(imgtag)
        #             wholeurl = self.url+imgtag['src']
        #             print(wholeurl)
        #             image.write(wholeurl+'\n')
        #         if status == 1:
        #             for tag in frameimagetags:
        #                 print(tag)
        #                 wholeurl = self.url + tag['src']
        #                 print(wholeurl)
        #                 image.write(wholeurl+'\n')
        #         image.write('\n')
        #         print('\n')
        #
        #         imageurls = list()
        #     except:
        #         print("作者权益已被保护，网站不提供乐谱")
        #         continue
        #=========================================================================


