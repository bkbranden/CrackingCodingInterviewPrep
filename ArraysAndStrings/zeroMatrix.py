def turnZero(s):
    newList = [[-1 for x in range(len(s[0]))] for y in range(len(s))]
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if(s[i][j] == 0):
                k = i
                l = 0                
                while(l < len(s[0])):
                    newList[k][l] = 0
                    l += 1
                k = 0
                l = j
                while(k < len(s)):
                    newList[k][l] = 0
                    k += 1
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if(newList[i][j] != 0):
                newList[i][j] = s[i][j]
    return newList


                


def main():
    s = [[1,23, 3],[7,8,9],[0, 230, 0]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in s]))
    print("______________________________")
    r = turnZero(s)
    # print(r)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in r]))





main()