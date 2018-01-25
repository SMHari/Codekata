def main():
    n,no=input().split(" ")
    arr=[]
    n=int(n)
    no=int(no)
    for i in range(0,n):
        y=int(input())
        arr.append(y)
    a=0
    for i in range(0,no):
        a+=arr[i]

    print(a)



if __name__=='__main__':
    main()
