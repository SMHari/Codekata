def main():
    #n=(input("Enter int or character to determine its type:"))
    n=input()
    if n.isalpha():
        print("Alphabet")
    elif n.isdigit():
        print("No")
    else:
        print("No")
if __name__=='__main__':
    main()
