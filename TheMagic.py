# THE MAGIC

def countDays(n):
    count = 0
    while(n):
        n = n&(n-1)
        count += 1
    return count

test = int(input())
for i in range(test):
    n = int(input())
    print(countDays(n))
