#ENUMERATE:
a=["table","qwezt","lemon","brx"]
for i,x in enumerate(a): print(i,x)

s=["cloud","xkq","window","plmno"]
for j,x in enumerate(s): print(j,x)

m=["river","zzta","pencil","worfle"]
for k,x in enumerate(m,1): print(k,x)

d=["stone","abcx","orange","trivo"]
for p,x in enumerate(d): print("index =",p,"value =",x)

q=["planet","mzr","coffee","lqetp"]
for h,x in enumerate(q,5): print(h,x)

w=["tiger","vbnm","mirror","zarp"]
for b,x in enumerate(w): print(x,len(x),b)

e=["alpha","skri","bread","nopqx"]
for n,x in enumerate(e): print(n,x.upper())

r=["aqua","blim","forest","xxrt"]
for u,x in enumerate(r): print(str(u)+": "+x)

t=["math","qazpl","rocket","trun"]
for f,x in enumerate(t): print("item",f+1,":",x)

y=["one","zqx","paper","mtevo"]
print(list(enumerate(y)))
#ZIP
a=list(range(5)); s=[x*x for x in range(5)]; print(list(zip(a,s)))

m=[chr(97+x) for x in range(6)]; d=[x+10 for x in range(6)]; print(list(zip(m,d)))

q="table chair lamp".split(); w=[len(x) for x in q]; print(list(zip(q,w)))

e=[2**x for x in range(6)]; r=[3**x for x in range(6)]; print(list(zip(e,r)))

t=[x for x in range(10) if x%2==0]; y=[x for x in range(10) if x%2!=0]; print(list(zip(t,y)))

u=[str(x)+"kg" for x in range(1,6)]; i=[x*1000 for x in range(1,6)]; print(list(zip(u,i)))

o=[chr(65+x) for x in range(5)]; p=["x"+str(x) for x in range(5)]; h=[x%2==0 for x in range(5)]; print(list(zip(o,p,h)))

j=[x/10 for x in range(5,10)]; k=[round(x*1.8+32,1) for x in j]; print(list(zip(j,k)))

l=["ab"+str(x) for x in range(4)]; c=[x[::-1] for x in l]; print(list(zip(l,c)))

v=[x for x in "qwerty"]; b=[ord(x) for x in v]; print(list(zip(v,b)))