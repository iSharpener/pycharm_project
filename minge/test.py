'''
Created on 2018年3月16日

@author: Xiaopeng
这个脚本是下载有防盗链的图片
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import urllib.request
from PIL import Image
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
f = open('picturenourl.txt','r')
lines = f.readlines()
driver = webdriver.Firefox(executable_path='/Users/xiaopeng/Downloads/geckodriver')
driver.maximize_window()
for i in range(int(len(lines)/2)):
    print(lines[i*2])
    print(lines[i*2+1])
    oripath = '/Users/xiaopeng/Music/download1/'
    name = lines[i*2]
    name = name.replace('/','&')
    makdir(oripath+name,name)
    url = lines[i*2+1]
    driver.get(url)
    #try:
    # 模拟鼠标单击事件，由于存在图片不自动加载需要手动点击的情况
    driver.find_element_by_xpath('// *[ @ id = "look_all"]').click()
    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
    imgList = soup.find(name = 'div',attrs={'class':'imageList'})
    print(imgList)
    u = imgList.find(name = 'img')
    sp = u.get('src').split('.')
    # sp = imgList.get_attribute('src').split('.')
    # print(sp[len(sp)-1])
    wholepath = oripath+name+'/'+'1.'+sp[len(sp)-1]
    urllib.request.urlretrieve('http://www.qupu123.com'+u.get('src'),wholepath)
    print(wholepath)
    num = 0
    try:
        frame = driver.find_element_by_xpath('//*[@id="get_all_iframe"]')
        driver.switch_to_frame('get_all_iframe')
        sleep(4)
        newsoup1 = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
        frameimglist = newsoup1.find(name='div', attrs={'id': 'imglist'})
        print(frameimglist)
        frameimagetags = frameimglist.findAll(name='img')
        num = len(frameimagetags)
    except:
        print('没有frame')
    print(num)
    for i in range(num):
        xpath = '// *[ @ id = "imglist"] / img['+str(i+1)+']'
        ele = driver.find_element_by_xpath(xpath)
        sleep(3)
        # driver.execute_script("arguments[0].scrollIntoView();", ele)
        # driver.save_screenshot(str(i+2)+'.png')
        # im = Image.open(str(i+2)+'.png')
        # im = open(str(i+2)+'.png', 'wb')
        # im.write(ele.screenshot)
        print(oripath+name+'/'+str(i+2)+'.png')
        with open(oripath+name+'/'+str(i+2)+'.png', 'wb') as im:
            im.write(ele.screenshot_as_png)

driver.close()

