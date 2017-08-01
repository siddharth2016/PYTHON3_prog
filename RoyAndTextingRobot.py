# ROY AND TEXTING ROBOT

for _ in range(int(input())):
    counttime = 0
    flag = 1
    st = str(input())
    for i in st:
        if i in ['.', ',' , '?' , '!' , '1']:
            if flag!=1:
                counttime += 1
                flag = 1
            if i=='.':
                counttime += 1
            elif i==',':
                counttime += 2
            elif i=='?':
                counttime += 3
            elif i=='!':
                counttime += 4
            elif i=='1':
                counttime += 5
        elif i in ['a' , 'b' , 'c' , '2']:
            if flag != 2:
                counttime += 1
                flag = 2
            if i=='a':
                counttime += 1
            elif i=='b':
                counttime += 2
            elif i=='c':
                counttime += 3
            elif i=='2':
                counttime += 4
        elif i in ['d' , 'e' , 'f' , '3']:
            if flag != 3:
                counttime += 1
                flag = 3
            if i=='d':
                counttime += 1
            elif i=='e':
                counttime += 2
            elif i=='f':
                counttime += 3
            elif i=='3':
                counttime += 4
        elif i in ['g' , 'h' , 'i' , '4']:
            if flag != 4:
                counttime += 1
                flag = 4
            if i=='g':
                counttime += 1
            elif i=='h':
                counttime += 2
            elif i=='i':
                counttime += 3
            elif i=='4':
                counttime += 4
        elif i in ['j' , 'k' , 'l' , '5']:
            if flag != 5:
                counttime += 1
                flag = 5
            if i=='j':
                counttime += 1
            elif i=='k':
                counttime += 2
            elif i=='l':
                counttime += 3
            elif i=='5':
                counttime += 4
        elif i in ['m' , 'n' , 'o' , '6']:
            if flag != 6:
                counttime += 1
                flag = 6
            if i=='m':
                counttime += 1
            elif i=='n':
                counttime += 2
            elif i=='o':
                counttime += 3
            elif i=='6':
                counttime += 4
        elif i in ['p' , 'q' , 'r' , 's' , '7']:
            if flag!=7:
                counttime += 1
                flag = 7
            if i=='p':
                counttime += 1
            elif i=='q':
                counttime += 2
            elif i=='r':
                counttime += 3
            elif i=='s':
                counttime += 4
            elif i=='7':
                counttime += 5
        elif i in ['t' , 'u' , 'v' , '8']:
            if flag != 8:
                counttime += 1
                flag = 8
            if i=='t':
                counttime += 1
            elif i=='u':
                counttime += 2
            elif i=='v':
                counttime += 3
            elif i=='8':
                counttime += 4
        elif i in ['w' , 'x' , 'y' , 'z' , '9']:
            if flag != 9:
                counttime += 1
                flag = 9
            if i=='w':
                counttime += 1
            elif i=='x':
                counttime += 2
            elif i=='y':
                counttime += 3
            elif i=='z':
                counttime += 4
            elif i=='9':
                counttime += 5
        elif i in ['_' , '0']:
            if flag!=0:
                counttime += 1
                flag = 0
            if i=='_':
                counttime += 1
            elif i=='0':
                counttime += 2
    print(counttime)
