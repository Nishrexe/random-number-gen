import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 200)

print("Your random number is:", random_number)

# Check if the number is even or odd
if random_number % 2 == 0:
    print("Even")
else:
    print("Odd")

# checking if the number is larger than 100
if random_number > 100 :
    print ("number is bigger than 100")
else:
    print ("number is smaller than 100")
