def isOne(s1, s2):
    count = 0
    len1 = len(s1)
    len2 = len(s2)
    table = {}
    for i in s1:
        table[i] = 1
    for i in s2:
        if (i in table):
             table[i] += 1
        else:
            table[i] = 1
    for k, v in table.items():
        if(v %2 == 1):
            count += 1
    if (len1 == len2):
        if(count >2):
            return False
    else:
        if(count >1):
            return False
    
    return True
    


def main():
    s1 = "bake"
    s2 = "pleas"
    print(isOne(s1, s2))



main()