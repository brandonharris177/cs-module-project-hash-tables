##################memoization###########################

# cache = {}

# def fib(n):
# if n <= 1
#     return n
 
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
# ​
#     return cache[n]

####################lookup table#######################

# import math

# lookup_table = {}

# def inverse_root(n):
#     return 1 / math/sqrt(n)

# def build_lookup_table():

#     for i in range(1, 10):
#         lookup_table[i] = inverse_root(n)

# build_lookup_table()

#######################Sorting##############################

# mylist = []

# d = {
#     "first": 1,
#     "second": 2
# }

# for pair in d.items():
#     print(pair)

# print(sorted(d.items()))

# sorted_list = list(d.items())
# sorted_list.sort()

# sorted_list.sort(reverse=True, key=lambda)

# print(sorted_list)

# sorted([(v, k) for k, v in d.items()])

# def print_letters(s):
#     tally = {}

#     s = s.lower()
#     # s.split() #method 1
#     s.replace(" ", "") #method 2
#     print(s)

#     for c in s:
#         # if c != " ": #method 3
#         if c not in s:
#             tally[c] = 1
#         else:
#             tally[c] += 1

#     # (sorted(tally.items(), key=lambda x: x[1], reverse=True)) #method 1 using sorted

#     tally_list = list(tally.items()) #method 2 ushing sort
#     tally_list.sort(key=lambda x: x[1], reverse=True)
#     for pair in tally_list:
#         print(pair)

# print_letters("the quick brown fox jumps over the lazy dog")

####################instructors notes sorting#################

# # lists keep things in order
# my_list = []
# ​
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# ​
# # why are dictionaries not in order? i.e., order is not guaranteed
# ## everything hashes differently
# ## don't know what index the hash function will return
# ​
# my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]
# ​
# d = {
#     'Austin': 12,
#     'Michael': 24,
#     'Troy': 35,
#     'Jorge': 99,
#     'David': 42
# }
# ​
# # how can we sort our dictionary?
# ​
# # turn into a list
# for pair in d.items():
#     print(pair)
# ​
# # d.items().sort()
# ​
# print(sorted(d.items()))
# ​
# sorted_list_of_items = list(d.items())
# sorted_list_of_items.sort()
# ​
# print(sorted_list_of_items)

####################instructor fibinacci#######################
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive
## base case
## call itself
### move in the direction of the base case
​
# finds the n-th number in the fibonacci sequence

# def fib(n):
#     if n <= 1:
#         return n
# ​
#     return fib(n - 1) + fib(n - 2)
# ​
# def simple_recursion(n):
#     if n <= 1:
#         return n
# ​
#     return simple_recursion(n - 1)
# ​
# # print(fib(3))
# # print(fib(5))
# # print(fib(6))
# # print(fib(7))
# # print(fib(8))
# # print(fib(9))
# ​
# cache = {}
# def fib(n):
#     if n <= 1:
#         return n
    
#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)
# ​
#     return cache[n]
# ​
# print(fib(50))
# ​
# # memoization
# # dynamic programming
# # top-down dynamic programming
# Collapse



# :thankyoukindly:
# 8

# 11:58
# We can use this idea of a 'cache' pretty generally, as in a lookup table for all kinds of calculations:
# lookup_table.py 
# ​
# import math
# ​
# # trade space for time
# ​
# lookup_table = {}
# ​
# def inverse_root(n):
#     return 1 / math.sqrt(n)
# ​
# def build_lookup_table():
# ​
#     for i in range(1, 1000):
#         lookup_table[i] = inverse_root(i)
# ​
# build_lookup_table()
# ​
# print(lookup_table[556])
# print(lookup_table[99])
# print(lookup_table[999])

#######################cache######################

# import math
# ​
# # trade space for time
# ​
# lookup_table = {}
# ​
# def inverse_root(n):
#     return 1 / math.sqrt(n)
# ​
# def build_lookup_table():
# ​
#     for i in range(1, 1000):
#         lookup_table[i] = inverse_root(i)
# ​
# build_lookup_table()
# ​
# print(lookup_table[556])
# print(lookup_table[99])
# print(lookup_table[999])

#####################sort and sorted######################

# # lists keep things in order
# my_list = []
# ​
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append(4)
# my_list.append(5)
# ​
# # why are dictionaries not in order? i.e., order is not guaranteed
# ## everything hashes differently
# ## don't know what index the hash function will return
# ​
# my_list = [5, 3, 4, 2, 6, 7, 8, 1, 9]
# ​
# d = {
#     'Austin': 12,
#     'Michael': 24,
#     'Troy': 35,
#     'Jorge': 99,
#     'David': 42
# }
# ​
# # how can we sort our dictionary?
# ​
# # turn into a list
# for pair in d.items():
#     print(pair)
# ​
# # d.items().sort()
# ​
# print(sorted(d.items()))
# ​
# sorted_list_of_items = list(d.items())
# ​
# def anon_function(pair):
#     return pair[1]
# ​
# # sorted_list_of_items.sort(reverse=True, key=anon_function)
# sorted_list_of_items.sort(reverse=True, key=lambda pair: pair[1])
# ​
# print(sorted_list_of_items)
# ​
# # Erik's way with list comprehension: sorted([(v, k) for k, v in d.items()])
# ​
# # const my_func = x => x * 2
# ​
# something = list(map(lambda x, y:
#     x * 2, [1, 2, 3]))
# Collapse

###############################dictionary count###############

# # Understand
# # given a string
# ## return every letter and how many times it occurs in this string
# ## sorted by frequence of occurrence
# ​
# # Planning
# # iterate through our string
# # tally the count using a dictionary
# # sort our dictionary by the value (i.e. the count of each letter)
# ​
# # upper- or lower-case everything
# # handle spaces
# ​
# # should we turn the string into a list first?
# ​
# # Execute
# def print_letter_count(s):
#     tally = {}
# ​
#     s = s.lower()
#     for character in s:
#         # if not char.isspace():
#         # if char != " ":
#         if character >= 'a' and character <= 'z':
#             if character not in tally:
#                 tally[character] = 1
#             else:
#                 tally[character] += 1
# ​
#     # print(sorted(tally.items(), key=lambda x: x[1], reverse=True))
#     # sorted gives back a new function
# ​
#     # sort works in place
#     tally_list = list(tally.items())
#     tally_list.sort(key=lambda x: x[1], reverse=True)
# ​
#     # alternate way to reverse sort
#     # tally_list.sort(key = lambda x: (-(x[1]))
# ​
#     for pair in tally_list:
#         print(f'Count: {pair[1]}, letter: {pair[0]}')
# ​
# ​
# ​
# print_letter_count("bunny hop")
# print_letter_count("The quick brown fox jumps over the lazy dog")
# ​
# # Review
# ## Well we could handle more characters than just spaces, if we wanted
