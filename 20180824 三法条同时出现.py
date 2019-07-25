import pandas as pd

df=pd.read_csv("DataFrame.csv",sep="\t")
law=df.loc[:,'12法律法条分组']

dic={}

for x in range(0,law.size):
    i=law[x]
    if str(i)!='nan':
        data=i.split(',')
        if data[len(data)=='']:
            del data[len(data)-1]
        data.sort()
        for j in range(0,len(data)):
            pos=data[j].find('《')
            tail=data[j].find('》')
            if pos>0:
                k=data[j]
                k=k[0:pos]+k[pos+1:]
        for j in range(0,len(data)-2):
            for l in range(j+1,len(data)-1):
                for m in range(l+1,len(data)):
                    if data[j]!=data[l] and data[j]!=data[m]:
                        if data[l]==data[m]:
                            print(l,m)
                        comb=data[j]+'+'+data[l]+'+'+data[m]
                        if not comb in dic: 
                            dic[comb]=1
                        else:
                            dic[comb]+=1
        
        if x%1000==0 and x!=0:
            print(len(dic))
            df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['num'])
            df1=df1[df1['num']>10]
            dic.clear()
            for temp in df1.index:
                dic[temp]=df1.loc[temp]['num']

df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['num'])       
op=df1.sort_values(by=['num'], ascending = False)
#op.to_csv('三法条同时出现频率.csv',sep='\t')