def checkPermutation(s1, s2):
    if (len(s1) != len(s2)):
        return False
    valS1 = 0
    valS2 = 0
    for i in range(0, len(s1)):
        valS1 += ord(s1[i])
    for j in range(0, len(s2)):
        valS2 += ord(s2[j])
    if(valS1 == valS2):
        return True
    else:
        return False


def main():
    s1 = "wert                     "
    s2 = "twer"
    print(checkPermutation(s1, s2))

main()