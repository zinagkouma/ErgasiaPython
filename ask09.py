fin = open("inFile.txt")
fout=open("outFile.txt",'w')
while True:
    c = fin.read(1)
    if not c:
        break
    n=ord(c)
    if n%2==1:
        fout.write(c)
fin.close()
fout.close()
fout=open("outFile.txt")
ff=fout.read()
freq = {} 
for i in ff: 
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1
for i in freq:
  print(i,':',freq[i]*'*')
fout.close()
