import urllib.request

def getHtml(url):#定义函数
    page = (urllib.request.urlopen(url)).read().decode('utf8') #获取网站内容
    return page

page = getHtml("http://www.17k.com/chapter/2933095/36699279.html") #方法调用

print(page)
fhandle = open("r'C:\titles.txt", "w",encoding='utf8')#创建文件并转码
fhandle.write(page)#写入数据
fhandle.close()



