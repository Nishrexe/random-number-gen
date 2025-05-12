import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 200)

print("Your random number is:", random_number)

# Check if the number is even or odd
if random_number % 2 == 0:
    print("Even")
else:
    print("Odd")


