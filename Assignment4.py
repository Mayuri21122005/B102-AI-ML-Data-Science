#1) Check whether a number is even or odd
#num = int(input("Enter a number:"))
#if num % 2 == 0:
#    print("Even number")
#else:
#    print("Odd number")

# 2) Find the largest of three numbers
#a = int(input("Enter first number:"))
#b = int(input("Enter second number"))
#c = int(input("Enter third number:"))
#if a >= b and a >= c:
#    print("Largest number:",a)
#elif b >= a and b >= c:
#   print("Largest number:",b)
#else:
#    print("Largest number:",c)

# 3) Check whether a number is prime
#num = int(input("Enter a number:"))
#if num <=  1:
#   print("Not a prime Number")
#else:
#    for i in range(2,num):
#       if num % i ==0:
#           print("Not a prime number")
#            break
#   else:
#        print("Prime number")

#4) print the fibonacci series up to n terms
#n = int(input("Enter number of terms:"))

#a = 0
#b = 1
#for i in range(n):
#    print(a, end=" ")
#   c = a+b
#   a = b
#   b = c

#5) find the factorial of a number using a loop
#num = int(input("Enter a number:"))
#fact = 1 
#for i in range(1, num+1):
#    fact = fact*i
#print("Factorial =", fact)

#6) Reverse a string without using slicing
#text = input("Enter a string:")
#reverse = ""
#for ch in text:
#    reverse = ch + reverse
#print("Reversed string:", reverse)

# 7) check whether a string is a palindrome
#text = input("Enter a string:")
#reverse = ""
#for ch in text:
#   reverse = ch + reverse
#if text == reverse:
#   print("Palindrome")
#else:
#   print("Not a palindrome")

# 8) Count the number of vowels and consonants in a string
#text = input("Enter a string:")
#vowels = 0
#consonants = 0 
#for ch in text.lower():
#    if ch in "aeiou":
#        vowels += 1
#    elif ch.isalpha():
#        consonants += 1 
#print("Vowels:",vowels)
#print("Consonants:", consonants)

#9) find the sum of all elements in a list
#numbers = [10,20,30,40,50]
#total =0 
#for num in numbers:
#    total += num
#print("Sum =", total)

#10)Find the largest and smallest element without using max() or min()
#numbers = [10, 25, 5, 40, 15]

#largest = numbers[0]
#smallest = numbers[0]

#for num in numbers:
 #   if num > largest:
 #       largest = num

 #   if num < smallest:
 #       smallest = num

#print("Largest:", largest)
#print("Smallest:", smallest)

# 11)Remove duplicate elements from a list
#numbers = [10, 20, 10, 30, 20, 40, 50]

#new_list = []

#for num in numbers:
#    if num not in new_list:
#       new_list.append(num)

#print("List after removing duplicates:", new_list)

# 12) Count how many times each element appears using a dictionary
#numbers = [10, 20, 10, 30, 20, 10, 40]

#frequency = {}

#for num in numbers:
#   if num in frequency:
#        frequency[num] += 1
#    else:
#        frequency[num] = 1

#print("Frequency:", frequency)


# 13) Find the second-largest number in a list
#numbers = [10, 25, 40, 15, 30]

#largest = numbers[0]
#second_largest = None

#for num in numbers:
#   if num > largest:
#       second_largest = largest
#       largest = num
#   elif num != largest:
#      if second_largest is None or num > second_largest:
 #           second_largest = num

#print("Second largest:", second_largest)

# 14) Sort a list without using sort() or sorted()
#numbers = [50, 20, 40, 10, 30]

#for i in range(len(numbers)):
#for j in range(i + 1, len(numbers)):
#       if numbers[i] > numbers[j]:
#           temp = numbers[i]
 #           numbers[i] = numbers[j]
 #           numbers[j] = temp

#print("Sorted list:", numbers)

# 15)Function that returns only even numbers from a list 
#def even_numbers(numbers):
#   result = []

#   for num in numbers:
#       if num % 2 == 0:
#            result.append(num)

#   return result


#numbers = [10, 15, 20, 25, 30, 35, 40]

#print("Even numbers:", even_numbers(numbers))


# 16) Find the frequency of each character in a string 
'''text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:", frequency)'''

# 17) Check whether two strings are anagrams
'''str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.lower()
str2 = str2.lower()

if len(str1) != len(str2):
    print("Not anagrams")
else:
    if sorted(str1) == sorted(str2):
        print("Anagrams")
    else:
        print("Not anagrams")'''


#18) Find duplicate values in a list
'''numbers = [10, 20, 30, 10, 40, 20, 50, 30]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1:
        if num not in duplicates:
            duplicates.append(num)

print("Duplicate values:", duplicates)'''

# 19)  Find the longest word in a sentence
'''sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length:", len(longest))'''

# 20) Simple Students marks program
marks = []

for i in range(1, 6):
    mark = int(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = 0

for mark in marks:
    total = total + mark

percentage = total / 5

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")

if any(mark < 35 for mark in marks):
    print("Result: Fail")
    print("Grade: F")
else:
    print("Result: Pass")

    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 50:
        print("Grade: D")
    else:
        print("Grade: E")