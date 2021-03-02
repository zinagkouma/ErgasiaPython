f = open("inFile2.txt")
maxDepth=0
count=0
while True:
    c = f.read(1)
    if not c:
        break
    if c=='[' or c=='{':
        count+=1
    elif c==']' or c=='}':
        count-=1
    if count>maxDepth:
        maxDepth=count
print (maxDepth)
f.close()
