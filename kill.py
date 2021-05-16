l=list(map(str, input().split()))
c=0
f=0
l2=[]
if(f==0):
    l1=[x for x in l]
    f=f+1
while (len(l)!=1):
    if(c==0):
        l=l[::2]
        c=c+1
        l2=l1
        l1=l
    else :
        if(l[len(l)-1]==l2[len(l2)-1]):
            l=l[1::2]
            l2=l1
            l1=l
        else :
            l=l[::2]
            l2=l1
            l1=l
print(''.join(l))
