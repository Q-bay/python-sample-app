import sys
import math
import time

def main():
    print('start!' )
    start = time.time()
    args = sys.argv
    
    if len(args) == 1:
        print('Please specify an argument.')
        exit()

    if args[1].isdigit() == True:
        erastosthenes(int(args[1]))
    else:
        print('Please specify a numerical value for the argument.')

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
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
    print('odd_numbers: ' + str(odd_numbers))
    
    # max_limitまでの奇数のリスト
    max_limit_odd_numbers = [i + 1 for i in range(2, max_limit, 2)]
    print('max_limit_odd_numbers: ' + str(max_limit_odd_numbers))
    
    # max_limitから素数だけにする
    max_limit_prime_numbers = []
    for max_limit_odd_num1 in max_limit_odd_numbers:
        add_flag = True
        for max_limit_odd_num2 in max_limit_odd_numbers:  

            if max_limit_odd_num1 <= max_limit_odd_num2:
                add_flag = True
                break

            if max_limit_odd_num1 % max_limit_odd_num2 == 0:
                add_flag = False
                break

        if add_flag == True:
                max_limit_prime_numbers.append(max_limit_odd_num1)

    print('max_limit_prime_numbers: ' + str(max_limit_prime_numbers))
    
    # 返却用のリスト(2は素数なので入れておく)
    prime_list = [2]

    for odd_num in odd_numbers:
        add_flag = True
        for max_limit_prime in max_limit_prime_numbers:
            
            if odd_num <= max_limit_prime:
                add_flag = True
                break

            if odd_num % max_limit_prime == 0:
                add_flag = False
                break

        if add_flag == True:
            prime_list.append(odd_num)
        

    print(prime_list)
    print(len(prime_list))

if __name__ == "__main__":
    main()
