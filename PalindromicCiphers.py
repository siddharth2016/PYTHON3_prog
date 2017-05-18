#PALINDROMIC CIPHERS

def value(s):
    i = 0
    prod = 1
    for i in range(len(s)):
        prod = prod * (ord(s[i])-96)
    return prod

test = int(input())
for i in range(test):
    string = str(input())
    stringr = string[::-1]
    if string == stringr:
        print("Palindrome")
    else:
        print(value(string))
