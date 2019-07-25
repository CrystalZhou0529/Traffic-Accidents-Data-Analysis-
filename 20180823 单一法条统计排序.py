import pandas as pd
import numpy as np

df=pd.read_csv("DataFrame.csv",sep="\t")
prov=df.loc[:,'12法律法条分组']

dic={}

for x in range(0,prov.size):
    i=prov[x]
    if str(i)!='nan':
        data=i.split(',')
        del data[len(data)-1]
        for j in range(0,len(data)):
            pos=data[j].find('《')
            if pos!=0:
                k=data[j]
                #print(k)
                k='《'+k[0:pos]+k[pos+1:]
                #print(k)
                data[j]=k
                if not k in dic: 
                    dic[k]=1
                else:
                    dic[k]+=1
                    
data=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['num'])
op=data.sort_values(by=['num'], ascending = False)

op.to_csv('单一法条出现频率.csv',sep="\t")