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
        binary_search(target, int(args[1]))
    else:
        print('Please specify a numerical value for the argument.')

    print('end!' )

def binary_search(taraget, n):
    left = 0
    right = len(target) -1
    

