# -------------------------------------------------------------------
# @author Anil Nayak
# @copyright (C) 2018, 
# @doc
#
# @end
# Created : 28. Apr 2018 12:31 AM
# -------------------------------------------------------------------

import math
import time

class Sample():
    def __init__(self):
        self.n = 123456
        start_time = time.time()
        self.prime_sol_1() #96643159579, 96643159579, 96643159579
        print("prime_sol_1", round((time.time() - start_time), 5))

        start_time = time.time()
        self.prime_sol_2() #96643159579, 96643159579
        print("prime_sol_2", round((time.time() - start_time), 5))

    def prime_sol_1(self):
        self.prime = [2]
        self.number = 3

        while True:
            prime_flag = True

            for i in range(2, int(math.sqrt(self.number)) + 1):
                if self.number % i == 0:
                    prime_flag = False
                    break

            if prime_flag:
                self.prime.append(self.number)
                self.number += 2
            else:
                self.number += 1

            if len(self.prime) == self.n:
                print(sum(self.prime))
                break


    def prime_sol_2(self):
        self.prime = [2]
        self.number = 3

        while True:
            prime_flag = True

            for k in self.prime[0:20]:
                if self.number % k == 0:
                    prime_flag = False
                    break

            if prime_flag:
                for i in range(2, int(math.sqrt(self.number))+1):
                    if self.number % i == 0:
                        prime_flag = False
                        break

            if prime_flag:
                self.prime.append(self.number)
                self.number += 2
            else:
                self.number += 1

            if len(self.prime) == self.n:
                print(sum(self.prime))
                break

if __name__ == '__main__':
    Sample()
