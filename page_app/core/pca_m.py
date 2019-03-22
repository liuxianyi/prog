#coding=utf-8
import numpy as np
from pyecharts import Scatter3D
from sklearn.decomposition import PCA,SparsePCA
from sklearn.datasets.samples_generator import make_blobs
from pyecharts import Bar,Page,Pie
from page_app.core import save_helper
#components_ratio取压缩的前百分比
#components_n为取压缩的前n个数据
#
#
class PCA_:
    def tu_pca(self,dataname="None",components_ratio=None,components_n=None,data=None):
        if components_n==None:
            components_n=1

        #返回信息
        message=[]
        #3D图参数
        page=Page()
        range_color = [
            '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
            '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

        #测试数据
        X,y=make_blobs(n_samples=10000,n_features=3,centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2],
                          random_state =9)
        if data == None:
            data=X

        #如果为3维数据，画出该图
        if(data.shape[1]==3):
            scatter3D=Scatter3D(dataname)
            scatter3D.add("",X,is_visualmap=True,visual_range_color=range_color)
            html_name=dataname+".html"
            page.add(scatter3D)

        #pca参数
        pca_=PCA(n_components=data.shape[1])
        pca_.fit(data)
        ratio=pca_.explained_variance_ratio_
        variance=pca_.explained_variance_
        attr=["成分"+str(i) for i in range(0,data.shape[1])]
        pie = Pie("PAC成分图", width=1000, height=600)
        pie.add(
            "百分比",
            attr,
            ratio,
            radius=[50, 55],
            center=[25, 50],
            is_random=True,
        )
        pie.add(
            "最大方差",
            attr,
            variance,
            radius=[0, 45],
            center=[25, 50],
            rosetype="radius",
        )
        page.add(pie)


        if components_ratio != None:
            pca=PCA(n_components=components_ratio)
            pca.fit(X)

            value=pca.transform(X)
            save_helper.save_txt_helper(value,dataname)

            #信息提示
            ratio_=np.sum(pca.explained_variance_ratio_)
            if ratio_ > components_ratio:
                message.append("所选百分比可能过小,为保证充分利用信息可以选择稍微向上调整")
            #绘图
            sum=0
            bar_data=None
            for i in range(0,data.shape[1]):
                sum=sum+ratio[i]
                if sum == ratio_:
                    bar_data=[x for x in ratio[range(i+1,data.shape[1])]]
                    bar=Bar("剩余成分百分比")
                    bar.add("",["剩余成分"+str(i) for i in range(i+1,data.shape[1])],bar_data)
                    page.add(bar)
                    break

        else:
            print(1)
            pca2=PCA(n_components=components_n)
            pca2.fit(X)
            value=pca2.transform(X)
            save_helper.save_txt_helper(value,dataname+"2")
            ratio_=np.sum(pca2.explained_variance_ratio_)
            pie_data=[ratio_]+[x for x in ratio[range(components_n,data.shape[1])]]
            attr=["s"]+["s"+str(i) for i in range(components_n,data.shape[1])]
            pie2=Pie("选择成分百分比")
            pie2.add("",attr,pie_data,radius=[40,75],label_text_color=None,is_label_show=True,legend_orient="vertical",legend_pos="right")
            page.add(pie2)

        #绘图
        save_helper.save_tu_helper(page,dataname)
        return message

    def tu_spca(self,dataname="kong",components_n=1,data=None):

        #测试数据
        X,y=make_blobs(n_samples=10000,n_features=3,centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2],
                          random_state =9)
        if data == None:
            data=X

        message=[]
        #训练数据
        spca=SparsePCA(n_components=components_n,normalize_components=True,random_state=0)
        spca.fit(X)
        #保存数据
        value=spca.transform(X)
        save_helper.save_txt_helper(value,dataname)

        components=spca.components_
        error=spca.error_
        page2=Page()
        #绘图
        for j in range(0,components.shape[0]):
            bar1=Bar("稀疏组建"+str(j))
            bar1.add("",["components_"+str(i) for i in range(0,components.shape[1])],components[j])
            page2.add(bar1)
        message.append("我们仅提供稀疏组建和数据误差供给分析")

        print(error)
        bar2=Bar("数据误差分析")
        bar2.add("",["error"+str(i) for i in range(0,len(error))],error)
        page2.add(bar2)
        save_helper.save_tu_helper(page2, dataname)

        return message
