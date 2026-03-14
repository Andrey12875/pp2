import os,shutil

a="src1"; s="bak1"; os.makedirs(a,exist_ok=True); os.makedirs(s,exist_ok=True); open(os.path.join(a,"qwe.txt"),"w").write("abc"); shutil.copy(os.path.join(a,"qwe.txt"),os.path.join(s,"qwe.txt")); print(os.listdir(s))

m="src2"; d="bak2"; os.makedirs(m,exist_ok=True); os.makedirs(d,exist_ok=True); open(os.path.join(m,"zrt.txt"),"w").write("def"); shutil.copy2(os.path.join(m,"zrt.txt"),os.path.join(d,"zrt_backup.txt")); print(os.listdir(d))

q="src3"; w="bak3"; os.makedirs(q,exist_ok=True); os.makedirs(w,exist_ok=True); open(os.path.join(q,"xop.txt"),"w").write("ghi"); shutil.copy(os.path.join(q,"xop.txt"),w); print(open(os.path.join(w,"xop.txt")).read())

e="src4"; r="bak4"; os.makedirs(e,exist_ok=True); os.makedirs(r,exist_ok=True); open(os.path.join(e,"mvn.txt"),"w").write("jkl"); shutil.copytree(e,r,dirs_exist_ok=True); print(os.listdir(r))

t="safe1.txt"; open(t,"w").write("qwe"); print(os.path.exists(t)); os.remove(t) if os.path.exists(t) else None; print(os.path.exists(t))

y="safe2.txt"; print(os.path.exists(y)); os.remove(y) if os.path.exists(y) else print("not found")

u="box5"; i="box6"; os.makedirs(u,exist_ok=True); os.makedirs(i,exist_ok=True); [open(os.path.join(u,f"f{x}.txt"),"w").write(str(x)) for x in range(3)]; [shutil.copy(os.path.join(u,z),os.path.join(i,z)) for z in os.listdir(u)]; print(os.listdir(i))

o="one.txt"; p="one_backup.txt"; open(o,"w").write("rst"); shutil.copy(o,p); print(open(p).read())

h="kill1.txt"; open(h,"w").write("uvw"); print(os.path.isfile(h)); os.remove(h) if os.path.isfile(h) else None; print(os.path.isfile(h))

j="delbox"; os.makedirs(j,exist_ok=True); open(os.path.join(j,"asd.txt"),"w").write("xyz"); shutil.rmtree(j) if os.path.isdir(j) else None; print(os.path.exists(j))