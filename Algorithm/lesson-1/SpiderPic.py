import re
import requests
import os
import cv2

PICPATH = []
for i in range(1,21):
    path = './img/0_' + str(i) + '.jpg'
    img = cv2.imread(path)
    if img.shape[0]>320 and img.shape[1]>320:
        img = cv2.resize(img,(320,320))
        cv2.imwrite(path,img)



# def dowmloadPic(html, keyword, pages):
#     pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
#     i = 1
#     print('找到关键词:' + keyword + '第' +str(pages) + '页的图片，现在开始下载图片...')
#     for each in pic_url:
#         print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
#         try:
#             pic = requests.get(each, timeout=10)
#         except requests.exceptions.ConnectionError:
#             print('【错误】当前图片无法下载')
#             continue

#         dir = './img/' + str(pages) + '_' + str(i) + '.jpg'
#         with open(dir,'wb') as fp:
#             # fp = open(dir, 'wb')
#             fp.write(pic.content)
#             fp.close()
#             i += 1

# if __name__ == '__main__':
#     word = 'cat'
#     page = 1

#     for k in range(0,page):
#         url = 'https://image.baidu.com/search/flip?tn=baiduimage&word='+word+'&pn='+str(k*20)
#         result = requests.get(url)
#         dowmloadPic(result.text, word, k)


