l=list(map(str,input().split()))
p=0
while (len(l)!=1):
    l.remove(l[p+1])
    if(p==len(l)-1):
        p=0
    elif(p==len(l)-2):
        l.remove(l[0])
        p=0
    else:
        p+=1
print(l)
