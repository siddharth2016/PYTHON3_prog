''' Simple Calculator '''

while True:
    print("Welcome to Your Personal Calculator")
    print("Enter 'ADD' for addition")
    print("Enter 'SUB' for subtraction")
    print("Enter 'MUL' for multiplication")
    print("Enter 'DIV' for division")
    print("Enter 'QUIT' to quit Program")
    a = input(" : ")

    if a=="ADD" or a=="add":
        n1 = float(input("Enter Number 1: "))
        n2 = float(input("Enter Number 2: "))
        res = str(n1+n2)
        print("Your Response Result is : "+res)
    elif a=="SUB" or a=="sub":
        n1 = float(input("Enter Number 1: "))
        n2 = float(input("Enter Number 2: "))
        res = str(n1 - n2)
        print("Your Response Result is : "+res)
    elif a=="MUL" or a=="mul":
        n1 = float(input("Enter Number 1: "))
        n2 = float(input("Enter Number 2: "))
        res = str(n1*n2)
        print("Your Response Result is : "+res)
    elif a=="DIV" or a=="div":
        n1 = float(input("Enter Number 1: "))
        n2 = float(input("Enter Number 2: "))
        res = str(n1/n2)
        print("Your Response Result is : "+res)
    elif a=="QUIT" or a=="quit":
        break
