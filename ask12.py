fin = open("inFile3.txt")
x=[]
while True:
    c = fin.read(1)
    if not c:
        break
    x.append(chr(128-ord(c)))
while x:
    print(x.pop())
fin.close()
