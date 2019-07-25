import pandas as pd

df=pd.read_csv("DataFrame.csv",sep="\t")
#data=df.iloc[:,0:18]
judge=df.loc[:,['0案号','2行政区划（省）','21审判组织成员']]
dic={}
dic2={}
a=[]

for i in range(0,judge.shape[0]):
    x=judge.iloc[i,2]
    prov=judge.iloc[i,1]
    if str(x)=='nan' or str(prov)=='nan':
        continue
    elif x.find('人民陪审员')!=-1 or (x.find('审判长')!=-1 and x.find('审判员')!=-1):
        if prov in dic:
            dic[prov]+=1
        else:
            dic[prov]=1
    else:
        if prov in dic2:
            dic2[prov]+=1
        else:
            dic2[prov]=1

df1=pd.DataFrame(list(dic.values()), index=dic.keys(), columns=['非独任审判num'])  
df2=pd.DataFrame(list(dic2.values()), index=dic2.keys(), columns=['独任审判num'])      
#op=df1.sort_values(by=['num'], ascending = False)
ans=pd.concat([df1,df2], axis=1, sort=False)
#ans.to_csv('独任审判&province.csv', sep='\t')
'''
doc = open('独任审判.txt','w')
print(a,file=doc)
doc.close()'''