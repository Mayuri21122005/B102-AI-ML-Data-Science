# 1. Find the data type of every value in a mixed list.
#def q1():
#   values = [10, 3.5, "Python", True, None, [1, 2], (3, 4)]
#    for value in values:
#        print(value, "->", type(value).__name__)
#q1()

# 2. Convert a nested list into a tuple.
#def q2():
#   nested_list = [[3, 2], [5, 4], [5, 6]]
#   result = tuple(tuple(item) if isinstance(item, list) else item for item in nested_list)
#    print("Tuple:", result)
#q2()

# 3. Remove duplicates from a mixed list while preserving order.
def q3():
    values = [1, "a", 2, "a", 1, 3, "b", 2]
    result = []
    for item in values:
        if item not in result:
            result.append(item)
    print("Original:", values)
    print("Without duplicates:", result)
q3()

'''# 4. Check whether a number is a power of 2 using operators.
def q4():
    n = int(input("Enter a positive integer: "))
    if n > 0 and (n & (n - 1)) == 0:
        print(n, "is a power of 2")
    else:
        print(n, "is not a power of 2")

# 5. Swap two numbers using bitwise XOR.
def q5():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    a = b ^ a
    b = b ^ a
    a = b ^ a
    print("After swapping: a =", a, "b =", b)

# 6. Check divisibility by both 4 and 6 using logical operators.
def q6():
    n = int(input("Enter a number: "))
    if n % 4 == 0 and n % 6 == 0:
        print("Divisible by both 4 and 6")
    else:
        print("Not divisible by both 4 and 6")

# 7. Electricity bill. Example rates: first 100 units Rs. 1.5/unit,
# next 100 Rs. 2.5/unit, above 200 Rs. 4/unit.
def q7():
    units = float(input("Enter electricity units consumed: "))
    if units < 0:
        print("Units cannot be negative")
        return
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    print("Electricity bill = Rs.", bill)

# 8. Check whether three sides can form a triangle.
def q8():
    a, b, c = map(float, input("Enter three sides separated by spaces: ").split())
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print("The sides can form a triangle")
    else:
        print("The sides cannot form a triangle")

# 9. Determine triangle type.
def q9():
    a, b, c = map(float, input("Enter three sides separated by spaces: ").split())
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle")
    elif a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

# 10. Simple ATM menu.
def q10():
    balance = 5000.0
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Balance\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= balance:
                balance -= amount
                print("Please collect your cash. Balance:", balance)
            else:
                print("Invalid amount or insufficient balance")
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit successful. Balance:", balance)
            else:
                print("Enter a positive amount")
        elif choice == "3":
            print("Available balance:", balance)
        elif choice == "4":
            print("Thank you")
            break
        else:
            print("Invalid choice")

# 11. Income tax using example slabs (annual income):
# Up to Rs. 2,50,000: 0%; next Rs. 2,50,000: 5%;
# next Rs. 5,00,000: 20%; above Rs. 10,00,000: 30%.
# These are practice slabs, not a statement of current tax law.
def q11():
    income = float(input("Enter annual income in Rs.: "))
    if income < 0:
        print("Income cannot be negative")
        return
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 250000 * 0.05 + (income - 500000) * 0.20
    else:
        tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30
    print("Calculated tax = Rs.", tax)

# 12. Menu-driven calculator using if-elif.
def q12():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("1.Add  2.Subtract  3.Multiply  4.Divide")
    choice = input("Choose operation: ")
    if choice == "1":
        print("Result =", a + b)
    elif choice == "2":
        print("Result =", a - b)
    elif choice == "3":
        print("Result =", a * b)
    elif choice == "4":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

# 13. Print all prime numbers between 1 and n.
def q13():
    n = int(input("Enter n: "))
    for number in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            print(number, end=" ")
    print()

# 14. Factorial using a loop.
def q14():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial =", factorial)

# 15. Fibonacci series up to n terms.
def q15():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    for _ in range(max(0, n)):
        print(a, end=" ")
        a, b = b, a + b
    print()

# 16. Check Armstrong number.
def q16():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Enter a non-negative number")
        return
    digits = str(n)
    total = sum(int(digit) ** len(digits) for digit in digits)
    print("Armstrong number" if total == n else "Not an Armstrong number")

# 17. Reverse a number and check palindrome.
def q17():
    n = int(input("Enter an integer: "))
    text = str(n)
    reversed_text = text[::-1]
    print("Reversed number =", int(reversed_text))
    print("Palindrome" if text == reversed_text else "Not a palindrome")

# 18. GCD of two numbers using Euclid's algorithm.
def q18():
    a = abs(int(input("Enter first number: ")))
    b = abs(int(input("Enter second number: ")))
    while b != 0:
        a, b = b, a % b
    print("GCD =", a)

# 19. Function to check whether a string is a palindrome.
def q19():
    text = input("Enter a string: ")
    cleaned = text.replace(" ", "").lower()
    print("Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome")

# 20. Count vowels and consonants.
def q20():
    text = input("Enter a string: ")
    vowels = consonants = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    print("Vowels =", vowels)
    print("Consonants =", consonants)

# 21. Calculate simple and compound interest.
def q21():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual rate (%): "))
    time = float(input("Enter time in years: "))
    simple_interest = principal * rate * time / 100
    compound_amount = principal * (1 + rate / 100) ** time
    compound_interest = compound_amount - principal
    print("Simple interest =", simple_interest)
    print("Compound interest =", compound_interest)

# 22. Return all factors of a number.
def q22():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Enter a positive integer")
        return
    factors = [i for i in range(1, n + 1) if n % i == 0]
    print("Factors:", factors)

# 23. Find second-largest number in a list (distinct values).
def q23():
    values = list(map(int,input("enter numbers:").split()))
    unique_values = sorted(set(values))
    if len(unique_values) < 2:
        print("A second-largest distinct number does not exist")
    else:
        print("Second-largest =", unique_values[-2])

# 24. Merge two lists without duplicates, preserving order.
def q24():
    first = input("Enter first list items separated by spaces: ").split()
    second = input("Enter second list items separated by spaces: ").split()
    merged = []
    for item in first + second:
        if item not in merged:
            merged.append(item)
    print("Merged list:", merged)

# 25. Find second-largest and second-smallest distinct elements.
def q25():
    values = list(map(int,input("enter numbers:").split()))
    unique_values = sorted(set(values))
    if len(unique_values) < 2:
        print("Need at least two distinct values")
    else:
        print("Second-smallest =", unique_values[1])
        print("Second-largest =", unique_values[-2])

# 26. Rotate a list to the left by k positions.
def q26():
    values = input("Enter list items separated by spaces: ").split()
    k = int(input("Enter k: "))
    if values:
        k %= len(values)
        values = values[k:] + values[:k]
    print("Rotated list:", values)

# 27. Separate even and odd numbers.
def q27():
    values = list(map(int,input("enter numbers:").split()))
    even = [x for x in values if x % 2 == 0]
    odd = [x for x in values if x % 2 != 0]
    print("Even numbers:", even)
    print("Odd numbers:", odd)

# 28. Find common elements between two lists, without duplicates.
def q28():
    first = input("Enter first list items separated by spaces: ").split()
    second = input("Enter second list items separated by spaces: ").split()
    common = []
    for item in first:
        if item in second and item not in common:
            common.append(item)
    print("Common elements:", common)

# 29. Count frequency of each element in a tuple.
def q29():
    values = tuple(input("Enter tuple items separated by spaces: ").split())
    frequency = {}
    for item in values:
        frequency[item] = frequency.get(item, 0) + 1
    print("Tuple:", values)
    print("Frequency:", frequency)

# 30. Union, intersection and difference of two sets.
def q30():
    a = set(input("Enter set A items separated by spaces: ").split())
    b = set(input("Enter set B items separated by spaces: ").split())
    print("Union:", a | b)
    print("Intersection:", a & b)
    print("A - B:", a - b)
    print("B - A:", b - a)

# 31. Check whether one set is a subset of another.
def q31():
    a = set(input("Enter first set items separated by spaces: ").split())
    b = set(input("Enter second set items separated by spaces: ").split())
    print("First set is a subset of second:", a.issubset(b))

# 32. Count frequency of words in a sentence.
def q32():
    sentence = input("Enter a sentence: ").lower()
    frequency = {}
    for word in sentence.split():
        word = word.strip(".,!?;:")
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    print("Word frequency:", frequency)

# 33. Create dictionary from two lists (keys and values).
def q33():
    keys = input("Enter keys separated by spaces: ").split()
    values = input("Enter values separated by spaces: ").split()
    if len(keys) != len(values):
        print("Both lists must have the same length")
    else:
        print("Dictionary:", dict(zip(keys, values)))

# 34. Sort a dictionary by its values.
def q34():
    data = {"A": 40, "B": 10, "C": 30, "D": 20}
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
    print("Original dictionary:", data)
    print("Sorted by values:", sorted_data)

# 35. Count lines, words and characters in a text file.
def q35():
    filename = input("Enter file name (e.g. singham.txt): ")
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print("Lines =", len(content.splitlines()))
    print("Words =", len(content.split()))
    print("Characters =", len(content))

# 36. Copy only even-numbered lines from one file to another.
def q36():
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")
    with open(source, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
    with open(destination, "w", encoding="utf-8") as outfile:
        for line_number, line in enumerate(lines, start=1):
            if line_number % 2 == 0:
                outfile.write(line)
    print("Even-numbered lines copied to", destination)

# 37. Handle invalid integer input using try-except.
def q37():
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
    except ValueError:
        print("Invalid input! Please enter a whole number.")

# 38. Handle file-not-found error while reading a file.
def q38():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: The file was not found.")

# 39. Random password generator using random and string modules.
def q39():
    import random
    import string
    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
        print("Please enter a length of at least 4")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password_chars += [random.choice(characters) for _ in range(length - 4)]
    random.shuffle(password_chars)
    print("Generated password:", "".join(password_chars))

# 40. Calculate number of days between two dates using datetime.
def q40():
    from datetime import datetime
    date1 = input("Enter first date (DD-MM-YYYY): ")
    date2 = input("Enter second date (DD-MM-YYYY): ")
    try:
        d1 = datetime.strptime(date1, "%d-%m-%Y").date()
        d2 = datetime.strptime(date2, "%d-%m-%Y").date()
        print("Number of days =", abs((d2 - d1).days))
    except ValueError:
        print("Invalid date. Please use DD-MM-YYYY.")
'''

