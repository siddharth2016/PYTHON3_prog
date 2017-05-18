# MAGICAL WORD - HACKER EARTH

ans_str = ""
test = int(input()) #Input the test cases

def prime(n):
    a=0
    for i in range(2,n//2,1):
        if n%i==0:
            a=2
            break
        else:
            a=1
    return a

def rprime(n):
    a=0
    while True:
       n+=1
       a = prime(n)
       if a==1:
           b = n
           break
    return b

def lprime(n):
    a=0
    while True:
        n-=1
        a = prime(n)
        if a==1:
            b = n
            break
    return b


for j in range(0,test,1):
    ans_str = ""
    word_len = int(input()) #input the length of the word
    word = str(input()) #Taking the input word

    for i in range(0,word_len,1):   
        ch = word[i]   
        asch = ord(ch)   #Finding ASCII value
        a = prime(asch)

        if '!'<=ch<='@':
            ans_str += 'C'
        elif '^'<=ch<='`':
            ans_str += 'a'
        elif '['<=ch<=']':
            ans_str += 'Y'
        elif '{'<=ch<='~':
            ans_str += 'q'
        elif a==1:
            ans_str += ch   #Making the result string
        else:
            rp = rprime(asch)  #Finding the right prime of the given ASCII
            lp = lprime(asch)  #Finding the left prime of the given ASCII
            rd = abs(asch - rp) #finding right distance
            ld = abs(asch - lp) #finding left distance
            if rd<ld and ('a'<=chr(rp)<='z' or 'A'<=chr(rp)<='Z'):
                ans_str += chr(rp)
            elif ld<rd and ('a'<=chr(lp)<='z' or 'A'<=chr(lp)<='Z'):
                ans_str += chr(lp)
            elif ('a'<=chr(lp)<='z' or 'A'<=chr(lp)<='Z'):
                ans_str += chr(lp)
            elif ('a'<=chr(rp)<='z' or 'A'<=chr(rp)<='Z'):
                ans_str += chr(rp)

    print(ans_str)
