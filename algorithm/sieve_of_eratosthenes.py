import sys
import math

def main():
    print('start!' )
    args = sys.argv
    
    if len(args) == 1:
        print('Please specify an argument.')
        exit()

    if args[1].isdigit() == True:
        erastosthenes(int(args[1]))
    else:
        print('Please specify a numerical value for the argument.')

    print('end!')

def erastosthenes(number):
    print(number)
    
    if number == 1:
        print('prime number is nothing.')
        return

    # 平方根にして整数化する、これが検索のMAX
    squrt_limit = int(math.sqrt(number))

    # 2からが素数なので
    for i in range(2, number, 2):
        print(i + 1)
    


        


if __name__ == "__main__":
    main()