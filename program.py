def func(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1 - i):  # Fixing the inner loop range
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1

list1 = [5, 3, 6, 1, 7]
func(list1)
print(list1)  # If you want to print the sorted list
#-------------------------------------
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Take user input
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
