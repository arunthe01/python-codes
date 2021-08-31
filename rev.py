st=input("enter input = ")
i = len(st)-2
rev= st[len(st)-1]
while i>=0 :
  rev=rev+st[i]
  i-=1
print(rev)
