#coding=utf-8
import datetime
import os
import numpy as np
import pyecharts
from data_goog.settings import *


def date_create():
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return now_time

def save_txt_helper(data,data_name):
    # if not os.path.exists("save_show"):
    #     os.mkdir("save_show")
    # if not os.path.exists("save_backup"):
    #     os.mkdir("save_backup")
    templates_path_save_show = os.path.join(TEMPLATES_PATH, 'save_show')
    templates_path_save_backup = os.path.join(TEMPLATES_PATH, 'save_backup')
    if not os.path.exists(templates_path_save_show):
        os.mkdir(templates_path_save_show)
    if not os.path.exists(templates_path_save_backup):
        os.mkdir(templates_path_save_backup)

    date = str(date_create())
    templates_path_save_show_date = os.path.join(templates_path_save_show, 'last_info')
    templates_path_save_backup_date = os.path.join(templates_path_save_backup, date)
    if not os.path.exists(templates_path_save_backup_date):
        os.mkdir(templates_path_save_backup_date)

    if not os.path.exists(templates_path_save_show_date):
        os.mkdir(templates_path_save_show_date)
    # if not os.path.exists("save_backup/"+date):
    #     os.mkdir("save_show/"+date)
    #     os.mkdir("save_backup/"+date)

    file_name_show = templates_path_save_show_date+'/show.txt'
    file_name_backup = templates_path_save_backup_date + '/'+ data_name
    # file_name_show="save_show/"+date+"/show.txt"
    # file_name_backup="save_backup/"+date+"/"+data_name
    np.savetxt(file_name_show, data)
    np.savetxt(file_name_backup, data)


def save_tu_helper(echart,data_name):

    ####################################
    templates_path_save_show_tu = os.path.join(TEMPLATES_PATH, 'save_show_tu')
    templates_path_save_backup_tu = os.path.join(TEMPLATES_PATH, 'save_backup_tu')
    ####################################
    if not os.path.exists(templates_path_save_show_tu):
        os.mkdir(templates_path_save_show_tu)
    # if not os.path.exists("save_show_tu"):
    #     os.mkdir("save_show_tu")
    if not os.path.exists(templates_path_save_backup_tu):
        os.mkdir(templates_path_save_backup_tu)
    # if not os.path.exists("save_backup_tu"):
    #     os.mkdir("save_backup_tu")

    date=str(date_create())
    templates_path_save_show_tu_date = os.path.join(templates_path_save_show_tu, 'last_info')
    templates_path_save_backup_tu_date = os.path.join(templates_path_save_backup_tu, date)
    # if not os.path.exists("save_backup_tu/"+date):
    #     os.mkdir("save_show_tu/"+date)
    #     os.mkdir("save_backup_tu/"+date)

    if not os.path.exists(templates_path_save_backup_tu_date):
        os.mkdir(templates_path_save_backup_tu_date)

    if not os.path.exists(templates_path_save_show_tu_date):
        os.mkdir(templates_path_save_show_tu_date)

    # file_name_show="save_show_tu/"+date+"/show"
    # file_name_backup="save_backup_tu/"+date+"/"+data_name
    file_name_show = templates_path_save_show_tu_date + '/show'
    file_name_backup = templates_path_save_backup_tu_date + '/' + data_name
    echart.render(file_name_show+".html")
    echart.render(file_name_backup+".html")
