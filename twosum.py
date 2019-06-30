def twosum(a,d):
    a.sort()
    i=0
    j=len(a)-1
    b=[]
    while(i<=j):
        if (a[i]+a[j])>d:
            j-=1
        elif (a[i]+a[j])<d:
            i+=1
        else: 
            i+=1 
            j-=1
            b.append((a[i],a[j]))
    return b

a=[1,4,3,5,2]
d=4
print(twosum(a,d))
