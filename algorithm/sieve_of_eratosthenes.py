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
        eratosthenes(int(args[1]))
    else:
        print('Please specify a numerical value for the argument.')

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print('end!')

def eratosthenes(n):
    print("check number: {0}".format(n))
    primes = list(range(0, n + 1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i] > 0:
            for j in range(2 * i, n + 1, i):
                primes[j] = 0
    print("prime number quantity is :{0}".format(sum(x > 0 for x in primes[2:])))

if __name__ == "__main__":
    main()
