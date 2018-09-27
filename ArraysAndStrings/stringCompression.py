def compress(s):
    result = ""
    trackingLetter = s[0]
    count = 0
    for i in range(0, len(s)):
        if(s[i] == trackingLetter):
            if(i == len(s)-1):
                result += trackingLetter + str(count + 1)
            count += 1
        else:
            result += trackingLetter + str(count)
            trackingLetter = s[i]
            count = 1
    return result





def main():
    s = "aabcccccaaa"
    print(compress(s))




main()