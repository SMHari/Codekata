def main():
    n=int(input())
    flag=1
    for i in  range(2,n//2):
        if n%i==0:
            flag=0
    if flag==1:
        print("yes")
    else:
        print("no")



if __name__=='__main__':
    main()
