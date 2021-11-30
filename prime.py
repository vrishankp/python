import time

lower = 1
upper = int(input("Enter a number: "))

total = 0

print("Prime numbers between " + str(lower) + " and " + str(upper) + " are:")

start_time = time.time()

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           total = total + 1
print("Total number of primes in the range: " + str(total))
exetime = (time.time() - start_time)
print("Time it took: " + str(exetime))
