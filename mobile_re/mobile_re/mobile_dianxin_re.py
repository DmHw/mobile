import re
import urllib.request  
page_num = 1
while page_num <= 12:
    response = urllib.request.urlopen('http://www.189.cn/dqmh/tianyiMall/searchMallAction.do?method=shopPhone&cityCode=ha&xspLeibie=%E6%89%8B%E6%9C%BA&listType=0&pageSize=16&internal_search=1&shopId=10017&currentPage='+str(page_num), timeout=6)  
    #print(response.read().decode('utf-8'))
    string = response.read().decode('utf-8')
    #print(type(string))

    #string = 'fdsafhojkgfgkld'
    #pat = 'kld'
    #pat = '\n'
    # \w  one a 2 _ 
    #pat = 'mkTitle":"网厅-iPhone8 64G 深空灰色'
    #"mkTitle":"网厅-iPhone8 64G 深空灰色"
    pat_mobile_price = 'xsj":"(\d{4}|\d{3})'
    #result = re.search(pat, string)
    mobile_price = re.findall(pat_mobile_price, string)

    pat_mobile_name = 'mkTitle":"(.*?)"'
    mobile_name = re.findall(pat_mobile_name, string)
    #for item in mobile_name:
    #   print(item)
    dictionary = dict(zip(mobile_name, mobile_price))
    for key in dictionary:
        print(key,',',dictionary[key])
        f = open('./text.txt', 'a')
        f.write('\n'+key+','+dictionary[key])
        f.close()
    page_num += 1
    #print(mobile_price)
    #print(type(mobile_price))
    # dir() 查看对象可以使用的方法， 又学到一点，哈哈加油吧 先全局在具体，学习就是东一点细一点 拼出来的。
    #print(dir(result))
    # 你不知道这是什么但是你要学会取调用函数来帮助自己了解他是什么？