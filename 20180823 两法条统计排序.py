import pandas as pd

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
            tail=data[j].find('》')
            if pos>0:
                k=data[j]
                k=k[0:pos]+k[pos+1:]
        for j in range(0,len(data)-1):
            for l in range(j,len(data)):
                str1=data[j]
                str2=data[l]
                if str1!=str2:
                    comb=str1+'+'+str2
                    comb2=str2+'+'+str1
                    if (not comb in dic) and (not comb2 in dic): 
                        dic[comb]=1
                    elif comb in dic:
                        dic[comb]+=1
                    else:
                        dic[comb2]+=1
        '''if x%1000==0 and x!=0:
            print(dic['《中华人民共和国侵权责任法》第十六条+《中华人民共和国道路交通安全法》第七十六条']) 
        '''
        if x%10000==0 and x!=0:
            print(x/10000,dic['《中华人民共和国侵权责任法》第十六条+《中华人民共和国道路交通安全法》第七十六条'])
            df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['num'])
            df1=df1[df1['num']>50]
            dic.clear()
            for temp in df1.index:
                dic[temp]=df1.loc[temp]['num']

df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['num'])       
op=df1.sort_values(by=['num'], ascending = False)
op.to_csv('两法条同时出现频率.csv',sep='\t')
