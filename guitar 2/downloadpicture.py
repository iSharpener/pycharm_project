'''
Created on 2018年3月16日

@author: Xiaopeng
这个脚本是下载无防盗链的图片
'''
import urllib.request
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
    oripath = '/Users/xiaopeng/Music/download/'
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
        print(sp[0])
       # makdir(oripath+sp[0],name[0])
        wholepath = oripath+sp[0]+'/'
        for s in range(1,len(sp)):
            print(sp[s])
            sps = sp[s].split('.')
            print(sps[len(sps)-1])
            type = sps[len(sps)-1]
            print('正在下载到:'+wholepath+str(s)+'.'+type)
            try:
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