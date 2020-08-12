# HIHI AND CRAZY BITS

for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        print(n+1)
    else:
        st = [a for a in bin(n)[2:]]
        lst = len(st)
        if lst==st.count('1'):
            st += ['1']
        else:
            for i in range(len(st)-1,-1,-1):
                if st[i]=='0':
                    st[i]='1'
                    break
        print(int(''.join(st),2))
