#coding=utf-8
import datetime
import os
import numpy as np
import pyecharts

def date_create():
    now_time=datetime.datetime.now().strftime('%Y-%m-%d')
    return now_time

def save_txt_helper(data,data_name):
    if not os.path.exists("save_show"):
        os.mkdir("save_show")
    if not os.path.exists("save_backup"):
        os.mkdir("save_backup")

    date=str(date_create())
    if not os.path.exists("save_backup/"+date):
        os.mkdir("save_show/"+date)
        os.mkdir("save_backup/"+date)

    file_name_show="save_show/"+date+"/show.txt"
    file_name_backup="save_backup/"+date+"/"+data_name
    np.savetxt(file_name_show,data)
    np.savetxt(file_name_backup,data)

def save_tu_helper(echart,data_name):
    if not os.path.exists("save_show_tu"):
        os.mkdir("save_show_tu")
    if not os.path.exists("save_backup_tu"):
        os.mkdir("save_backup_tu")

    date=str(date_create())
    if not os.path.exists("save_backup_tu/"+date):
        os.mkdir("save_show_tu/"+date)
        os.mkdir("save_backup_tu/"+date)

    file_name_show="save_show_tu/"+date+"/show"
    file_name_backup="save_backup_tu/"+date+"/"+data_name

    echart.render(file_name_show+".html")
    echart.render(file_name_backup+".html")
