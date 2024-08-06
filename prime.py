a=7
c=0
for i in range(1,a):
    if a%i==0:
        c=c+1
if c>1:
    print("Not a prime")
else:
    print("prime")
        