'''
Created on 2018年3月16日

@author: Xiaopeng
这个脚本是下载无防盗链的图片
'''
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
def makdir(path,info):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print('创建文件夹'+info+'成功')
        return True
    else:
        print(path+'已经存在')
        return False
if __name__ == "__main__":
    oripath = '/Users/xiaopeng/Music/豫剧/'
    f = open('imageurl.txt','r')
    lines = f.read()
    #print(lines)
    newlines = lines.split('\n\n')
    lists = list()
    for line in newlines:
        lists.append(line)
    for l in lists:
        sp = l.split('\n')
        sp[0] = sp[0].replace('/','&')
        #输出文件夹名称
        print(sp[0])
        #makdir(oripath+sp[0],sp[0])
        wholepath = oripath+sp[0]+'/'
        for s in range(1,len(sp)):
            #输出网址
            print(sp[s])
            sps = sp[s].split('.')
            #输出网址后缀，防盗链图片后缀以com开头
            type = sps[len(sps)-1]
            if type == 'html':
                print("使用特殊方式对防盗链图片所在网站进行爬取")
                #------------------------------------------------------------------------------
                driver = webdriver.Firefox(executable_path='/Users/xiaopeng/Downloads/geckodriver')
                driver.maximize_window()
                name = sp[0]
                url = sp[s]
                driver.get(url)
                # try:
                # 模拟鼠标单击事件，由于存在图片不自动加载需要手动点击的情况
                driver.find_element_by_xpath('// *[ @ id = "look_all"]').click()
                soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                imgList = soup.find(name='div', attrs={'class': 'imageList'})
                #print(imgList)
                u = imgList.find(name='img')
                sp = u.get('src').split('.')
                # sp = imgList.get_attribute('src').split('.')
                # print(sp[len(sp)-1])
                wholepath = oripath + name + '/' + '1.' + sp[len(sp) - 1]
                print("正在下载到:" + wholepath)
                urllib.request.urlretrieve('http://www.qupu123.com' + u.get('src'), wholepath)
                print("下载完成")
                num = 0
          #  try:
                frame = driver.find_element_by_xpath('//*[@id="get_all_iframe"]')
                driver.switch_to_frame('get_all_iframe')
                sleep(4)
                newsoup1 = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                frameimglist = newsoup1.find(name='div', attrs={'id': 'imglist'})
                print(frameimglist)
                frameimagetags = frameimglist.findAll(name='img')
                num = len(frameimagetags)
          #  except:
                print('没有frame')
                print(num)
                for i in range(num):
                    xpath = '// *[ @ id = "imglist"] / img[' + str(i + 1) + ']'
                    ele = driver.find_element_by_xpath(xpath)
                    sleep(3)
                    # driver.execute_script("arguments[0].scrollIntoView();", ele)
                    # driver.save_screenshot(str(i+2)+'.png')
                    # im = Image.open(str(i+2)+'.png')
                    # im = open(str(i+2)+'.png', 'wb')
                    # im.write(ele.screenshot)
                    print("正在下载到:"+oripath + name + '/' + str(i + 2) + '.png')
                    with open(oripath + name + '/' + str(i + 2) + '.png', 'wb') as im:
                        im.write(ele.screenshot_as_png)
                    print("下载成功")
                driver.close()
                #------------------------------------------------------------------------------
                break
            else:
                print("此图不含有防盗链")
                print('正在下载到:'+wholepath+str(s)+'.'+type)
                try:
                  #  print(wholepath+str(s)+'.'+type)
                    urllib.request.urlretrieve(sp[s],wholepath+str(s)+'.'+type)
                except:
                    print('下载失败')
                    continue;
                print('下载成功')
        print('\n')

    #
    #     #for()
    #     # for line in lines:
    #     #     print(line)