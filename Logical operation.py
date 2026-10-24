a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
a1 = bin(a)[2:]
b1 = bin(b)[2:]
s = ''
if len(a1) < 4:
    a1='0'*(4-len(a1))+a1
if len(b1)<4:
    b1='0'*(4-len(b1))+b1
print(a1, b1)
for i in range(4):
    if a1[i] == '1' or b1[i] == '1':
        s+='1'
    else:
        s+='0'
print(s)
print(int(s, 2))