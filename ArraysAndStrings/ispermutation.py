def isPermutation(s):
    table = {}
    temp = s.strip()
    newstring = temp.replace(" ", "")
    for i in newstring:
        x = ord(i)
        table[x] = 0
    for i in newstring:
        x = ord(i)
        if(x >= 97 or x <= 122):
            table[x] += 1
    foundOdd = False
    for j, k in table.items():
        if(k %2 == 1):
            if(foundOdd):
                return False
            foundOdd = True
    return True

def main():
    st = "tact coa"
    print(isPermutation(st))


main()
    