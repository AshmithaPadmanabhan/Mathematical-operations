a=list(map(str,input("Enter the string array:").split()))
n=len(a)
for i in a:
    s1=1
    l1=len(i)
    for j in i:
        if j in 'AEIOUaeiou':
            l1-=1
    if l1==0:
        print('0')
    else:
        for k in range(l1,0,-1):
            s1*=k
        print(s1)