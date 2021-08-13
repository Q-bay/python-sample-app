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
    max_limit = int(math.sqrt(number))
    print('Max: ' + str(max_limit))

    # 3以上の奇数のリストを作る(2より大きい偶数は素数でないので無視)
    odd_numbers = [i + 1 for i in range(2, number, 2)]
    print(odd_numbers)
    
    # max_limitまでの奇数のリスト
    max_limit_odd_numbers = [i + 1 for i in range(2, max_limit, 2)]
    print(max_limit_odd_numbers)
    
    # 返却用のリスト(2は素数なので入れておく)
    prime_list = [2]

    # 限界の数値を倍数していく、numbersに存在したら削除する
    for odd_num in max_limit_odd_numbers:
        
        for multiple_num in range (2, number // max_limit_odd_numbers[0]):
            del_num = odd_num * multiple_num
            if del_num in odd_numbers:
                odd_numbers.remove(del_num)
            
    prime_list = prime_list + odd_numbers

    print(prime_list)
    print(len(prime_list))

if __name__ == "__main__":
    main()