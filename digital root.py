a=int(input("Enter the integer:"))
a1=str(a)
while len(a1)>1:
        sum=0
        for i in a1:
              sum+=int(i)
        a1=str(sum)
print(sum)