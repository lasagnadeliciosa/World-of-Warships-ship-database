import time
import math

def is_prime(n):
    # if is prime return True, else return false
    for i in range(2, math.floor(math.log(n, 2))):
        if n % i == 0:  # i is a divisor
            return False  # n is not a prime number
    return True

start_time = time.time()
max_num = 82149898964599889796854356789087654356789008  # 27843648
print(math.log(max_num, 2))
for num in range(max_num, 2, -1):
    if is_prime(num):
        print("largest prime under %s is: " % max_num, num)
        break

print("this took %s seconds" % (time.time() - start_time))
