#1. Reverse a Number Without Converting It into a String
'''num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)'''

#Check Whether a Number Is a Palindrome
'''num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")'''

#3)Check whether a number is an Armstrong number
'''num = int(input("Enter a number: "))

original = num
digits = len(str(num))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")'''

#4. Factorial of a Number Using a Loop
'''num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial:", fact)'''

#5. Generate Fibonacci Series up to N Terms
'''n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c'''

#6. Check Whether a Number Is Prime
'''num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")'''

#7. Print All Prime Numbers Between 1 and 100
'''print("Prime numbers between 1 and 100:")

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")'''

#8.Find GCD and LCM of Two Numbers
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    temp = y
    y = x % y
    x = temp

gcd = abs(x)

if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)'''

#9. Reverse a String Without Using Slicing
'''text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)'''

#10. Check Whether a String Is a Palindrome
'''text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text.lower() == reverse.lower():
    print("Palindrome String")
else:
    print("Not a Palindrome String")'''

#11. Count Vowels, Consonants, Digits and Special Characters
'''text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    elif ch.isdigit():
        digits += 1

    elif not ch.isspace():
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)'''

#12. Find Frequency of Each Character in a String
'''text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequency:")

for key, value in frequency.items():
    print(key, ":", value)'''

#13. Find the First Non-Repeating Character
'''text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")'''

#14. Remove Duplicate Characters from a String
'''text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)'''

#15. Check Whether Two Strings Are Anagrams
'''str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")'''

#16. Find the Longest Word in a Sentence
'''sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
else:
    print("No words entered")'''

#17. Find the Second-Largest Element Without Using sort()
'''numbers = list(map(int, input("Enter numbers: ").split()))

largest = float('-inf')
second = float('-inf')

for num in numbers:
    if num > largest:
        second = largest
        largest = num

    elif largest > num > second:
        second = num

if second == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Second largest:", second)'''

#18. Remove Duplicate Elements from a List Without Using set()
'''numbers = [1, 2, 3, 2, 4, 1, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("Original list:", numbers)
print("List without duplicates:", result)'''

#19. Find Common Elements Between Two Lists
'''list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)'''

#20. Move All Zeros to the End of a List
'''numbers = [0, 1, 0, 3, 12, 0, 5]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

for num in numbers:
    if num == 0:
        result.append(num)

print("Result:", result)'''

#21. Find the Missing Number in a List from 1 to N
'''n = int(input("Enter N: "))

numbers = [1, 2, 3, 5, 6]

expected_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Missing number:", missing)'''

#22. Maximum Difference Between Two Elements
'''numbers = [2, 3, 10, 6, 4, 8, 1]

min_value = numbers[0]
max_difference = float('-inf')

for num in numbers[1:]:
    difference = num - min_value

    if difference > max_difference:
        max_difference = difference

    if num < min_value:
        min_value = num

print("Maximum difference:", max_difference)'''

#23. Rotate a List to the Right by K Positions
'''numbers = [1, 2, 3, 4, 5]

k = int(input("Enter rotation positions: "))

if numbers:
    k = k % len(numbers)

    if k != 0:
        numbers = numbers[-k:] + numbers[:-k]

print("Rotated list:", numbers)'''

#24. Find All Pairs Whose Sum Equals a Target
'''numbers = [2, 4, 3, 5, 7, 8, 1]

target = int(input("Enter target sum: "))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs:", pairs)'''

#25. Count Frequency of Each Word in a Paragraph
'''paragraph = input("Enter a paragraph: ").lower()

words = paragraph.split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:")

    if word:
        frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:")

for word, count in frequency.items():
    print(word, ":", count)'''

#26. Merge Two Dictionaries and Add Common Key Values
'''dict1 = {"a": 10, "b": 20, "c": 30}

dict2 = {"b": 5, "c": 15, "d": 40}

result = dict1.copy()

for key, value in dict2.items():

    if key in result:
        result[key] += value
    else:
        result[key] = value

print("Merged Dictionary:", result)'''

#27. Sort a Dictionary Based on Its Values
'''data = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 40,
    "Orange": 30
}

sorted_data = dict(
    sorted(data.items(), key=lambda item: item[1])
)

print("Sorted Dictionary:", sorted_data)'''

#28. Find the Student with the Highest Marks
'''students = [
    {"name": "Yash", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Amit", "marks": 78},
    {"name": "Sneha", "marks": 95}
]

topper = max(students, key=lambda student: student["marks"])

print("Topper:", topper["name"])
print("Highest Marks:", topper["marks"])'''

#29. Group Words Based on Their First Character
'''words = ["apple", "ant", "banana", "ball", "cat", "car"]

groups = {}

for word in words:

    first = word[0]

    if first not in groups:
        groups[first] = []

    groups[first].append(word)

print(groups)'''

#30. Convert Two Lists into a Dictionary
'''keys = ["name", "age", "city"]

values = ["Yash", 22, "Nashik"]

result = dict(zip(keys, values))

print("Dictionary:", result)'''

#31. Calculate Factorial Using Recursion
'''def factorial(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial:", factorial(num))'''

#32. Find Sum of Digits Using Recursion
'''def sum_digits(n):

    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)


num = int(input("Enter a number: "))

print("Sum of digits:", sum_digits(abs(num)))'''

#33. Implement Your Own map() Function
'''def my_map(function, numbers):

    result = []

    for num in numbers:
        result.append(function(num))

    return result


numbers = [1, 2, 3, 4, 5]

result = my_map(lambda x: x * 2, numbers)

print("Original List:", numbers)
print("New List:", result)'''

#34. Return Only Even Numbers from a List
'''def even_numbers(numbers):

    result = []

    for num in numbers:

        if num % 2 == 0:
            result.append(num)

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("Even Numbers:", even_numbers(numbers))'''

#35. Flatten a Nested List
'''def flatten(nested_list):

    result = []

    for item in nested_list:

        if isinstance(item, list):
            result.extend(flatten(item))

        else:
            result.append(item)

    return result


numbers = [1, [2, 3], [4, [5, 6]], 7]

print("Flattened List:", flatten(numbers))'''

#36. Student Management System
'''students = {}

while True:

    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        sid = input("Enter Student ID: ")

        if sid in students:
            print("Student ID already exists")
            continue

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        students[sid] = {
            "name": name,
            "age": age,
            "course": course
        }

        print("Student Added Successfully")

    elif choice == "2":

        for sid, details in students.items():
            print(sid, details)

    elif choice == "3":

        sid = input("Enter Student ID: ")

        if sid in students:
            print(students[sid])
        else:
            print("Student Not Found")

    elif choice == "4":

        sid = input("Enter Student ID: ")

        if sid in students:
            students[sid]["name"] = input("Enter New Name: ")
            students[sid]["age"] = input("Enter New Age: ")
            students[sid]["course"] = input("Enter New Course: ")

            print("Student Updated")
        else:
            print("Student Not Found")

    elif choice == "5":

        sid = input("Enter Student ID: ")

        if sid in students:
            del students[sid]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == "0":
        break

    else:
        print("Invalid Choice")'''

#37. Bank Account Management System
'''account = {}

while True:

    print("\n--- BANK MANAGEMENT SYSTEM ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Account Details")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if account:
            print("Account already exists")
        else:
            account["name"] = input("Enter Account Holder Name: ")
            account["number"] = input("Enter Account Number: ")
            account["balance"] = 0

            print("Account Created Successfully")

    elif choice in ["2", "3", "4", "5"]:

        if not account:
            print("Please Create Account First")
            continue

        if choice == "2":

            amount = float(input("Enter Deposit Amount: "))

            if amount > 0:
                account["balance"] += amount
                print("Money Deposited Successfully")
            else:
                print("Invalid Amount")

        elif choice == "3":

            amount = float(input("Enter Withdrawal Amount: "))

            if amount <= 0:
                print("Invalid Amount")
            elif amount <= account["balance"]:
                account["balance"] -= amount
                print("Withdrawal Successful")
            else:
                print("Insufficient Balance")

        elif choice == "4":

            print("Available Balance:", account["balance"])

        elif choice == "5":

            print("Account Holder:", account["name"])
            print("Account Number:", account["number"])
            print("Balance:", account["balance"])

    elif choice == "0":
        break

    else:
        print("Invalid Choice")'''

#38. Employee Salary Management System
'''employees = {}

while True:

    print("\n--- EMPLOYEE SALARY MANAGEMENT ---")
    print("1. Add Employee")
    print("2. Calculate Salary")
    print("3. Display All Employees")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        eid = input("Enter Employee ID: ")

        if eid in employees:
            print("Employee already exists")
            continue

        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        hra = float(input("Enter HRA: "))
        allowance = float(input("Enter Allowances: "))
        deduction = float(input("Enter Deductions: "))

        employees[eid] = {
            "name": name,
            "basic": basic,
            "hra": hra,
            "allowance": allowance,
            "deduction": deduction
        }

        print("Employee Added Successfully")

    elif choice in ["2", "3"]:

        if choice == "2":
            eid = input("Enter Employee ID: ")

            if eid not in employees:
                print("Employee Not Found")
                continue

            selected = {eid: employees[eid]}

        else:
            selected = employees

        for eid, emp in selected.items():

            gross = emp["basic"] + emp["hra"] + emp["allowance"]

            net = gross - emp["deduction"]

            print("\nEmployee ID:", eid)
            print("Name:", emp["name"])
            print("Gross Salary:", gross)
            print("Deductions:", emp["deduction"])
            print("Net Salary:", net)

    elif choice == "0":
        break

    else:
        print("Invalid Choice")'''

#39. Library Management System
'''books = {}

while True:

    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Display Available Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        bid = input("Enter Book ID: ")

        if bid in books:
            print("Book ID already exists")
            continue

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books[bid] = {
            "title": title,
            "author": author,
            "issued": False
        }

        print("Book Added Successfully")

    elif choice == "2":

        for bid, book in books.items():

            if not book["issued"]:
                print(bid, book["title"], book["author"])

    elif choice == "3":

        bid = input("Enter Book ID: ")

        if bid in books:

            if not books[bid]["issued"]:
                books[bid]["issued"] = True
                print("Book Issued Successfully")
            else:
                print("Book Already Issued")

        else:
            print("Book Not Found")

    elif choice == "4":

        bid = input("Enter Book ID: ")

        if bid in books and books[bid]["issued"]:
            books[bid]["issued"] = False
            print("Book Returned Successfully")
        else:
            print("Book Not Found or Not Issued")

    elif choice == "5":

        title = input("Enter Book Title: ").lower()

        found = False

        for bid, book in books.items():

            if title in book["title"].lower():
                print(bid, book)
                found = True

        if not found:
            print("Book Not Found")

    elif choice == "0":
        break

    else:
        print("Invalid Choice")'''

#40. Task Management Application
'''tasks = {}

task_id = 1

while True:

    print("\n--- TASK MANAGEMENT SYSTEM ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Completed")
    print("6. View Completed Tasks")
    print("7. View Pending Tasks")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter Task: ")

        tasks[task_id] = {
            "task": task,
            "status": "Pending"
        }

        print("Task Added Successfully")
        print("Task ID:", task_id)

        task_id += 1

    elif choice == "2":

        for tid, details in tasks.items():
            print(tid, details)

    elif choice == "3":

        tid = int(input("Enter Task ID: "))

        if tid in tasks:

            tasks[tid]["task"] = input("Enter Updated Task: ")

            print("Task Updated Successfully")

        else:
            print("Task Not Found")

    elif choice == "4":

        tid = int(input("Enter Task ID: "))

        if tid in tasks:
            del tasks[tid]
            print("Task Deleted Successfully")
        else:
            print("Task Not Found")

    elif choice == "5":

        tid = int(input("Enter Task ID: "))

        if tid in tasks:
            tasks[tid]["status"] = "Completed"
            print("Task Marked as Completed")
        else:
            print("Task Not Found")

    elif choice == "6":

        print("\nCompleted Tasks:")

        for tid, details in tasks.items():

            if details["status"] == "Completed":
                print(tid, details["task"])

    elif choice == "7":

        print("\nPending Tasks:")

        for tid, details in tasks.items():

            if details["status"] == "Pending":
                print(tid, details["task"])

    elif choice == "0":
        break

    else:
        print("Invalid Choice")'''

