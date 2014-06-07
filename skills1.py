# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []
    for num in some_list:
        if num % 2 == 1:
            new_list.append(num)
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []
    for num in some_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

# Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for word in word_list:
        if len(word) >= 4:
            new_list.append(word)
    return new_list


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = sorted(some_list)[0]
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = sorted(some_list)[-1]
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return []

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return []

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None
