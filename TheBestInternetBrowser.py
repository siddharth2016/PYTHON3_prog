# THE BEST INTERNET BROWSER

for _ in range(int(input())):
    st = str(input())
    countvowel = st.count('a') + st.count('e') + st.count('i') + st.count('o') + st.count('u') - 1
    totallen = len(st)
    urllen = totallen - 4 - countvowel
    res = str(urllen)+"/"+str(totallen)
    print(res)
