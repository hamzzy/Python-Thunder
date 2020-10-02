"""
Problem statement: Count the amount of ones in the binary representation of an integer. So for example, since 12 is '1100' in binary, the return value should be 2
Problem Link: https://edabit.com/challenge/GbyPdqNnp75Wci7Cn
"""


def count_ones(num):
    binary = bin(num)[2:] 
    one=binary.count('1')
    return one


if __name__ == "__main__":
    print(count_ones(12))