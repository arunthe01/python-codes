n= int(input("enter a number"))
status = True 
for i in range(2,n//2):
    if(n%i==0):
        status=False
        break
        
if(status):
    print(" prime")
else:
    print("not prime")
