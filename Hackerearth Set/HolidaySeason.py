# HOLIDAY SEASON        

n = int(input())
S = str(input())
newElement = {}
presentElement = {}
count = 0
if n<4:
    print('0')
else:
    for i in range(n):
        if S[i] in newElement:
            if S[i] in presentElement:
                count += presentElement[S[i]]
            cost = 1
            for j in S[newElement[S[i]]+1:i]:
                if j in presentElement:
                    presentElement[j] += cost
                else:
                    presentElement[j] = cost

                if j==S[i]:
                    cost += 1
        else:
            newElement[S[i]] = i
    print(count)
