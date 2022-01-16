import sys
import math

target = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def main():
    print('start!' )

    args = sys.argv
    
    if len(args) == 1:
        print('Please specify an argument.')
        exit()

    if args[1].isdigit() == True:
        print(binary_search(target, int(args[1])))
    else:
        print('Please specify a numerical value for the argument.')
    print('end!' )

def binary_search(taraget, n):
    left = 0
    right = len(target) - 1

    while left <= right:
        print('left: {0}'.format(left))
        print('right: {0}'.format(right))
    
        mid = (left + right) // 2
        print('mid: {0}'.format(mid))

        if(target[mid] == n):
            return mid
        elif target[mid] < n:
            left = mid + 1
        else:
            right = mid -1
    return -1

if __name__ == "__main__":
    main()
