import os
a="demo/x/y/z"
os.makedirs(a,exist_ok=True)
print(os.path.exists(a))

s="demo"
print(os.listdir(s))

m="demo"
print([x for x in os.listdir(m) if os.path.isfile(os.path.join(m,x))])

d="demo"
print([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))])

q="demo"
w=".txt"
print([os.path.join(r,f) for r,_,t in os.walk(q) for f in t if f.endswith(w)])

e="demo"
r=".py"
print([f for f in os.listdir(e) if f.endswith(r)])

t="demo/a/b/c"
os.makedirs(t,exist_ok=True)
print(os.listdir("demo/a/b"))

y="demo"
u=[]
for i,j,k in os.walk(y): u+=k
print(u)

o="demo"
p=[]
for i,j,k in os.walk(o): p+=j
print(p)

h="demo"
l=[".jpg",".png"]
print([os.path.join(i,f) for i,_,k in os.walk(h) for f in k if any(f.endswith(c) for c in l)])