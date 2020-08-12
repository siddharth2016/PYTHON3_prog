# STAIRCASE

from sys import stdout, stdin
N = int(stdin.readline())
for i in range(N):
    A = ''
    for j in range(N-1-i):
        stdout.write(" ")
    for k in range(i+1):
        A += '#'
    stdout.write(A+"\n")
