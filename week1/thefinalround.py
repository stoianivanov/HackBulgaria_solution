from therealdeal import *
from copy import *
import calendar
from warmups import *


def count_words(arr):
    result = {}
    for key in arr:
        if key not in result:
            result[key] = 1
        else:
            result[key] = result[key] + 1
    return result


def unique_words_count(arr):
    return sum([1 for i in range(0, len(count_words(arr)))])


def nan_expand(times):
    if times == 0:
        return ""
    else:
        result = ""
        for i in range(0, times):
            result += "Not a "
        return result + "NaN"


def iterations_of_nan_expand(string):
    counter = string.count("Not a")
    if counter == 0 and string != "" or (counter * len("Not a ") + 3) < len(string):
        return False
    return counter


"""def get_divisors(n):
    i = 1
    result = []
    while i <= n:
        if n % i == 0:
            result.append(i)
        i += 1
    return result

"""


def prime_factorization(n):
    devisors = get_divisors(n)
    i = 1
    count = 0
    result = []
    while n > 1:
        if not is_prime(devisors[i]):
            i += 1
        if n % devisors[i] == 0:
            n = n//devisors[i]
            count += 1
        else:
            result.append((devisors[i], count))
            i += 1
            count = 0
    result.append((devisors[i], count))
    return result


def group(items):
    result = []
    item = []
    for i in items:
        if i in item:
            item.append(i)
        else:
            if len(item) > 0:
                result.append(item)
                item = []
                item.append(i)
            else:
                item.append(i)
    result.append(item)
    return result


def max_consecutive(items):
    return max(group(items))[0]


def groupby(func, seq):
    keys = set(map(func, seq))
    return {key: list(filter(lambda x: func(x) == key, seq)) for key in keys}


def divided_five(number):
    res = ""
    while number % 5 == 0:
        res += "eggs "
        number = number//5
    return res


def divided_three(number):
    res = ""
    while number % 3 == 0:
        res += "spam "
        number = number//3
    return res[:len(res) - 1]


def prepare_meal(number):
    result_spam = ""
    result_eggs = ""
    result_spam = divided_three(number)
    result_eggs += divided_five(number)
    if len(result_spam) > 1 and len(result_eggs) > 1:
        return result_spam + "and " + result_eggs
    return result_spam + result_eggs[:len(result_eggs)-1]


def is_an_bn_generator(n):
    return "a"*n + "b"*n


def is_an_bn(text):
    return text == is_an_bn_generator(len(text)//2)


def magic_square(square):
    row_sums = set(list(map(sum, square)))
    col_sums = set(list(map(sum, zip(*square))))
    mdiag_sum = sum(map(lambda el: el[1][el[0]], list(enumerate(square))))
    rdiag_sum = sum(map(lambda el: el[1][len(square) - 1 - el[0]],list(enumerate(square))))
    return len(row_sums) <= 1 and len(col_sums) <= 1 and row_sums.pop() == col_sums.pop() == mdiag_sum == rdiag_sum


def to_digits(n):
    digits_list = []
    while n > 0:
        digits_list.append(n % 10)
        n = n // 10
    return digits_list[::-1]


def sum_of_digits(number):
    numbers = to_digits(number)[::-1]
    sum1 = ""
    for i in range(0, len(numbers)):
        if i % 2 != 0:
            sum1 += str(numbers[i]*2)
        else:
            sum1 += str(numbers[i])
    return sum([int(i) for i in sum1])


def is_credit_card_valid(number):
    if len(to_digits(number)) % 2 != 0:
        if sum_of_digits(number) % 10 == 0:
            return True
        else:
            return False
    else:
        return False


def to_string(string):
    result = ""
    for i in string:
        result += i
    return result


def reduce_file_path(path):
    splitted_path = path.split('/')
    while '.' in splitted_path:
        splitted_path.remove('.')
    while '' in splitted_path:
        splitted_path.remove('')
    final_path = []
    while len(splitted_path) != 0:
        top = splitted_path.pop(0)
        if top == '..':
            if len(final_path) != 0:
                final_path.pop()
        else:
            final_path.append(top)
    return "/" + "/".join(final_path)


def goldbach(n):
    return [(x, n - x) for x in range(2, n//2 + 1)
            if is_prime(x) and is_prime(n - x)]


def is_leap_year(year):
    if calendar.isleap(year):
        return {3, 4}
    else:
        return {4}


def friday_years(start, end):
    return sum([1 for elem in[year for year in range(start, end + 1) if calendar.weekday(year, 1, 1) in is_leap_year(year)]])
