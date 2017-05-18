# MANNA'S FIRST NAME

for i in range(int(input())):
    s = input().strip()
    countsuvo = s.count("SUVO")
    countsuvojit = s.count("SUVOJIT")
    countsuvo -= countsuvojit
    print("SUVO = "+str(countsuvo)+", SUVOJIT = "+str(countsuvojit))
