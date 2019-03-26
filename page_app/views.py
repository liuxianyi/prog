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


def index(request):

    # 获取历史记录中的目录
    templates_path_save_backup_tu = os.path.join(TEMPLATES_PATH, 'save_backup_tu')
    list_dir = os.listdir(templates_path_save_backup_tu)
    history_list = []
    for dirs in list_dir:
        templates_path_save_backup_tu_date = os.path.join(templates_path_save_backup_tu, dirs)
        date = templates_path_save_backup_tu_date.split('\\')[-1]  # 获取时间
        print('日期:', date)
        html = get_all_html_file(templates_path_save_backup_tu_date)  # 获取历史html路径
        history = {
            'history_date': date,
            'history_data_html': date + '/' + html[0].replace('\\', '/').split('/')[-1]
        }
        history_list.append(history)
    return render(request, 'index.html', context={'history': history_list})


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
            if file:
                file_path = os.path.join(MEDIA_ROOT, file.name)
                print(file_path)
                with open(file_path, 'wb+') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                    f.close()
                print("success!")
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
