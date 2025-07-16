# Ask for the user's name
name = input("What is your name? ")

# Greet the user
print(f"Hello, {name}! Let's do a simple counting game.")

# Ask the user for a number
number = int(input("Enter a number to count up to: "))

# Count from 1 to the number
for i in range(1, number + 1):
    print(i)

# Final message based on the number entered
if number < 5:
    print("That was a short count!")
else:
    print("Nice counting!")
