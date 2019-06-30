a=[1,4,3,5,2,6]
a.sort()
d=11
def threesum(a,d):
    k=0
    i=k+1
    j=len(a)-1
    while(k<i<j):
        while(i<j):
            if (a[k]+a[i]+a[j])>d:
                j-=1
            elif (a[k]+a[i]+a[j])<d:
                i+=1
            else:
                print(a[k],a[i],a[j])
                i+=1 
                j-=1
        k+=1
        i=k+1
        j=len(a)-1
threesum(a,d)
