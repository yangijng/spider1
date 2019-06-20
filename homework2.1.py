import  urllib.request
hearders={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
urls = 'http://www.baidu.com'
ips=('http://183.51.190.51:33913','http://119.191.79.46:80','http://122.193.245.44:9999')
for ip in ips:
    proxy_handle = {
        'http': ip
    }
    #处理代理
    proxy = urllib.request.ProxyHandler(proxy_handle)
    #构建代理
    opener = urllib.request.build_opener(proxy)
    response = opener.open(url)
    print(response.status)
        if response.status == 200:
            print('爬取成功'.format(url))
        else:
            print('爬取失败'.format(url))
