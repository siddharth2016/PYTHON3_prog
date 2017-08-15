# INSERTION SORT AND SELECTION SORT

def insertionsort(l):

    for start in range(1,len(l),1):

        pos = start
        while pos>0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1]) = (l[pos-1],l[pos])
            pos -= 1

l = list(range(100,0,-1))
print(l)
insertionsort(l)
print(l)

def selectionsort(l):

    for start in range(0,len(l),1):

        minpos = start
        for i in range(start,len(l),1):
            if l[i]<l[minpos]:
                minpos = i
        (l[start],l[minpos]) = (l[minpos], l[start])

l = list(range(500,0,-1))
print(l)
selectionsort(l)
print(l)
