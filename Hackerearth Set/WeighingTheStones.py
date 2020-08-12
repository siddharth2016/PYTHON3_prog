# WEIGHING THE STONES

for _ in range(int(input())):
    N = int(input())
    DictR = {}
    DictA = {}
    Rupam = [int(a) for a in input().split()]
    Ankit = [int(a) for a in input().split()]
    for i in range(N):
        DictR[Rupam[i]] = Rupam.count(Rupam[i])
        DictA[Ankit[i]] = Ankit.count(Ankit[i])
    #print(DictR)
    #print(DictA)
    maxr = r = 0
    maxa = a = 0
    for key,value in DictR.items():
    	if maxr==value:
    		if key>r:
    		    r=key
    	if maxr<value:
    		maxr=value
    		r=key
    #print(r,maxr)
    for key,value in DictA.items():
    	if maxa==value:
    		if key>a:
    		    a=key
    	if maxa<value:
    		maxa=value
    		a=key
    #print(a,maxa)
    if a>r:
        print("Ankit")
    elif r>a:
        print("Rupam")
    else:
        print("Tie")
    
            
