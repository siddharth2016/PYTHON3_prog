# DIGIT PROBLEM

num = str(input())
num = num.split()
x = num[0]
x = ' '.join(x)
x = x.split()
k = int(num[1])
i=0
while k!=0:
    if x[i]!='9':
        x[i]='9'
        k=k-1
        i=i+1
    elif x[i]=='9':
        i=i+1

x = ''.join(x)
print(x)


