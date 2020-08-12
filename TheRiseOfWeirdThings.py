# THE RISE OF THE WEIRD THINGS

def insertionsort(Arr,n):
    for start in range(n):
        pos = start
        while pos>0 and Arr[pos]<Arr[pos-1]:
            (Arr[pos],Arr[pos-1]) = (Arr[pos-1],Arr[pos])
            pos -= 1
n = int(input())
Arr = list(map(int, input().split()))
insertionsort(Arr,n)
rese = ""
reso = ""
sme = smo = 0
for i in Arr:
    if i%2==0:
        rese += str(i) + " "
        sme += i
    else:
        reso += str(i) + " "
        smo += i
rese += str(sme) + " " + reso + str(smo)
print(rese)
