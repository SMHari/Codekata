MAX_CHARS = 256
def areIso(str1, str2):
    a = len(str1)
    b = len(str2)
    if a != b:
        return False
    marked = [False] * MAX_CHARS
    map = [-1] * MAX_CHARS
    for i in range(b):
        if map[ord(str1[i])] == -1:
            if marked[ord(str2[i])] == True:
                return False
            marked[ord(str2[i])] = True
            map[ord(str1[i])] = str2[i]
        elif map[ord(str1[i])] != str2[i]:
            return False
    return True
if __name__ == '__main__':
    str1,str2=input().split(" ")
    if areIso(str1,str2):
        print("yes")
    else:
        print("no")
