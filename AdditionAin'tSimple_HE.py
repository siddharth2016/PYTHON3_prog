# ADDITION AIN'T SIMPLE

def addition(strr, strr1):
    s = ""
    for i in range(0,len(strr),1):
        ch = ord(strr[i]) - 96
        ch1 = ord(strr1[i]) - 96
        add = ch + ch1
        
        if add%26 == 0:
            s = s + 'z'
        else:
            res = add%26 + 96
            s = s + chr(res)
    return s

n = int(input())
for i in range(0,n,1):
    strr = str(input())
    strr1 = strr[::-1]
    print(addition(strr,strr1))
