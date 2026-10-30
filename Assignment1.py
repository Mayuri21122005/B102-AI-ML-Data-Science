#Even or Odd Function

def is_even(n):

    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter a number: " ))
result = is_even(n)
    
print("The number is", result) 


#Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(20, 10))

# Print Numbers
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)


# Sum of Numbers
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

print(sum_n(5)) 


#Multiplication Table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5) 


#Count Even Numbers
def count_even(numbers):
    count = 0

    for i in numbers:
        if i % 2 == 0:
            count = count + 1

    return count

print(count_even([1, 2, 3, 4, 6])) 


#find maximum
def find_max(numbers):
    if len(numbers) == 0:
        return "List is empty"

    maximum = numbers[0]

    for i in numbers:
        if i > maximum:
            maximum = i

    return maximum

print(find_max([10, 25, 5, 40, 15])) 



#FizzBuzz 
def fizzbuzz():
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

fizzbuzz() 


#Palindrome Checker
def palindrome(s):
    s = s.lower()

    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome("nayan"))
print(palindrome("hello")) 


#Count Vowels
def count_vowels(s):
    count = 0

    for i in s:
        if i.lower() in "aeiou":
            count = count + 1

    return count

print(count_vowels("I am mayuri bachhav, a student from LGNSCOE")) 


#Second Largest Number
def second_largest(numbers):
    unique_numbers = []

    for i in numbers:
        if i not in unique_numbers:
            unique_numbers.append(i)

    if len(unique_numbers) < 2:
        return "Second largest number does not exist"

    largest = unique_numbers[0]
    second = unique_numbers[0]

    for i in unique_numbers:
        if i > largest:
            second = largest
            largest = i

        elif i > second and i < largest:
            second = i

    return second

print(second_largest([10, 20, 5, 40, 30]))  


#Guessing Game
import random

def guessing_game():

    number = random.randint(1, 10)

    while True:

        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Congratulations! You guessed it right.")
            break

        elif guess < number:
            print("Too low! Try again.")

        else:
            print("Too high! Try again.")

guessing_game()
