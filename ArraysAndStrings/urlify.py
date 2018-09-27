def urlify(s, someint):
    cleanstring = []
    for i in range(0, someint):
        cleanstring.append(s[i])
    for j in range(0, len(cleanstring)):
        if(cleanstring[j] == " "):
            cleanstring[j] = "%20"
    newstring = "". join(cleanstring)
    return newstring

def main():
    st = "Mr John Smith      "
    print(urlify(st, 13))




main()