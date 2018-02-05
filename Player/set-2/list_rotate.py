def main():
    list=[]
    n,k=input().split(" ")
    n=int(n)
    k=int(k)
    for i in range(0,n):
        y=int(input())
        list.append(str(y))

    final=(list[-k:]+list[:-k])
    print( ' '.join(final))
if __name__ == '__main__':
    main()
