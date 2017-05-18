# BALANCED STRINGS          #INCOMPLETE
    
for i in range(int(input())):
    s = input().strip()
    count = 0
    for j in range(0,len(s)-1,1):
        x = ord(s[j])
        for k in range(j+1,len(s),1):
            x ^= ord(s[k])
            if x==0:
                count += 1
    print(count)
        
    
