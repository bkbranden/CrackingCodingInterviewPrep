def isUnique(s):
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                return False

    return True


def main():
    s = "wwwwwwwwwwww"
    print(isUnique(s))


main()


#Can optimize by using a bit vector and mapping that so that the space used is a lot less