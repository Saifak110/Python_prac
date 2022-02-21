# Complete the main method and user defined function to find whether a given 3-digit number is an Armstrong number or not. An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 33 + 73 + 1**3 = 371.
# Following requirements should be taken care in the program.
# Input should be taken through Console
# Program should print the output as described in the Example Section below
# If the number is not 3 digit output should show as INVALID_INPUT
# Sample Input 1:
# 371
# Expected Output:
# ARMSTRONG
# Sample Input 2:
# 832
# Expected Output:
# NOT ARMSTRONG
# Sample Input 3:
# 153
# Expected Output:
# ARMSTRONG
# Sample Input 4:
# 963
# Expected Output:
# NOT ARMSTRONG
# Sample Input 5:
# 45
# Expected Output:
# INVALID_INPUT

# def main():
#     a=input('Enter the number')
#     if len(a)!=3:
#         return 'INVALID_INPUT'
#     li=[int(i) for i in a]
#     x=li[0]**3+li[1]**3+li[2]**3
#     if x==int(a):
#         return 'ARMSTRONG'
#     elif x!=int(a):    
#         return 'NOT ARMSTRONG'
#     else:
#         return 'Something missing'
# print(main())

# Write a Python function to arrange the elements of a given list of integers where all positive integers appear before all the negative integers

# Input Format:
# The first integer N indicates number of elements in the list.
# The next N lines will have one integer per line.

# Output Format:
# Print a single list where all positive integers have appeared before all the negative integers.

# n=int(input("Enter list length"))
# b=[]
# for i in range(0,n):
#     ele = int(input())
#     b.append(ele)
# b.sort()
# print(b[::-1])  

# You need to write a program that rewrites numbers from input to output until the number 7 is encountered.
