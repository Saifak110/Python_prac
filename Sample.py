# a = [10, 20, 30, 40]
# b = a

# b[1] = 50

# # print(b)

# # print(a)

# # a = [10, 20, 30, 40]
# # b = a.copy()
# # b[1] = 50
# # print(a)
# # print(b)

# print(id(a))
# print(id(b))

#List of lists
a = [10, 20, 30]
b = [40, 50, 60]
a.append(b)
# print(a)

# print(a[3])
# print(a[3][1])

c = [70, 80, 90]
b.append(c)
print(a)

print(a[3][3][1])

c[1] = 0

print(a[3][3][1])
