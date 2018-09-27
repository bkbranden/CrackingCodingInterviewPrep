def isRotation(s1, s2):
    t = len(s1)
    if( t == len(s2) and t > 0):
        s1s1 = s1 + s1
        return isSubstring(s1s1, s2)
    return False



def isSubstring(str1, str2):
    x = len(str2)
    count = 1
    for i in range(0,len(str1)):
        if (str1[i] == str2[0]):
            l = i
            k = 0
            while(count < x):
                l += 1
                k += 1
                count += 1
                if(str1[l] == str2[k] and count == x):
                    return True
    return False
                     





def main():
    s = "waterbottle"
    d = "erbottlewat"
    print(isRotation(d,s))




main()