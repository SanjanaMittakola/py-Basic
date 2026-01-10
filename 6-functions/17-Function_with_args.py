#Write a function that takes variable number of arguments and returns their sum.


def sumall(*args):
    return sum(args)

print(sumall(3, 4))
print(sumall(3, 4, 5, 6))
print(sumall(2, 3, 4, 5, 6, 7, 9 ))

