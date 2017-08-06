# EASY MULTIPLE

for _ in range(int(input())):
    n = int(input())-1
    if n<3:
        print('0')
        continue
    elif n<5:
        print('3')
        continue
    t3 = n//3
    t5 = n//5
    t15 = n//15
    t3l = t3*3
    t5l = t5*5
    t15l = t15*15
    res3 = (t3*(3+t3l))//2
    res5 = (t5*(5+t5l))//2
    res15 = (t15*(15+t15l))//2
    fres = int(res3+res5-res15)
    print(fres)
