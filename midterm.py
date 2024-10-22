#1 yzabdecw
s = input("Enter the string: ")

test = s[0]
best = ''
for n in range(1, len(s)):    # have s[0] so compare to s[1]
    if len(test) > len(best):
        best = test
    if s[n] >= s[n-1]:
        test = test + s[n]    # add s[1] to s[0] if greater or equal
    else:                     # if not, do one of these options
        test = s[n]

print ("Longest substring in alphabetical order is:", best)

#2 a, ab, abc
number = int(input("Enter the number: "))

for y in range(1, number + 1):
    for i in range(y):
        print(chr(ord('a') + i), end="")
    print()


#3 kubi bisekc

x = 25
epsilon = 0.01
numguesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 3 - x) >= epsilon:
    numguesses +=1
    if ans ** 3 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2.0

print (ans)


#3.1 kvadrati bisekc

x = 25
epsilon = 0.01
numguesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= epsilon:
    numguesses +=1
    if ans ** 2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2.0

print (ans)


#3.2 newton

epsilon = 0.01
y = 24.0
guess = y / 2.0
numGuesses = 0

while abs (guess * guess - y) >= epsilon:
    numGuesses +=1
    guess = guess - ((guess ** 2 - y) / (2 * guess))

print(guess)


#4

words_tuple = (
    "apple", "banana", "orange", "grape", "peach",
    "plum", "kiwi", "mango", "tomato", "coconut" )

# Check if the tuple contains exactly 10 words
if len(words_tuple) != 10:
    raise ValueError("Input must be a tuple containing exactly 10 words.")

# Create a new tuple with words containing both 'a' and 'o'
filtered_words = tuple(word for word in words_tuple if 'a' in word and 'o' in word)

# Print the result
print(f"Filtered words: {filtered_words}")

#5

import random

def generate_random_numbers():
    # Generate a list of 10 random numbers between 0 and 100
    random_numbers = [random.randint(0, 100) for _ in range(10)]
    return random_numbers

# Example usage
random_numbers = generate_random_numbers()
print(f"Random numbers: {random_numbers}")

