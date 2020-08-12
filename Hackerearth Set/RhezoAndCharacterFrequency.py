# RHEZO AND CHARACTER FREQUENCY

string = str(input())
c = str(input())
p = int(input())
z = -1
for i in range(0,len(string)-p,1):
    ss = string[i:i+p:1].count(c)
    if ss>z:
        z = ss
#print(z)
if p==1:
    print('-1')

else:
    maxi = -1
    for i in range(0,len(string)-p+1,1):
        ss = list(string[i:i+p:1])
        #print(ss)
        for j in range(0,p+1,1):
            ss.insert(j,c)
            #print(ss)
            sscount = ss[0:p].count(c)
            sscount1 = ss[1:p+1].count(c)
            #print(sscount)
            if sscount == z+1 and maxi<=i+j:
                maxi = i+j
                #print(maxi)
            if sscount1 == z+1 and maxi<=i+j:
                maxi = i+j
                #print(maxi)
            ss = list(string[i:i+p:1])
    print(maxi)
