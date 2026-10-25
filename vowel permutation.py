s=input("Enter a string:")
l=len(s)
for i in s:
    if i in 'aeiouAEIOU':
        l-=1
s1=1
for i in range(l,0,-1):
    s1*=i
print(s1)