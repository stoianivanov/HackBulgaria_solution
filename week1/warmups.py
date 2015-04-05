def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def fibonacciHelper(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacciHelper(n-1) + fibonacciHelper(n-2)


def fibonacci(n):
    lst = []
    for i in range(1, n+1):
        lst.append(fibonacciHelper(i))
    return lst


def sum_of_digits(n):
    number = 0
    if n < 10 and n > -10:
        return abs(n)
    else:
        number = abs(n) % 10
        return number + sum_of_digits(abs(n//10))


def fact_digits(n):
    if n < 10:
        return factorial(n)
    else:
        return factorial(n % 10) + fact_digits(n//10)


def palindrome(obj):
    obj = str(obj)
    string = obj[::-1]
    return obj == ''.join(string)


def to_digits(n):
    digits_list = []
    while n > 0:
        digits_list.append(n % 10)
        n = n // 10

    return digits_list[::-1]


def to_number(digits):
    number = 0
    for i in digits:
        number = number*10 + i
    return number


def fib_number(n):
    fib_list = fibonacci(n)
    number = ""
    for num in fib_list:
        number = number + str(num)
    return int(number)


def is_a_vowels(ch):
    vowels = "aeiouyAEIOUY"
    for i in vowels:
        if ch == i:
            return True
    return False


def count_vowels(str1):
    counter = 0
    for i in range(0, len(str1)):
        if is_a_vowels(str1[i]):
            counter = counter + 1
    return counter


def is_a_consonants(ch):
    consonants = "bcdfghjklmnpqrstvwxz"
    consonants = consonants + consonants.upper()
    for i in consonants:
        if ch == i:
            return True
    return False


def count_consonants(str1):
    counter = 0
    for i in range(0, len(str1)):
        if is_a_consonants(str1[i]):
            counter = counter + 1
    return counter


def added_in_dict(ch, histogram):
    for key in histogram:
        if key == ch:
            return True
    return False


def char_histogram(string):
    histogram = {}

    for i in string:
        if added_in_dict(i, histogram):
            histogram[i] = histogram[i] + 1
        else:
            histogram[i] = 1
    return histogram


def reverse_number1(n):
    number = 0
    while n > 10:
        number = number * 10 + n % 10
        n = n // 10
    return number * 10 + n


def p_score(n):
    if palindrome(n):
        return 1
    return 1 + p_score(n + reverse_number1(n))


def is_increasing(seq):
    last_number = seq[0]
    for i in range(1, len(seq)):
        if last_number >= seq[i]:
            return False
        last_number = seq[i]
    return True


def is_decreasing(seq):
    last_number = seq[0]
    for i in range(1, len(seq)):
        if last_number <= seq[i]:
            return False
        last_number = seq[i]
    return True


def to_binary_code(n):
    binary_code = bin(n)
    binary_code = binary_code[2:len(binary_code)]
    binary_code = int(binary_code)
    return binary_code


def is_odd(n):
    counter = 0
    while n != 0:
        residue = n % 10
        if residue % 2 == 1:
            counter += 1
        n = n // 10
    return counter % 2 == 1


def next_hack(n):
    while (True):
        n += 1
        code = to_binary_code(n)
        if palindrome(code) == True and is_odd(code) == True:
            return n
