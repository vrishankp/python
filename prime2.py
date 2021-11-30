import time

num = int(input("Enter a number: "))

total = 0

start_time = time.time()
for n in range(2, 1000000):
    if n > 1:
       for i in range(2, n):
           if (n % i) == 0:
               break
       else:
           print(n)
           total = total + 1
    if (total == num):
        break
exetime = (time.time() - start_time)
print("Total time taken: " + str(exetime))
