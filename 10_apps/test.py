"""
Python Challenges
Author: BluJayThomas, updated 'Daily'
"""

"""
capital_indexes
Author: BluJayThomas, updated 'Daily'
"""
# def mid(s):
#     if (len(s) % 2) == 0:
#         print("")
#         return ""
#     else:
#         middle = len(s)/2
#         mid_string = s[int(middle)]
#         return mid_string
#
"""
middle character
Author: BluJayThomas, updated 'Daily'
"""
# mid('abcd')
# def online_count(statuses):
#     count = 0
#     for i in statuses.values():
#         if 'online' in i:
#             count += 1
#     return count
#
#
# online_count({'Alice': 'online', 'Bob': 'online'})
"""
Random number 
Author: BluJayThomas, updated 'Daily'
"""
# import random
#
#
# def random_number():
#     num = random.randint(1, 101)
#     return num
#
#
# random_number()
"""
capital_indexes
Author: BluJayThomas, updated 'Daily'
"""
# def capital_indexes(s):
#     return [i for i, c in enumerate(s) if c.isupper()]
# capital_indexes("HeLlO")

"""
Only ints
Author: BluJayThomas, updated 'Daily'
"""
# def only_ints(i, s):
#     if type(i) is int and type(s) is int:
#         return True
#     else:
#         return False
#
#
# only_ints(1, 2)

"""
Anagram
Author: BluJayThomas, updated 'Daily'
"""
# def is_anagram(word, word2):
#     result_1 = [char for char in word]
#     result_1.sort()
#     result_2 = [char for char in word2]
#     result_2.sort()
#     print(result_2, result_1)
#     if result_1 == result_2:
#         return True
#     else:
#         return False
#
#
# is_anagram("Alice", "Bob")
"""
double letters
Author: BluJayThomas, updated 'Daily'
"""
# def double_letters(s):
#     lists = [char for char in s]
#     print(lists)
#     length = len(s)
#     print(length)
#     for i in range(length):
#         print(lists[i], lists[i - 1])
#         if lists[i] == lists[i - 1]:
#             print("True: ", lists[i], lists[i - 1])
#             return True
#     return False
#
#
# double_letters("abc")
"""
add/remove dots
Author: BluJayThomas, updated 'Daily'
"""
# def add_dots(s):
#     return '.'.join(s)
#
#
#
# def remove_dots(s):
#     return (s.replace('.', ''))
#
#
# add_dots("abc")
# remove_dots("t.e.s.t")
# def count(s):
#     hyphen = 1
#     length = len(s)
#     for i in s:
#         if i == "-":
#             hyphen += 1
#     return hyphen
#
#
# count("ho-tel")
"""
Flatten list
Author: BluJayThomas, updated 'Daily'
"""
# def flatten(s):
#     result = []
#     for sublist in s:
#         for item in sublist:
#             result.append(item)
#     return result
#
#
# flatten([[1, 2], [3, 4]])

"""
Flatten list
Author: BluJayThomas, updated 'Daily'
"""
''''
Min max Python
'''

# def largest_different(s):
#     print(s)
#     minimum = min(s)
#     maxinum = max(s)
#     print(maxinum - minimum)
#     return maxinum - minimum
#
#
# largest_different([1, 2, 3])

"""
Palindrome, abba is because it's the same backwords
"""
# def palindrome(s):
#     print(s)
#     result = s[::-1]
#     print(result)
#     if s == result:
#         print('True')
#         return True
#     else:
#         print('False')
#         return False
#
#
# palindrome('abc')
"""
Up 1 down 1
"""
# def up_down(s):
#     up = s + 1
#     down = s - 1
#     print(up, down)
#     return down, up
# up_down(5)
"""
If else all equal 
"""

# def all_equal(s):
#     length = len(s)
#     for i in range(length):
#         if s[i] == s[i - 1]:
#             print("True")
#             return True
#         else:
#             print("False")
#             return False
#
#
# all_equal([11, 10, 11])
"""
Triple True
"""


# def triple_and(s, d, f):
#     if s is True and d is True and f is True:
#         print("True")
#         return True
#     else:
#         print("False")
#         return False
#
#
# triple_and(True, False, True)

def zap(s, f):
    print(s, f)


zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
)
