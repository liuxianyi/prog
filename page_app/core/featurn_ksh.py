#coding=utf-8
import pyecharts, random
#助手函数
#一般的三点图，不同种类的点用 "FG" 隔开
#格式为  "图名"，“点名”，数据.... "FG" ，"点名"，数据...
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
    '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']

def ksh_scatter(*data):
    n=len(data)

    if "FG" in data:
        m=4

        lamble=0        #数据是2D为0,3D为1
        if data[m] == "FG" :
            scatter=pyecharts.Scatter(data[0])
            scatter.add(data[m-3],data[m-2],data[m-1])

        else :
            scatter=pyecharts.Scatter3D(data[0], width=1200, height=600)
            scatter.add(data[m-3],data[m-2],is_visualmap=True, visual_range_color=range_color)
            lamble=1

        while m<=n:
            if lamble == 0:
                scatter.add(data[m-3],data[m-2],data[m-1])
                m=m+4
            else:
                print(m)
                scatter.add(data[m],data[m+1],is_visualmap=True, visual_range_color=range_color)
                m=m+3


    if n == 4:
        scatter=pyecharts.Scatter(data[0])
        scatter.add(data[1],data[2],data[3])
    if n == 3:
        scatter=pyecharts.Scatter3D(data[0], width=1200, height=600)
        scatter.add(data[1],data[2],data[3],data[4],is_visualmap=True,visual_range_color=range_color)
    return scatter
