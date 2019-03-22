#encoding=utf-8
from pyecharts import WordCloud,Page,Pie,Style
import jieba,jieba.analyse
import numpy
import save_helper
#默认选取文本前十个做关键词
class GJC:
    def GuanJianCi(self,data_name="None",num=20,text=None):
        page = Page()
        if text == None:
            text="SimHash是一种局部敏感hash，它也是Google公司进行海量网页去重使用的主要算法。传统的Hash算法只负责将原始内容尽量均匀随机地映射为一个签名值，原理上仅相当于伪随机数产生算法。传统的hash算法产生的两个签名，如果原始内容在一定概率下是相等的；如果不相等，除了说明原始内容不相等外，不再提供任何信息，因为即使原始内容只相差一个字节，所产生的签名也很可能差别很大。所以传统的Hash是无法在签名的维度上来衡量原内容的相似度，而SimHash本身属于一种局部敏感哈希算法，它产生的hash签名在一定程度上可以表征原内容的相似度。我们主要解决的是文本相似度计算，要比较的是两个文章是否相似，当然我们降维生成了hash签名也用于这个目的。看到这里估计大家就明白了，我们使用的simhash就算把文章中的字符串变成 01 串也还是可以用于计算相似度的，而传统的hash却不行。"

        tags=jieba.analyse.extract_tags(text,topK=num,withWeight=True,withFlag=True)

        name = []
        value = []

        for tag in tags:
            name.append(tag[0])
            value.append(tag[1])
        print(value)
        wordCloud=WordCloud(data_name)
        wordCloud.add("",name,value)

        pie = Pie('前十个词汇占重', "", title_pos='center')
        style = Style()
        pie_style = style.add(
            label_pos="center",
            is_label_show=True,
            label_text_color=None
        )

        hight = 10
        width = 30
        sum_Wight = sum(value)
        for index,(n,v) in enumerate(zip(name,value)):

            if index == 5:
                hight = 10
                width = width +40
            if index < 10:
                pie.add(
                    "", [n, ""], [v/sum_Wight,1-v/sum_Wight], center=[hight,width], radius=[18, 24], **pie_style
                    )
                hight = hight + 20
                print (hight,width)
                print index


        page.add(pie)
        page.add(wordCloud)
        save_helper.save_tu_helper(page,data_name)
