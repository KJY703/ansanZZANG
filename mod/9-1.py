""" import os

fp = "test.py"
#fp = "temp1.txt"

#file = open(fp, "w")

if os.path.exists(fp) :
    print("ok")
    file = open("temp.txt", "a")
else :
    print("error")
    file = open("temp.txt", "w")
    
#file.close()
    
#exception file read """



""" import os

fp = "temp.txt"

if os.path.exists(fp) :
    f = open(fp, "r")
    for line in f :
        print(line)
else :
    f = open(fp, "w")
    for i in range(100):
        f.write(str(i) + "\n")
    #print("error")
    
f.close() """



""" import os

fp = "new.txt"

f = open(fp, "w")
f.close()

os.remove(fp)
print("complete") """



""" import os

def dir_point(p):
    files = os.listdir(p)
    for f in files :
        print(f)
        
fp = "new.txt"

f = open(fp, "w")
f.close()

dir_point("./")

os.remove(fp)
print("\n----------------------\n\n")
dir_point("./") """




""" import os

fp = "new.txt"

f = open(fp, "w")
f.close()

os.rename(fp, "new1.txt")
print("complete") """



""" import os

fp = "new.txt"
tp = "new1.txt"

f= open(fp, "w")
f.close()

if os.path.exists(tp):
    print("exist, same name file")
    os.remove(tp)
else :
    os.rename(fp, "new1.txt")
    print("complete") """
    
    

    
""" import os

def dir_point(p):
    files = os.listdir(p)
    for f in files :
        print(f)
        
fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

dir_point("./")
print("\n----------------------\n\n")


if os.path.exists(tp):
    os.remove(tp)
    dir_point("./")
    print("exist, same name file")
else :
    os.rename(fp, "new1.txt")
    dir_point("./")
    print("complete") """
    
    
    
#f = open("temp.txt", "r")
with open("temp.txt", "r") as f :
    print(f.read())
    
    #for i in range(110):
        #res = f.readline()
        #print(res)