number = int(input("Enter a number: "))
count = 0

while number > 1:
    if number % 2 == 1:
        number = number * 3 + 1
        count = count + 1
    elif number % 2 != 1:
        number = number / 2
        count = count + 1
    print(number)

print("The total stopping time is " + str(count))
