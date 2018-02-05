def main():
    count=0
    a = "kabali"
    src_str=''.join(sorted(a))
    n=int(input())
    list=[]
    for i in range(0,n):
        name=input()
        list.append(name)
    for name in list:
        if ''.join(sorted(name))==src_str:
            count=count+1
    print(count)

if __name__ == '__main__':
    main()
