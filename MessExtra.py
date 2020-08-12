#BITS-ACM MESS EXTRA

def main():
    from sys import stdin, stdout
    Arr = set()
    for i in range(int(stdin.readline())):
        name = stdin.readline().lower()
        if name in Arr:
            stdout.write("Don't Give\n")
        else:
            Arr.add(name)
            stdout.write("Give\n")
if __name__ == "__main__":
    main()
