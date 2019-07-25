### color_map.py
import pandas as pd
from bs4 import BeautifulSoup

'''
data=pd.read_csv('province.csv', sep='\t')
data=data.iloc[0:31,:]

for i in range(0,data.shape[0]):
    province[data.iloc[i,0]]=data.iloc[i,1]
'''

# Load the SVG map
svg = open('newbs.svg','rb').read()
 
# Load into Beautiful Soup
soup = BeautifulSoup(svg, 'lxml')#selfClosingTags=['defs','sodipodi:namedview'])

# Find counties
paths = soup.findAll('path')
 
# Map colors
colors = ['#f1e1ff', '#e6caff', '#dcb5ff', '#d3a4ff', '#ca8eff', '#be77ff',
          "#b158ff", '#9f35ff', "#921aff",
          "#8600ff", '#6f00d2',"#5b00ae", "#4b0091", '#3a006f']
 
# County style
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
dic={'_40576896':'黑龙江','_40576568':'吉林','_40578648':'辽宁',
     '_40578320':'河北','_40578848':'山东','_40567464':'江苏',
     '_40566848':'浙江','_40569488':'安徽','_40562416':'河南',
     '_40562088':'山西','_39889000':'陕西','_40549512':'甘肃',
     '_40549184':'湖北','_40548664':'江西','_40524208':'湖南',
     '_40526624':'贵州','_40526296':'四川','_40529848':'云南',
     '_40521872':'青海','_40508216':'海南','_40506856':'重庆',
     '_40513120':'天津','_40512392':'北京','_40509384':'宁夏',
     '_40499616':'内蒙古','_40498944':'广西','_40446064':'新疆',
     '_40437568':'西藏','_40506880':'上海','_39191984':'上海',
     '_40547808':'福建','_40524296':'广西'}

# Color the counties based on unemp_39889000loyment rate
cnt=0
for p in paths:
    cnt+=1
    print(cnt,p['id'])
    
    #if p['id']=='_40524296':
    if p['id'] in dic:
        
        rate = proportion[dic[p['id']]]
        if rate > 11:
            color_class = 13
        elif rate > 10:
            color_class = 12
        elif rate > 9:
            color_class = 11
        elif rate > 8:
            color_class = 10
        elif rate > 7:
            color_class = 9
        elif rate > 6:
            color_class = 8
        elif rate > 5:
            color_class = 7
        elif rate>4:
            color_class = 6
        elif rate > 3:
            color_class = 5
        elif rate > 2.5:
            color_class = 4
        elif rate > 2:
            color_class = 3
        elif rate > 1.5:
            color_class = 2
        elif rate > 1:
            color_class = 1
        else:
            color_class = 0
         
        color = colors[color_class]
        
        p['style'] = path_style + color
    else:
        p['style'] = path_style + colors[0]
soup=soup.prettify()

f=open('proportionsoup.html','w')
f.write(soup)
f.close()