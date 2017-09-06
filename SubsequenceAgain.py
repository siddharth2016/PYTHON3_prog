# SUBSEQUENCE AGAIN

S = input()
k = int(input())
d = {}
result = ""
for letter in S:
    #print(letter)
    try:
        if d[letter]>=k:
            result += letter
            #print("#")
    except:
        d[letter] = S.count(letter)
        if d[letter]>=k:
            result += letter
            #print("##")
print(result)

    
