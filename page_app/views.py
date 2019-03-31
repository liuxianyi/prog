# coding:utf-8
from django.shortcuts import render
# Create your views here.

# 申明编码格式 中文不报错
from django.http import HttpResponse
from django.shortcuts import render
import os
from data_goog.settings import *
import xlrd
from page_app.core.save_helper import date_create
from page_app.history import get_all_html_file
import json
from django.views.decorators.csrf import csrf_exempt


def index1(request):
    return HttpResponse(u"雨")


def add_ab(request):
    """
    网址运算
    :param request:
    :return:
    """
    return HttpResponse(str(int(request.GET['a'])+int(request.GET['b'])))


def add_ab_(request, a, b):
    """
    网址
    :param request:
    :param a:
    :param b:
    :return:
    """
    c = int(a)+int(b)
    return HttpResponse(str(c))


def index1(request):
    # 获取历史记录中的目录
    templates_path_save_backup_tu = os.path.join(TEMPLATES_PATH, 'save_backup_tu')
    list_dir = os.listdir(templates_path_save_backup_tu)

    for dirs in list_dir:
        templates_path_save_backup_tu_date = os.path.join(templates_path_save_backup_tu, dirs)
        date = templates_path_save_backup_tu_date.split('\\')[-1]  # 获取时间
        print('日期:', date)
        html = get_all_html_file(templates_path_save_backup_tu_date)  # 获取历史html路径
        history = {
            'history_date': date,
            'history_data_html': html
        }
        history = json.dumps(history)
        print(type(history), history)
    return render(request, 'index1.html', context={'history': history})


def btn(request):
    return render(request, 'btn_group.html')


def test(request):
    return render(request, 'test_html.html')


def show_html(request):
    date = str(date_create())
    print(date)
    return render(request, 'save_show_tu/' + date + '/show.html')


##from submit
from page_app.core.holder import Holder


 ## from submit
## https://blog.csdn.net/kkorkk/article/details/80150644


def index(request):
    # 两个标志位
    ajax_flag = 0
    form_submit_flag = 0

    param1 = request.session.get('param')
    if param1:
        param = param1
        print(param)
    else:
        param = 1  # 默认1
    if request.is_ajax():
        print('ajax success!')
        ajax_flag = 1
        # global param
        ## python manage.py migrate 报错
        param = request.POST.get('choice')
        request.session['param'] = param
        print(param)
        # hole.holder(param, "data", None, None, 1)
        # name_dict = {'success': 1, 'error': 2}
        # HttpResponse(json.dumps(name_dict), content_type='application/json')
    else:
        if request.method == 'POST':  # form表单请求
            form_submit_flag = 1
            file = request.FILES['file_name']
            excel = file.name.split('.')[1]
            print(excel)
            # 解析excel数据
            if 'xlsx' == excel:
                # hole = Holder()
                # hole.holder(1, "data", None, None, 1)  # 默认算法
                if file:
                    file_path = os.path.join(MEDIA_ROOT, file.name)
                    # print(file_path)
                    with open(file_path, 'wb+') as f:
                        for chunk in file.chunks():
                            f.write(chunk)
                        f.close()
                    print("form submit success!")
    if ajax_flag == 1 | form_submit_flag == 1:
        hole = Holder()
        print('flag_arrive!')
        hole.holder(int(param), "data", None, None, 1)
    print('hold')
# history dealing    # 获取历史记录中的目录
    templates_path_save_backup_tu = os.path.join(TEMPLATES_PATH, 'save_backup_tu')
    templates_path_save_backup = os.path.join(TEMPLATES_PATH, 'save_backup')
    templates_path_save_show_last_info = os.path.join(TEMPLATES_PATH, 'save_show/last_info')
    templates_path_save_show_tu_last_info = os.path.join(TEMPLATES_PATH, 'save_show_tu/last_info')
    if not os.path.exists(templates_path_save_backup_tu):
        os.mkdir(templates_path_save_backup_tu)
    if not os.path.exists(templates_path_save_backup):
        os.mkdir(templates_path_save_backup)
    if not os.path.exists(templates_path_save_show_last_info):
        os.mkdir(templates_path_save_show_last_info)
    if not os.path.exists(templates_path_save_show_tu_last_info):
        os.mkdir(templates_path_save_show_tu_last_info)
    list_dir = os.listdir(templates_path_save_backup_tu)
    list_dir_data = os.listdir(templates_path_save_backup)  # 获得所有数据
    history_list_data = []
    for dirs in list_dir_data:
        templates_path_save_backup_date = os.path.join(templates_path_save_backup, dirs)
        date = templates_path_save_backup_date.split('\\')[-1]  # 获取时间
        data = os.listdir(templates_path_save_backup_date)[0]  # 获取历史html路径
        history_data = {
            'history_date': date,
            'history_data': date + '/' + data
        }
        history_list_data.append(history_data)
        # print(data)
    print(history_list_data)

    history_list = []
    for dirs in list_dir:
        templates_path_save_backup_tu_date = os.path.join(templates_path_save_backup_tu, dirs)
        date = templates_path_save_backup_tu_date.split('\\')[-1]  # 获取时间
        # print('日期:', date)
        html = get_all_html_file(templates_path_save_backup_tu_date)  # 获取历史html路径
        history = {
            'history_date': date,
            'history_data_html': date + '/' + html[0].replace('\\', '/').split('/')[-1]
        }
        history_list.append(history)

    show_txt = os.listdir(templates_path_save_show_last_info)[0]
    # print(templates_path_save_show_last_info+'/'+show_txt)
    list_dict_data = []
    with open(templates_path_save_show_last_info+'/'+show_txt, 'r') as f:
        # 读取前十行
        key = 0
        for line in f.readlines():
            if key > 5:
                break
            # print(key, ':', line.strip())
            line_ = line.strip()
            line_e = line_.split(' ')
            #  https://blog.csdn.net/litao_243/article/details/80517668 保留指定小数位数
            dict_data = {
                'c1': round(float(line_e[0].strip()), 6),
                'c2': round(float(line_e[1].strip()), 6),
                'c3': round(float(line_e[2].strip()), 6),
                'c4': round(float(line_e[3].strip()), 6),
            }
            key = key + 1
            list_dict_data.append(dict_data)
    print(list_dict_data)
    return render(request, 'index.html', context={'history': history_list, 'history_data': history_data,
                                                  'list_dict_data': list_dict_data})


def upload(request):
    """
    上传excel
    参考连接:https://blog.csdn.net/weixin_39682177/article/details/82378086
    https://blog.csdn.net/hejunw/article/details/80222980
    :param request:
    :return:
   """

    if request.method == 'POST':
        file = request.FILES['file_name']
        excel = file.name.split('.')[1]
        print(excel)
        # 解析excel数据
        if 'xlsx' == excel:
            hole = Holder()
            hole.holder(6, "data", None, None, 1)
            if file:
                file_path = os.path.join(MEDIA_ROOT, file.name)
                print(file_path)
                with open(file_path, 'wb+') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                    f.close()
                print("upload success!")

            # data = xlrd.open_workbook(filename=None, file_contents=file.read())
            # table = data.sheets()[0]  # # 打开第一张表
            # n_row = table.nrows  # 行数
            # n_col = table.ncols  # 列数
            # print(n_row, '  \t\t', n_col)
            # row_value_all = []
            # row_value = []
            # dic = {}
            # dic['rows'] = n_row  # 行数
            # dic['cols'] = n_col  # 列数
            # lst = []
            # '''
            #     将每一列数据储存在字典中
            # '''
            # for j in range(0, n_col):
            #     dic[str(j)] = []
            #     for i in range(0, n_row):
            #         dic[str(j)].append(table.row_values(i)[j])   # 解析一行数据
            # dic1 = {}
            # for j in range(0, n_row):
            #     for i in range(0, n_col):
            #         dic1[str(i)] = table.row_values(j)[i]  # 解析一行数据
            #     lst.append(dic1)
            #     dic1 = {}
                # row_value_all.append(row_value)
                    #print(row_value)  # 第一行数据j

            # print(type(row_value_all))
            # print(type(row_value_all[0]))

            # dic['row_value'] = row_value_all
            # for i in range(1, n_col):  # 提取每一列数据
                # dic[str(i)] = row_value_all[i]
            # print(str(dic['1']))
            # print(str(lst[190]))
    return render(request, 'index.html')# , context={'data': dic, 'lst': lst})
