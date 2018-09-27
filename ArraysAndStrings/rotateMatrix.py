import math

def rotate(lis):
    # newList = [len(lis)[0][len(lis)[0]]
    for layer in range(0, math.floor(len(lis)/2)):
        first = layer
        last = len(lis) -1 - layer
        for i in range(first, last):
            offset = i - first
            top = lis[first][i]
            lis[first][i] = lis[last-offset][first]
            lis[last-offset][first] = lis[last][last-offset]
            lis[last][last-offset] = lis[i][last]
            lis[i][last] = top
    
    return lis



def main():
    s = [[1,2,3],[4,5,6],[7,8,9]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in s]))
    print("______________________________")
    r = rotate(s)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in r]))
    


main()