import pandas as pd
import matplotlib.pyplot as plt
import re
#df_age=pd.read_csv('age.csv', sep='\t')
'''f=open('prov_age.txt','r')
s=f.read()
f.close()
data=re.findall('\'(.*?)\'',s)
dd=df_age.iloc[:,1:]

'''
dic={}
ss='辽宁 吉林 黑龙江 内蒙古 河北 山西 陕西 宁夏 山东 安徽 江苏 浙江 上海 北京 重庆 天津 河南 湖北 湖南 江西 福建 云南 海南 四川 贵州 广东 广西 甘肃 新疆 西藏 青海'
pl=ss.split(' ')

for pn in pl: #pn=province name, pl=province name list
    sn=0
    sa=0
    for i in range(0,dd.shape[0]):
        if data[i]==pn:
            length=dd.loc[i,'length']
            for j in range(0,length):
                age=dd.loc[i,str(j)]
                if age>=120 or age<0:
                    continue
                sa+=age
            sn+=length
    dic[pn]=sa/sn
    res_age=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['Average'])
    res_age.to_excel('age_averagepro.xlsx')
