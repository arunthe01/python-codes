password="the01"
word=True
i=0
match=True
while i<3 :
  curr=input("enter pass")
  if(curr==password):
    match=False
    break
  i+=1
if(match):
  print("wrong")
else:
  print("correct")
