#ACRONYM HE
k = int(input())
dislikeWords =[]
for i in range(k):
    dislikeWords = dislikeWords + [str(input())]
#print(dislikeWords)
n = int(input())
sentence = str(input())
sentence = sentence.split()
for i in range(k):
    if sentence.count(dislikeWords[i])>=1:
        sentence.remove(dislikeWords[i])
#print(sentence)
acr = ""
for i in range(len(sentence)-1):
    #print(sentence[i][0].upper())
    acr = acr + sentence[i][0].upper() + '.'
    #print(acr)
acr = acr + sentence[len(sentence)-1][0].upper()
print(acr)
