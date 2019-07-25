import pandas as pd
import numpy as np

f=open('amountresult.txt','r')
money=[]
#law=df.loc[:,'12法律法条分组']
for line in f.readlines():
    money.append(float(line.strip()))
f.close()

f=open('独任审判01.txt','r')
a=f.read()
tf=a.split(', ')
#law=df.loc[:,'12法律法条分组']
for line in f.readlines():
    money.append(float(line.strip()))
f.close()

df=pd.read_csv("data10000.csv",sep="\t")
judge=df.loc[:,['0案号','2行政区划（省）']]
dic={}
dic2={}
dic_num={}
dic2_num={}
for i in range(0,judge.shape[0]):

    prov=judge.iloc[i,1]
    if tf[i]=='-1':
        continue
    elif tf[i]=='1':
        if prov in dic:
            dic[prov]+=money[i]
        else:
            dic[prov]=money[i]
    else:
        if prov in dic2:
            dic2[prov]+=money[i]
        else:
            dic2[prov]=money[i]
#for x in range(0,law.size):
    
df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['非独任审判'])  
df2=pd.DataFrame(list(dic2.values()), index=dic2.keys(), columns=['独任审判'])  
res=pd.concat([df1,df2], axis=1, sort=False)
#df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['num'])       
#op=df1.sort_values(by=['num'], ascending = False)
