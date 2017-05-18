# TIME CONVERSION

s = input().strip()
#print(s[-1:-3:-1])
if s[-1:-3:-1]=='MP' and s[0:2]!='12':
    a = (int(s[0:2])+12)%24
    print(str(a) + s[2:8])
elif s[-1:-3:-1]=='MP' and s[0:2]=='12':
    print(s[0:8])
elif s[-1:-3:-1]=='MA' and s[0:2]!='12':
    print(s[0:8])
else:
    print("00" + s[2:8])
