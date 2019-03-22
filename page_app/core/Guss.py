#coding=utf-8
import numpy as np
from pyecharts import Page,Bar,Scatter
import math, random
from sklearn.datasets.samples_generator import make_blobs
import page_app.core.featurn_ksh as ksh
from page_app.core import save_helper
from functools import reduce

class GUSS:
    page=Page()

    def estimateGaussion(self,X):
        mu=np.mean(X,0)
        sigma2=np.var(X,0)
        return mu,sigma2
    #默认使用的是精度和召回率的调和均值，其适用于数据倾斜的情况

        # 一维高斯
    def gaussian(self, sigma, x, u):
        y = np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
        return y


    def tu_Gussian(self,dataname="None",X=None,TrainData=None,choice=12):

    #测试数据集
        if X==None:
            X,y=make_blobs(n_samples=100,n_features=3,centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2],
                              random_state =9)
        n=X.shape[1]
        m=X.shape[0]
        if TrainData==None:
            col=np.random.randint(0,1,(98,1))
            col2=np.random.randint(1,2,(2,1))
            TrainData=np.column_stack((X,np.row_stack((col,col2))))
    #高斯模型
        mu1,sigms1=self.estimateGaussion(X)
        if choice==1:
            px_one=self.gaussian(sigms1,X,mu1)
            if n<=10:
                scatter=Scatter("featurn")
                for j in range(0,n):
                    scatter.add(str(j),X[:,j], px_one[:,j])

        else:
            px_one=self.multivariateGaussian(X,mu1,sigms1)
            scatter=Scatter("featurn")
            def f(x):
                y=1
                for i in range(n):
                    y=y*x[i]
                return y

            scatter.add("总体分布", list(map(f,X)), px_one)

        #交叉验证，取得最好epsilon
        len = TrainData.shape[1]

        Xval=TrainData[:,0:-1]
        Yval=TrainData[:,-1]

        pvals=[]                       #各个特征值的概率相乘
        if choice==1:
            pval=gaussian(sigms1,Xval,mu1)
            for i in range(0,m):
                pvals.append(reduce(mul,pval[i,:]))
        else:
            pvals=self.multivariateGaussian(Xval,mu1,sigms1)

        epsilon,F1=self.selectThreshold(Yval, pvals)

        # yc=[.0]              #异常点为0

        #def filteryc(x):
            #return x[n-1]  in yc
        # newdata=filter(filteryc,TrainData)
        inliers = np.where(px_one>epsilon)
        # save_helper.save_txt_helper(newdata,dataname)
        save_helper.save_txt_helper(X[inliers], dataname)
        outliers=np.where(px_one<epsilon)
        scatter2=ksh.ksh_scatter("离散点异常分布图","正常点",X,"FG","异常点",X[outliers])
        self.page.add(scatter)
        self.page.add(scatter2)

        save_helper.save_tu_helper(self.page,dataname)

    def mul(self,x,y):
        return x*y






    #多维高斯
    def multivariateGaussian(self,X,mu,Sigma2):
        k = len(mu)
        if (Sigma2.shape[0]>1):
            Sigma2 = np.diag(Sigma2)
            X = X-mu
            argu = (2*np.pi)**(-k/2)*np.linalg.det(Sigma2)**(-0.5)
            p = argu*np.exp(-0.5*np.sum(np.dot(X,np.linalg.inv(Sigma2))*X,axis=1))
            return p




    #利用召回精准率来选择最佳的得分
    def selectThreshold(self,Yval,pval):         #训练集的标签Yval和训练集的结果pval
        bestEpsilon=0.
        bestF1=0.
        bestFN=0.
        bestFP=0.
        bestTP=0.
        bestTN=0.
        F1=0.
        P=np.sum(Yval==1)
        N=np.sum(Yval==0)
        print(P,N)
        step=(np.max(pval)-np.min(pval))/1000
        for epsilon in np.arange(np.min(pval),np.max(pval),step):

            result=pval<epsilon  #1表示他是一个异常点
            TP=np.sum((result==1) & (Yval == 1).ravel()).astype(float)      #真正例
            TN=np.sum((result==0) & (Yval == 0).ravel()).astype(float)      #真负例
            FN=np.sum((result==0) & (Yval == 1).ravel()).astype(float)      #假负例
            FP=np.sum((result==1) & (Yval == 0).ravel()).astype(float)      #假正例
            precision=TP/(TP+FP)                              #精准率
            recision=TP/(TP+FN)                               #召回率
            #step=(np.max(pval)-np.min(pval))/random.randint(500,1500)
            F1 = (2*precision*recision)/(precision+recision)  # F1Score计算公式

            if F1 > bestF1:  # 修改最优的F1 Score
                bestF1 = F1
                bestEpsilon = epsilon
                bestTP=TP
                bestTN=TN
                bestFP=FP
                bestFN=FN

        bar=Bar("分析")
        bar.add("",["识别率","错误率","敏感度","特效性","精度","分数"],[(bestTP+bestTN)/(P+N),(bestFP+bestFN)/(P+N),bestTP/P,bestTN/N,bestTP/(bestTP+bestFP),bestF1])
        self.page.add(bar)
        return bestEpsilon,bestF1
