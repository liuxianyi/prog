#coding=utf-8
import tree
from pyecharts import Graph as Tu_Graph
from pyecharts import Page
import save_helper as sh
#data数据，格式为[[1-1节点权重，1-2节点权重，1-3节点权重]，[2-1节点权重，2-2节点权重，2-3节点权重]...],对于本节点的权重(例如1-1的权重)为0，如果不可达用max_value = 9999999
#dataN是每个节点名称
class MST:
    def mst(self,data=None,dataN=None,dataname="None",choice="prim"):
        page = Page()
        if data == None:
            max_value = 9999999
            row0 = [0,7,max_value,max_value,max_value,5]
            row1 = [7,0,9,max_value,3,max_value]
            row2 = [max_value,9,0,6,max_value,max_value]
            row3 = [max_value,max_value,6,0,8,10]
            row4 = [max_value,3,max_value,8,0,4]
            row5 = [5,max_value,max_value,10,4,0]
            data = [row0, row1, row2,row3, row4, row5]
            dataN=["节点1","节点2","节点3","节点4","节点5","节点6"]
        #对初始数据可视化
        link=[]
        node=[]
        n=len(data)
        m=len(data[0])
        for i in range(n):
            for j in range(m):
                if data[i][j] == max_value:
                    continue
                else:
                    link.append({"source":dataN[i],"target":dataN[j]})
            fdata=filter(lambda x : x!=max_value,data[i])
            big=reduce(lambda x,y:x+y,fdata)
            node.append({"name":dataN[i],"symbolSize":big})

        tu_graph=Tu_Graph("总关系图")
        tu_graph.add("",node,link)
        page.add(tu_graph)


        graph=tree.Graph(data)

        if choice == "prim":
            res=graph.prim()
        else:
            res=graph.kruskal()
        print(res)

        n1=len(res)
        m1=len(res[0])
        def sum2(x,y):
            if type(x) == int:
                return x+y[2]
            else:
                return x[2]+y[2]
        big=reduce(sum2,res)

        link2=[]
        for i in res:
            link2.append({"source":i[0],"target":i[1]})
        tu_graph2 = Tu_Graph("最小生成树图")
        tu_graph2.add("权重和为:"+str(big),node,link2)
        print(link2)
        page.add(tu_graph2)
        sh.save_tu_helper(page,dataname)
