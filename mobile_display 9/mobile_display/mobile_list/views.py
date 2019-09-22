from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from mobile_list.models import *  # 导入模型
from django.db.models import Count  # 导入聚合模块


# 两个列表的相加!
def list_add(a, b):
    # c = [0, 0, 0, 0, 0, 0, 0]
    c = list(range(len(a)))
    for i in range(len(a)):
        c[i] = a[i] + b[i]
    return c


# 计算百分比
def count_list(n):
    # m = [0, 0, 0, 0, 0, 0, 0]
    m = list(range(len(n)))
    for i in range(len(n)):
        m[i] = int((n[i]/560)*100)
    return m


# 显示手机品牌数量(1. 一个是全部手机显示 2. 一个是各个运营商显示)
def count_all_mobile():
    # 1.实现联通数据库数据聚合并返回字典
    count_mobile = MobileLiantongFormated.objects.aggregate(count_liantong=Count('id'))
    # 2.电信的聚合
    count_mobile.update(MobileDianxinFormated.objects.aggregate(count_dianxin=Count('id')))
    # 3. 移动的聚合
    count_mobile.update(MobileYidongFormated.objects.aggregate(count_yidong=Count('id')))
    return count_mobile


def mobile_brand():
    # 计算运营商总手机数,并返回字典
    count_mobile = count_all_mobile()
    # 筛选各个品牌手机
    # 电信
    dianxin_iphone = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__icontains='iPhone'))
    dianxin_xiaomi = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains='小米'))
    dianxin_shanxin = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains='三星'))
    dianxin_huawei = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains='华为'))
    dianxin_vivo = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__icontains='vivo'))
    dianxin_oppo = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__icontains='oppo'))
    dianxin_list = [dianxin_iphone, dianxin_xiaomi, dianxin_shanxin, dianxin_huawei, dianxin_vivo, dianxin_oppo]
    dianxin_list.append(count_mobile['count_dianxin'] - sum(dianxin_list))
    # 联通
    liantong_iphone = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__icontains='iPhone'))
    liangtong_xiaomi = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__contains='小米'))
    liangtong_shanxin = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__contains='三星'))
    liangtong_huawei = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__contains='华为'))
    liangtong_vivo = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__icontains='vivo'))
    liangtong_oppo = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__icontains='oppo'))
    liangtong_list = [liantong_iphone, liangtong_xiaomi, liangtong_shanxin, liangtong_huawei, liangtong_vivo, liangtong_oppo]
    liangtong_list.append(count_mobile['count_liantong'] - sum(liangtong_list))
    # 移动
    yd_iphone = len(MobileYidongFormated.objects.filter(mobile_yidong_name__icontains='iPhone'))
    yd_xiaomi = len(MobileYidongFormated.objects.filter(mobile_yidong_name__contains='小米'))
    yd_shanxin = len(MobileYidongFormated.objects.filter(mobile_yidong_name__contains='三星'))
    yd_huawei = len(MobileYidongFormated.objects.filter(mobile_yidong_name__contains='华为'))
    yd_vivo = len(MobileYidongFormated.objects.filter(mobile_yidong_name__icontains='vivo'))
    yd_oppo = len(MobileYidongFormated.objects.filter(mobile_yidong_name__icontains='oppo'))
    yd_list = [yd_iphone, yd_xiaomi, yd_shanxin, yd_huawei, yd_vivo, yd_oppo]
    yd_list.append(count_mobile['count_yidong'] - sum(yd_list))
    # print(yd_list)
    # print(liangtong_list)
    # print(dianxin_list)

    all_brand = list_add(list_add(dianxin_list, yd_list), liangtong_list)
    all_brand.reverse()
    count_all_brand = count_list(all_brand)
    info_mobile = {'lt': liangtong_list, 'yd': yd_list, 'dx': dianxin_list, 'all_brand': count_all_brand}
    # print(info_mobile)
    #return render(request, 'mobile_list/charts-1.html', info_mobile)

    # 返回一个字典
    return info_mobile

def mobile_price():
    price_dx_1 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
    price_dx_2 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=500, mobile_dianxin_price__lte=999))
    price_dx_3 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1000, mobile_dianxin_price__lte=1999))
    price_dx_4 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=2000, mobile_dianxin_price__lte=2999))
    price_dx_5 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=3000, mobile_dianxin_price__lte=4999))
    price_dx_6 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=5000))
    price_list_dx = [price_dx_1, price_dx_2, price_dx_3, price_dx_4, price_dx_5, price_dx_6]

    price_lt_1 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=1, mobile_liantong_price__lte=499))
    price_lt_2 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=500, mobile_liantong_price__lte=999))
    price_lt_3 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=1000, mobile_liantong_price__lte=1999))
    price_lt_4 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=2000, mobile_liantong_price__lte=2999))
    price_lt_5 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=3000, mobile_liantong_price__lte=4999))
    price_lt_6 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=5000))
    price_list_lt = [price_lt_1, price_lt_2, price_lt_3, price_lt_4, price_lt_5, price_lt_6]

    price_yd_1 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=1, mobile_yidong_price__lte=499))
    price_yd_2 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=500, mobile_yidong_price__lte=999))
    price_yd_3 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=1000, mobile_yidong_price__lte=1999))
    price_yd_4 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=2000, mobile_yidong_price__lte=2999))
    price_yd_5 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=3000, mobile_yidong_price__lte=4999))
    price_yd_6 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=5000))
    price_list_yd = [price_yd_1, price_yd_2, price_yd_3, price_yd_4, price_yd_5, price_yd_6]

    all_price = list_add(list_add(price_list_yd, price_list_dx), price_list_lt)

    price_dict = {'lt': price_list_lt, 'yd': price_list_yd, 'dx': price_list_dx, 'all_price': all_price}
    # print(price_dict)
    #return render(request, 'mobile_list/charts-4.html', price_dict)
    return price_dict

# 滚动显示
def roll_display():
    roll_info = MobileYidongFormated.objects.all()
    # for 遍历这个列表 , 并取其name 和 price !
    return roll_info


# 显示价格折线图



# 返回登录页面
def login(request):
    return render(request, 'mobile_list/login.html')

# 登录的验证
def login_ajax_check(request):
    username = request.POST.get('userName')
    password = request.POST.get('passWord')
    print(username, password)
    if username == 'admin' and password == 'admin':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})




#
# def login(request):
#     dict_brand = mobile_brand()
#     dict_brand_name = ['iPhone', '小米', '三星', '华为', 'vivo', 'oppo']
#     dict_price = mobile_price()
#     list_roll = roll_display()
#     print(dict_brand, dict_price, list_roll)
#     return render(request, 'mobile_list/login.html')



# 主要负责显示页面
def index(request):
    # 直方图 以及 百分比图
    dict_brand = mobile_brand()
    # dict_brand_name = ['iPhone', '小米', '三星', '华为', 'vivo', 'oppo', '其他']
    # 滚动
    dict_roll = roll_display()
    # 折线图
    dict_price = mobile_price()
    #list_price = ['1-499', '500-999', '1000-1999', '2000-2999', '3000-4999', '5000']
    # 饼状图对比什么好呢?
    print(dict_price)
    return render(request, 'mobile_list/index.html', {'dict_brand': dict_brand, 'dict_roll': dict_roll,
                                                      'dict_price': dict_price})


def index_2(request):
    return render(request, 'mobile_list/index_2.html')



#
# def test(request):
#     # dict_brand = mobile_brand()
#     # dict_brand_name = ['iPhone', '小米', '三星', '华为', 'vivo', 'oppo', '其他']
#     # # print(dict_brand, dict_brand_name)
#     # dict_roll = roll_display()
#     # dict_price = mobile_price()
#
#     return render(request, 'mobile_list/test.html')




# 实现滚动显示 !

# def welcome(request):
#     # 实现数据的展示
#     # 实现数据的筛选展示
#     #
#     mobile_list = MobileDianxinFormated.objects.all()
#     return render(request, 'mobile_list/welcome.html', {'mobile_list': mobile_list})
#
#
# # 查找功能
# def search(request):
#
#     key = request.GET['name_mobile']
#     mobile_list = MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains=key)
#
#     # return HttpResponse('you have search{}'.format(request.GET['name_mobile']))
#     return render(request, 'mobile_list/welcome.html', {'mobile_list': mobile_list})
#
#
# # def index(request):
# #
# #     #return HttpResponse('ok !')
# #     return render(request, 'mobile_list/index.html')
# #
# #
# # def login(request):
# #     return render(request, 'mobile_list/login.html')
#
# #
# def count_all_mobile():
#     # 1.实现联通数据库数据聚合并返回字典
#     count_mobile = MobileLiantongFormated.objects.aggregate(count_liantong=Count('id'))
#     # 2.电信的聚合
#     count_mobile.update(MobileDianxinFormated.objects.aggregate(count_dianxin=Count('id')))
#     # 3. 移动的聚合
#     count_mobile.update(MobileYidongFormated.objects.aggregate(count_yidong=Count('id')))
#     return count_mobile
#
#
# # 计算手机价格区间数量
# def interval_price(mobile_price):
#     price_1 = len(MobileDianxinFormated.objects.filter(mobile_price__gte=1, mobile_price__lte=499))
#     price_2 = len(MobileDianxinFormated.objects.filter(mobile_price__gte=500, mobile_price__lte=999))
#     price_3 = len(MobileDianxinFormated.objects.filter(mobile_price__gte=1000, mobile_price__lte=1999))
#     price_4 = len(MobileDianxinFormated.objects.filter(mobile_price__gte=2000, mobile_price__lte=2999))
#     price_5 = len(MobileDianxinFormated.objects.filter(mobile_price__gte=3000, mobile_price__lte=4999))
#     price_6 = len(MobileDianxinFormated.objects.filter(mobile_price__gte=5000))
#     price_list = [price_1, price_2, price_3, price_4, price_5, price_6]
#     return price_list
#
# # def charts_1(yys, ):
# #     yunYinShang = 'Mobile' + yys + 'Formated'  # 电信运营商名字
# #   e_name = 'mobile_' + yys.lower() + 'name'
#
# def charts_1(request):
#     # 计算运营商总手机数,并返回字典
#     count_mobile = count_all_mobile()
#     # 筛选各个品牌手机
#     # 电信
#     dianxin_iphone = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__icontains='iPhone'))
#     dianxin_xiaomi = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains='小米'))
#     dianxin_shanxin = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains='三星'))
#     dianxin_huawei = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__contains='华为'))
#     dianxin_vivo = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__icontains='vivo'))
#     dianxin_oppo = len(MobileDianxinFormated.objects.filter(mobile_dianxin_name__icontains='oppo'))
#     dianxin_list = [dianxin_iphone, dianxin_xiaomi, dianxin_shanxin, dianxin_huawei, dianxin_vivo, dianxin_oppo]
#     dianxin_list.append(count_mobile['count_dianxin'] - sum(dianxin_list))
#     # 联通
#     liantong_iphone = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__icontains='iPhone'))
#     liangtong_xiaomi = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__contains='小米'))
#     liangtong_shanxin = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__contains='三星'))
#     liangtong_huawei = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__contains='华为'))
#     liangtong_vivo = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__icontains='vivo'))
#     liangtong_oppo = len(MobileLiantongFormated.objects.filter(mobile_liantong_name__icontains='oppo'))
#     liangtong_list = [liantong_iphone, liangtong_xiaomi, liangtong_shanxin, liangtong_huawei, liangtong_vivo, liangtong_oppo]
#     liangtong_list.append(count_mobile['count_liantong'] - sum(liangtong_list))
#     # 移动
#     yd_iphone = len(MobileYidongFormated.objects.filter(mobile_yidong_name__icontains='iPhone'))
#     yd_xiaomi = len(MobileYidongFormated.objects.filter(mobile_yidong_name__contains='小米'))
#     yd_shanxin = len(MobileYidongFormated.objects.filter(mobile_yidong_name__contains='三星'))
#     yd_huawei = len(MobileYidongFormated.objects.filter(mobile_yidong_name__contains='华为'))
#     yd_vivo = len(MobileYidongFormated.objects.filter(mobile_yidong_name__icontains='vivo'))
#     yd_oppo = len(MobileYidongFormated.objects.filter(mobile_yidong_name__icontains='oppo'))
#     yd_list = [yd_iphone, yd_xiaomi, yd_shanxin, yd_huawei, yd_vivo, yd_oppo]
#     yd_list.append(count_mobile['count_yidong'] - sum(yd_list))
#     # print(yd_list)
#     # print(liangtong_list)
#     # print(dianxin_list)
#     info_mobile = {'lt': liangtong_list, 'yd': yd_list, 'dx': dianxin_list}
#     # print(info_mobile)
#     return render(request, 'mobile_list/charts-1.html', info_mobile)
#
#
# def charts_2(request):
#     return render(request, 'mobile_list/charts-2.html')
#
#
# def charts_3(request):
#
#     # price_1 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#     # price_2 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#     # price_3 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#     # price_4 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#     # price_5 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#     # price_6 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#
#     return render(request, 'mobile_list/charts-3.html')
#
#
# def charts_4(request):
#
#     price_dx_1 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1, mobile_dianxin_price__lte=499))
#     price_dx_2 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=500, mobile_dianxin_price__lte=999))
#     price_dx_3 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=1000, mobile_dianxin_price__lte=1999))
#     price_dx_4 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=2000, mobile_dianxin_price__lte=2999))
#     price_dx_5 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=3000, mobile_dianxin_price__lte=4999))
#     price_dx_6 = len(MobileDianxinFormated.objects.filter(mobile_dianxin_price__gte=5000))
#     price_list_dx = [price_dx_1, price_dx_2, price_dx_3, price_dx_4, price_dx_5, price_dx_6]
#
#
#     price_lt_1 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=1, mobile_liantong_price__lte=499))
#     price_lt_2 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=500, mobile_liantong_price__lte=999))
#     price_lt_3 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=1000, mobile_liantong_price__lte=1999))
#     price_lt_4 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=2000, mobile_liantong_price__lte=2999))
#     price_lt_5 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=3000, mobile_liantong_price__lte=4999))
#     price_lt_6 = len(MobileLiantongFormated.objects.filter(mobile_liantong_price__gte=5000))
#     price_list_lt = [price_lt_1, price_lt_2, price_lt_3, price_lt_4, price_lt_5, price_lt_6]
#
#
#     price_yd_1 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=1, mobile_yidong_price__lte=499))
#     price_yd_2 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=500, mobile_yidong_price__lte=999))
#     price_yd_3 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=1000, mobile_yidong_price__lte=1999))
#     price_yd_4 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=2000, mobile_yidong_price__lte=2999))
#     price_yd_5 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=3000, mobile_yidong_price__lte=4999))
#     price_yd_6 = len(MobileYidongFormated.objects.filter(mobile_yidong_price__gte=5000))
#     price_list_yd = [price_yd_1, price_yd_2, price_yd_3, price_yd_4, price_yd_5, price_yd_6]
#
#     price_dict = {'lt': price_list_lt, 'yd': price_list_yd, 'dx': price_list_dx}
#     print(price_dict)
#     return render(request, 'mobile_list/charts-4.html', price_dict)
#
#
# def charts_5(request):
#     count_mobile = count_all_mobile()
#     return render(request, 'mobile_list/charts-5.html', count_mobile)
#
#
# def charts_6(request):
#     return render(request, 'mobile_list/charts-6.html')
#
#
# def charts_7(request):
#     return render(request, 'mobile_list/charts-7.html')
#
#
# def table_show(request):
#     mobile_list = MobileDianxinFormated.objects.all()
#     return render(request, 'mobile_list/table.html', {'mobile_list': mobile_list})

