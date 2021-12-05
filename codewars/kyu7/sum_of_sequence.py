"""
Description:
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
"""


class Class:

    def get_sum(self, a, b):
        return sum(range(min(a, b), max(a, b) + 1))


print(Class.get_sum(2, 3))
