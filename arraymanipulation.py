def arraymanipulation(n,q):
    a=[0]*n 
    for i in q:
        a[i[0]-1]+=i[2]
        if i[1]!=len(a):
            a[i[1]]-=i[2]
    m=0
    i=0
    for j in a:
        i+=j 
        if i>m:
            m=i 
    return m 
n=5
q=[[1, 2, 100], [2, 5, 100], [3, 4, 100]]
print(arraymanipulation(n,q))
    
