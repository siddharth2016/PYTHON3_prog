# GENERATING ALL BINARY STRINGS AND K-ARY STRINGS

n = int(input("Enter number of bits: "))
Arr = ['0']*n
def binary(n):
    if n<1:
        print(''.join(Arr))
    else:
        Arr[n-1] = '0'
        binary(n-1)
        Arr[n-1] = '1'
        binary(n-1)
binary(n)
k = int(input("Enter K: "))
def kary(n):
    if n<1:
        print(''.join(Arr))
    else:
        for i in range(0,k,1):
            Arr[n-1] = str(i)
            kary(n-1)
kary(n)
