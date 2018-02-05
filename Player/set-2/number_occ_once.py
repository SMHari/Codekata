def main():
    n=int(input())
    list=[]
    for i in range(0,n):
        y=int(input())
        list.append(y)
    print(list)
    num=list[0]
    for i in range(1,len(list)):
        num=num ^ list[i]
    print(num)
if __name__ == '__main__':
    main()
