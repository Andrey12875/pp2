import os,shutil
a="demo_src"; s="demo_dst"; os.makedirs(a,exist_ok=True); os.makedirs(s,exist_ok=True); open(os.path.join(a,"note.txt"),"w").write("hello"); shutil.copy(os.path.join(a,"note.txt"),os.path.join(s,"note.txt")); print(os.listdir(s))

m="demo_src2"; d="demo_dst2"; os.makedirs(m,exist_ok=True); os.makedirs(d,exist_ok=True); open(os.path.join(m,"data.csv"),"w").write("1,2,3"); shutil.move(os.path.join(m,"data.csv"),os.path.join(d,"data.csv")); print(os.listdir(d))

q="demo_a"; w="demo_b"; os.makedirs(q,exist_ok=True); os.makedirs(w,exist_ok=True); open(os.path.join(q,"clock.png"),"w").write("x"); shutil.copy2(os.path.join(q,"clock.png"),os.path.join(w,"clock.png")); print(os.listdir(w))

e="demo_c"; r="demo_d"; os.makedirs(e,exist_ok=True); os.makedirs(r,exist_ok=True); open(os.path.join(e,"log.txt"),"w").write("abc"); shutil.move(os.path.join(e,"log.txt"),r); print(os.listdir(r))

t="folder1"; y="folder2"; os.makedirs(t,exist_ok=True); os.makedirs(y,exist_ok=True); [open(os.path.join(t,f"f{x}.txt"),"w").write(str(x)) for x in range(3)]; [shutil.copy(os.path.join(t,z),os.path.join(y,z)) for z in os.listdir(t) if z.endswith(".txt")]; print(os.listdir(y))

u="box1"; i="box2"; os.makedirs(u,exist_ok=True); os.makedirs(i,exist_ok=True); [open(os.path.join(u,f"a{x}.py"),"w").write("print(1)") for x in range(2)]; [shutil.move(os.path.join(u,z),os.path.join(i,z)) for z in os.listdir(u) if z.endswith(".py")]; print(os.listdir(i))

o="main_src/sub"; p="main_dst"; os.makedirs(o,exist_ok=True); os.makedirs(p,exist_ok=True); open(os.path.join(o,"deep.txt"),"w").write("ok"); shutil.copy(os.path.join(o,"deep.txt"),os.path.join(p,"deep.txt")); print(os.listdir(p))

h="copy_tree_src"; l="copy_tree_dst"; os.makedirs(h,exist_ok=True); open(os.path.join(h,"a.txt"),"w").write("a"); open(os.path.join(h,"b.txt"),"w").write("b"); shutil.copytree(h,l,dirs_exist_ok=True); print(os.listdir(l))

j="move_here"; k="move_there"; os.makedirs(j,exist_ok=True); os.makedirs(k,exist_ok=True); open(os.path.join(j,"one.md"),"w").write("text"); open(os.path.join(j,"two.md"),"w").write("text"); [shutil.move(os.path.join(j,z),k) for z in os.listdir(j) if z.endswith(".md")]; print(os.listdir(k))

v="from_dir"; b="to_dir"; os.makedirs(v,exist_ok=True); os.makedirs(b,exist_ok=True); open(os.path.join(v,"report.pdf"),"w").write("pdf"); shutil.copy(os.path.join(v,"report.pdf"),b); print(os.listdir(b))