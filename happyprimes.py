# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:43:18 2019

@author: Simran
"""

with open("other.txt",mode='w+') as f:
    l=['4', '16', '37', '58', '89', '145', '42', '20']
    x=['1','10','100','1000','10000']
    for i in range(1,1000):
        sum=0
        j=str(i)
        while True:
            for m in range(len(j)):
                n=int(j[m])
                sum=sum+(n**2)
            sum=str(sum)
            if sum in l:
                break
            elif sum in x:
                f.write(str(i)+'\n')
                break
            else:
                j=sum
                sum=0
    f.seek(0)
    h=f.readlines()
    
with open("one.txt",mode='w+') as fo:
    for n in range(2,1000):
        flag=0
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                flag+=1
                break
        if flag==0:
            fo.write(str(n)+'\n')
    fo.seek(0)
    p=fo.readlines()

happyprimes= []
for i in h:
    if i in p:
        happyprimes.append(i)
        
happyprimes=''.join(happyprimes)
print(happyprimes)