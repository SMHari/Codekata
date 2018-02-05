def main():
    str=input()
    str1="".join([str[y:y+2][::-1] for y in range(0,len(str),2)])
    print(str1)

if __name__ == '__main__':
    main()
