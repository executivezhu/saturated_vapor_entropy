import pandas as pd
import numpy as np

t_l=[0,10,20,40,60,80,
     100,120,140,160,180,
     200,220,240,260,280,
     300,350,400,420,440,450,460,480,
     500,520,540,550,580,600]
p_l=[0.01,0.1,0.5,1,3,5,7,10,14,20,25,30]

df=pd.read_csv('han_ref.csv')

import sys
t_input=float(sys.argv[1])
p_input=float(sys.argv[2])


for i,t_v in enumerate(t_l):
    if t_input<t_v:
        t_1=t_l[i-1]
        t_2=t_v
        target_i=i
        break
    else:
        continue
for j,p_v in enumerate(p_l):
    if p_input>p_v:
        p_1=p_l[j-1]
        p_2=p_v
        target_j=j
        break
    else:
        continue

'''
           p_1       p_input      p_2

t_1        a                       c


t_input    x1           x3         x2


t_2        b                        d


'''        
        
    
    
a=df.iloc[target_i-1,target_j-1]
b=df.iloc[target_i,target_j-1]
c=df.iloc[target_i-1,target_j]
d=df.iloc[target_i,target_j]

x1=a+(t_input-t_1)/(t_2-t_1)*(b-a)
x2=c+(t_input-t_1)/(t_2-t_1)*(d-c)

x3=x1+(p_input-p_1)/(p_2-p_1)*(x2-x1)
print(x3)







