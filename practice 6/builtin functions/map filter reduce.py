#REDUCE EXAMPLES:
from functools import reduce

from functools import reduce
nums=[1,2,3,4,5]
print(reduce(lambda a,b:a+b,nums))

nums=[1,2,3,4,5]
print(reduce(lambda a,b:a*b,nums))

words=["I","you","we"]
print(reduce(lambda a,b:a+" "+b,words))

nums=[12,7,25,3,18]
print(reduce(lambda a,b:a if a>b else b,nums))

nums=[12,7,25,3,18]
print(reduce(lambda a,b:a if a<b else b,nums))

transactions=[200,-50,100,-20,300]
print(reduce(lambda a,b:a+b,transactions))

letters=["m","y","t","t","o","n"]
print(reduce(lambda a,b:a+b,letters))

nums=[5,8,2,9]
print(reduce(lambda a,b:a+b*b,nums,0))

prices=[1200,800,1500,600]
print(reduce(lambda a,b:a+b,prices))

nums=[2,4,6,8]
print(reduce(lambda a,b:(a+b)/2,nums))

#MAP:
a=[1,2,3,4,5]
print(list(map(lambda x:x*x,a)))

sqd=[1,2,3,4,5]
print(list(map(lambda x:x*2,s)))

m=[0,20,30,40]
print(list(map(lambda x:x*9/5+32,m)))

z=["python","map","fun"]
print(list(map(lambda x:x.upper(),zd)))

a=["A","D","N"]
print(list(map(lambda x:"Hello "+x,a)))

sjkhl=[1,2,3,4,5]
print(list(map(lambda x:x%2==0,s)))

asd=[1200,800,1500]
print(list(map(lambda x:x*0.9,m)))

d=[(2,3),(4,5),(6,7)]
print(list(map(lambda x:x[0]*x[1],zd)))

x=["apple","banana","kiwi"]
print(list(map(len,a)))

z=[-3,7,-1,9,-5]
print(list(map(abs,s)))

#FILTER
a=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,a)))

s=[1,2,3,4,5,6]
print(list(filter(lambda x:x>3,s)))

m=[-5,3,-2,7,0]
print(list(filter(lambda x:x>=0,m)))

zd=["cat","elephant","dog","tigr"]
print(list(filter(lambda x:len(x)>3,zd)))

q=["A","D","","B"," "]
print(list(filter(lambda x:x.strip()!="",q)))

w=[12,15,18,21,24]
print(list(filter(lambda x:x%3==0,w)))

e=["appl","banan","ki","avocado"]
print(list(filter(lambda x:"a" in x,e)))

r=[100,450,700,1200,300]
print(list(filter(lambda x:x>=500,r)))

t=[True,False,True,False,True]
print(list(filter(lambda x:x,t)))

y=["python","map","filter","reduce","fun"]
print(list(filter(lambda x:x.startswith("f"),y)))