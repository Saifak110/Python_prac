# def mul(a, b):
#     return a*b

# a = 30
# c = mul(a, b=10)
# print(c)

# def sub(a, b):
#     return a-b

# ans = sub(b=10, a=20)
# print(ans)

#Fibonacci series
def fib1(x):
    if x==1 or x==2:
        return 1
    else:
        return fib1(x-1)+fib1(x-2)
print(fib1(7))

class User:
    pass

user1 = User()

user1.name = "Amarnath"
user1.id = 100

print(user1)

print(user1.name)
print(user1.id)

user2 = User()
user2.name = "Varun"
user2.id = 101
print(user2.name)
print(user2.id)

