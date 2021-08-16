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
    print('check number: ' + str(number))
    
    if number == 1:
        print('prime number is nothing.')
        return

    # 平方根にして整数化する、これが検索のMAX
    max_limit = int(math.sqrt(number))
    #print('Max: ' + str(max_limit))

    # 3以上の奇数のリストを作る(2より大きい偶数は素数でないので無視)
    odd_numbers = [i for i in range(3, number, 2)]
    #print('odd_numbers: ' + str(odd_numbers))
    
    # max_limitまでの奇数のリスト
    max_limit_odd_numbers = [i for i in range(3, max_limit, 2)]
    #print('max_limit_odd_numbers: ' + str(max_limit_odd_numbers))
    
    # max_limitから素数だけにする
    max_limit_prime_numbers = make_prime_list(max_limit_odd_numbers, max_limit_odd_numbers)
    #print('max_limit_prime_numbers: ' + str(max_limit_prime_numbers))
    
    # 返却用のリスト(2は素数なので入れておく)
    ret_prime_list = [2] + make_prime_list(odd_numbers, max_limit_prime_numbers)
    #print(ret_prime_list)
    print('prime number quantity is :' + str(len(ret_prime_list)))

def make_prime_list(num_list1, num_list2):
    prime_list = []
    for num1 in num_list1:
        add_flag = True
        for num2 in num_list2:
            
            if num1 <= num2:
                add_flag = True
                break

            if num1 % num2 == 0:
                add_flag = False
                break
            
        if add_flag == True:
            prime_list.append(num1)

    return prime_list

if __name__ == "__main__":
    main()
