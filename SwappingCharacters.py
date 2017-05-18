# SWAPPING CHARACTERS

from sys import stdin, stdout

for i in range(int(stdin.readline())):
    N = int(stdin.readline())
    s = [a for a in stdin.readline()]
    #print(s)
    for j in range(0,N-1,1):
        for k in range(j,N,2):
            if k+1>=N:
                continue
            temp = s[k]
            s[k] = s[k+1]
            s[k+1] = temp
    stdout.write(''.join(s)+'\n')
