# REST IN PEACE -21-1!

for i in range(int(input())):
    s = input().strip()
    sn = int(s)
    if s.count('21') or sn%21==0:
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
