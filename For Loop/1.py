import random as r
i=0
o,s,x,c=0,0,0,0
while(i!=200):
    y=x
    x=r.randrange(1,7)
    if x==1:
        o+=1
    elif x==6:
        if y==6:
            c+=1
        s+=1
    i+=1
print("Times rolled a 6: ",s)
print("Times rolled a 1: ",o)
print("Times rolled 2 6's: ",c)