import collections


def main():
    string=input()
    max_str=collections.Counter(string).most_common(1)[0][0]
    print(max_str)
if __name__ == '__main__':
    main()
