#JARVIS AND SEVEN SEGMENTS
test = int(input())
for i in range(test):
    num = int(input())
    numarr = str(input())
    numarr = numarr.split()
    minn = 50
    for j in range(num):
        num1 = numarr[j]
        countBulb = 0
        #print(num1)
        for k in range(len(num1)):
            if num1[k]=='0' or num1[k]=='6':
                countBulb += 6
            elif num1[k]=='1':
                countBulb += 2
            elif num1[k]=='2' or num1[k]=='3' or num1[k]=='5' or num1[k]=='9':
                countBulb += 5
            elif num1[k]=='4':
                countBulb += 4
            elif num1[k]=='7':
                countBulb += 3
            elif num1[k]=='8':
                countBulb += 7
        #print(countBulb)
        if countBulb<minn:
            reqBulb = num1
            minn = countBulb
        #print(minn)
    print(reqBulb)
    
