def isEditDistanceOne(str1, str2):
    m = len(str1)
    n = len(str2)

    if abs(m - n) > 1:
        return False

    count = 0

    i = 0
    j = 0
    while i < m and j < n:
        if str1[i] != str2[j]:
            if count == 1:
                return False

            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1


            count += 1

        else:
            i += 1
            j += 1

    if i < m or j < n:
        count += 1

    return count == 1

if __name__ == '__main__':
    str1, str2 =input().split(" ")
    if isEditDistanceOne(str1, str2):
        print("Yes")
    else:
        print("No")

