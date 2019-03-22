#coding=utf-8
import numpy as np
from pyecharts import Scatter
from sklearn.cluster import KMeans
from pyecharts import Radar
from pyecharts import Page,Bar
import sklearn.cluster as skc
from page_app.core import save_helper
from functools import reduce
class KM:
    def tu_kmeans(self,v=None,n_c=4,dataname="None"):

        def lable_(ny,num,lable):
            num=0
            for i in lable:
                for j in range(0,n_c):
                    if i == j:
                        ny[j]=np.vstack((ny[j],np.array(v[num])))
                        num=num+1
            return ny

        #test data
        if v==None:
            v=np.random.random((190,2))

        setattr=Scatter("数据平面图")
        #kmeans

        kmeans = KMeans(n_clusters=n_c, random_state=9).fit(v)
        y_pred=kmeans.labels_
        print(kmeans.cluster_centers_[1])
        setattr.add("center",kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1])
        nn={}
        for i in range(0,n_c):
            nn[i]=np.array([0,0])
        nn=lable_(nn,n_c,y_pred)


        arr=np.array([[1,3],[2,3],[3,2]])

        bar =Bar("方差分析")

        td=["cul"+str(i) for i in range(0,n_c)]
        td.append("u")
        td.append("sum")


        for i in range(0,n_c):
            nn[i]=np.delete(nn[i],0,0)
            setattr.add("cul"+str(i),nn[i][:,0],nn[i][:,1])

        def manhattan_distance(x,y):
            sum=0
            for poin in y:
                sum=np.sum(abs(x-y))
            return sum

        dis={}

        for i in range(0,n_c):
            dis[i]=manhattan_distance(kmeans.cluster_centers_[i],nn[i])

        dis_list=[dis[i] for i in dis]
        dis_sum=reduce(lambda x,y:x+y,dis_list)
        print(dis_sum)


        radar=Radar("簇点误差分析.html")

        #dbscan
        dis_db=0.1
        num_simple=5
        dbscan=skc.DBSCAN(dis_db,num_simple).fit(v)
        n_clusters=len(set(dbscan.labels_))-1
        clu_lab=dbscan.labels_

        scatter=Scatter("噪声分析")

        for i in range(n_clusters):
            print(i)
            one_clu=v[clu_lab == i]

            scatter.add("scan"+str(i),one_clu[:,0],one_clu[:,1])


        zaosheng=v[dbscan.labels_==-1]
        if zaosheng != []:
            scatter.add("噪声点",zaosheng[:,0],zaosheng[:,1])


        radar.config([("clu"+str(i),reduce(max,dis_list)) for i in range(0,n_c)])
        dis_list.append(dis_sum/n_c)
        dis_list.append(dis_sum)
        bar.add("",td,dis_list,is_stack=True,label_pos='inside')
        radar.add("bia",[dis_list],is_splitline=True, is_axisline_show=True)
        page=Page()
        page.add(setattr)
        page.add(bar)
        page.add(radar)
        page.add(scatter)

        save_helper.save_tu_helper(page, dataname)
