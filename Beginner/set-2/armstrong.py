def main():
    n=int(input())
    org=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+(digit**3)
        n//=10
    if org==sum:
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
