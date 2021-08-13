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

    # 2からが素数なので2と3以上の奇数のリストを作る(2より大きい偶数は素数でないので無視)、
    # このリストから割れる数字を除いたものが素数
    list = [2]
    list += [i + 1 for i in range(2, number, 2)]

    for i in list:
        print(i)
        
    


        


if __name__ == "__main__":
    main()