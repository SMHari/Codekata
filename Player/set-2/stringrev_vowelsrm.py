def main():
    str=input()
    list=[]
    vowels=['a','e','i','o','u']
    for i in str:
        if i in vowels:
            y=i.replace(i,'')
            list.append(y)
        else:
            list.append(i)

    final=''.join(list)
    print(final[::-1])
if __name__ == '__main__':
    main()
