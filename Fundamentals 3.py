# GISC 605 Lab: Fundamentals 3

for i in range(13, 1000, 13):
    print(i)


numbers = [2, 8, 64, 16, 32, 4, 16, 8]
singleNumbers = set(numbers)

if len(singleNumbers) != len(numbers):
    print("This list provided contains duplicate values.")
else:
    print("This list provided does not contain duplicate values.")


numbers = list(singleNumbers)




