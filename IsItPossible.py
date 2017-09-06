# IS IT POSSIBLE...?

from sys import stdin, stdout
for _ in range(int(stdin.readline())):
    n = stdin.readline()
    if n[-2]=='0' or n[-2]=='2' or n[-2]=='4' or n[-2]=='6' or n[-2]=='8':
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
