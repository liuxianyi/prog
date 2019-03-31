#coding=utf-8
from page_app.core.kmean import KM
from page_app.core.GuanJianCi import GJC
from page_app.core.pca_m import PCA_
from page_app.core.Guss import GUSS
from page_app.core.corr import Corr
from page_app.core.China import China
from page_app.core.mst import MST
from page_app.core import pca_m
import datetime, time
import os
import numpy as np
import pandas as pd
#choice :算法选择
#dataname:数据名称，后续可能根据此值寻找以前数据图片
#param:是一个list，存放数组
#data:数据
#other:某算法的细分算法，默认为none
#return :回馈信息
#关于生成的html文件：backup文件为后备文件，展示文件夹为show_tu
#关于返回的数据文件：save_show为展示的数据文件，save_backup为后备文件夹
class Holder(object):

    def __init__(self):
        self.kmeans = KM()
        self.pca = PCA_()
        self.guss = GUSS()
        self.corr = Corr()
        self.china = China()
        self.mst = MST()
        self.gjc = GJC()

    def holder(self,choice,dataname,param,data_path,other=None):
        message = None
        if param == None:
            param = {"n_c":6,"components_ratio":0.9,"components_n":4,"guss_choice":2,"data_place":data_path,"mst_choice":"prim","num":10}
        if data_path == None:
            data = None
        else:
            df = pd.read_excel(data_path)
            message = self.check_data(choice,df)
            if message != None:
                return message
            data_col = df.columns.values
            data = df.values

        # random_clear = np.random.randn()
        # if random_clear < 0.3:
        #     self.clear_holder()

        if choice == 1:
            self.kmeans.tu_kmeans(v=data,n_c=param["n_c"], dataname=dataname)
        if choice == 2:
            func_name=["tu_pca", "tu_spca"]
            func = getattr(self.pca,func_name[other])
            if other == 0:
                message = func(dataname=dataname,components_ratio=param["components_ratio"],components_n=param["components_n"],data=data)
            else:
                message = func(dataname=dataname,components_n=param["components_n"],data=data)
        if choice == 3:
            if data == None:
                self.guss.tu_Gussian(dataname=dataname,choice=2)
            else:
                ##############
                n = data[:, -1].shape[0]
                TrainData = data[0:n]
                X = data[n:]
                self.guss.tu_Gussian(dataname=dataname, X=X, TrainData=TrainData,choice=param["guss_choice"])
                #self.guss.tu_Gussian(dataname=dataname,X=data[:,0:-1],TrainData=data[:,-1],choice=param["guss_choice"])
        if choice == 4:
            message = self.corr.corr_m(dataname=dataname, data_place=param["data_place"])
        if choice == 5:
            self.china.china_city(dataname=dataname,data=data)
        if choice == 6:
            if data == None:
                self.mst.mst(dataname=dataname,choice=param["mst_choice"])
            else:
                self.mst.mst(data=data,dataN=data_col,dataname=dataname,choice=param["mst_choice"])
        if choice == 7:
            self.gjc.GuanJianCi(data_name=dataname,num=param["num"],text=data)
        return message

    def history(self,dataname):
        data = self.date_create()
        path_txt = "save_backup/"+data+"/"+dataname
        path_tu = "save_backup_tu/"+data+"/"+dataname
        path = []
        if os.path.exists(path_tu):
            path.append(path_tu)
        if os.path.exists(path_txt):
            path.append(path_txt)
        return path

    def date_create(self):
        now_time=datetime.datetime.now().strftime('%Y-%m-%d')
        return now_time

    def clear_holder(self):
        dir_list = ["save_backup","save_backup_tu","save_show","save_show_tu"]
        for dir in dir_list:
            self.clear_helper(dir)

    def clear_helper(self,name):
        now = self.date_create()
        old = os.listdir(name)

        def rmdir(dir):
            for roots,dirs,files in os.walk(dir):
                for name in files:
                    os.remove(roots+"/"+name)
            os.rmdir(dir)

        for itme in old:
            if itme[5:7] != now[5:7] or itme[0:5] != now[0:5]:
                rmdir(name+"/"+itme)

    def check_data(self,choice,df):
        message = self.isnull(data)
        if message != null:
            return message

        if choice == 1 or 2 or 4:
            message = self.numcheck(df)
            return message

        if choice == 3:
            message = self.numcheck(df)
            col = df.columns.values
            label = col[-1]
            if df.drop_duplicates([label])[label].size != 2:
                message.append("数据错误：Guss异常检查的标签应该只有两个类型，例如1和0")

        if choice == 5:
            col_size = df.columns.values.size
            if col_size != 2:
                message.append("数据错误：中国地图数据只需要两列，第一列是city名，第二列是数值类型")

        if choice == 6:
            if df.shape[0] != df.shape[1]:
                message.append("数据错误，每个节点应该对应所有节点都有数值")


    def numcheck(self,df):
        types = df.get_dtype_counts()

        if 'object' in types:
            message.append("数据错误：数据应全是数值类型且同一列应是同一种数据类型")
            message.append("数据类型：同列数据应该全是浮点型或者全是整数型")
        return message

    def isnull(self,df):
        message = []
        if type(df) == pd.core.frame.DataFrame:
            null = df.isnull().sum()
            if len(null[null != 0]) != 0:
                message.append("数据错误：数据存在缺失，请处理后继续")
        return message
# hole=Holder()
# hole.holder(7, "data",None,None,1)
#hole.isnull("d")
# df = pd.read_excel("/home/yhw/桌面/2019_MCM-ICM_Problems/2012年工作簿4.xlsx")
# print df.size,df.shape
