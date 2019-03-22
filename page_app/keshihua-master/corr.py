#coding=utf-8
import pandas as pd
import os
import numpy as np
from pyecharts import Bar,Page
import save_helper

class Corr:
    #dataname :数据名称
    #data_place : 数据存放地点
    #return 回馈信息
    def corr_m(self,dataname,data_place):

        if data_place != None and os.path.exists(data_place):
            df = pd.read_excel(data_place,header=0,index=None)
        else:
            message = "数据不存在，或者数据格式错误"
            return message

        col_name = df.columns.values
        ax = df.corr()
        len = ax.shape[1]
        array = np.array(ax)
        rank = array.argsort()
        first_rank = rank[:,-2]

        first_name = []
        for j in range(len-1):
            first_name.append(col_name[first_rank[j]])

        page = Page()
        bar = Bar("相关性分析")
        page.add(bar)


        for j in range(len-1):
            bar.add(col_name[j],col_name,array[j],is_more_utils=True,is_datazoom_show=True,datazoom_type="both",
            is_datazoom_extra_show=True,datazoom_extra_type="slider")


        save_helper.save_tu_helper(page,dataname)
        message = []
        message.append("如果出现NAN数据说明该列不是数值型，请删除")
        return message
corr =Corr()
corr.corr_m("myda","/home/yhw/桌面/2019_MCM-ICM_Problems/2013年工作簿3.xlsx")
