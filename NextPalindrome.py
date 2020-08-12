# NEXT PALINDROME           #NOT GOOD FOR LENGHT OVER 100 DIGITS
from sys import stdin,stdout
for i in range(int(stdin.readline())):
    N = int(stdin.readline())
    j = 1
    x = N
    while j:
        x = x+1
        y = str(x)
        y1 = y[::-1]
        if y==y1:
            stdout.write(y+'\n')
            j=0
        
