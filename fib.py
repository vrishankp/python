import time
num = input("Enter a number: ")

n1 = 1
n2 = 1

start_time = time.time()
print(n1)
print(n2)
if num > 2:
    for i in range(1, num - 2):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3
exetime = (time.time() - start_time)
print("Time it took: " + str(exetime))
