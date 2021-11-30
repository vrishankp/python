
num = input("Enter a number: ")

n1 = 1
n2 = 1
print(n2/n1)
if num > 2:
    for i in range(1, num - 1):
        n3 = n1 + n2
        ratio = float(n3)/float(n2)
        print(ratio)
        n1 = n2
        n2 = n3
