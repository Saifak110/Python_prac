# def add(a,b):
#     return a+b

# def sub(a, b):
#     return a-b

# def div(a, b):
#     return a/b

# def mul(a, b):
#     return a*b

# import calc
# a=calc.add(2,3)
# print(a)

# class Calculator:
#     a, b, c = 0, 0, 0
#     def setdata(self, a, b):
#         self.a = a
#         self.b = b

#     def add(self):
#         self.c = self.a + self.b

# calc = Calculator()
# calc.setdata(10, 20)
# calc.add()
# print(calc.c)
         

class Calculator:
    a, b, c = 0, 0,  #global variable
    def __init__(self, a, b):  #constructor
        self.a = a   #global variable and local variable 
        self.b = b

    def add(self):
        self.c = self.a + self.b

calc = Calculator(30, 40)
calc.add()
print(calc.c)

##Classes
# from Cl import Calc
# # Created a class object
# #obj = Cl.Calc()
# # Calling and printing class methods
# c = Calc.add(15,5)
# print(c)

# class Calc:
#     def add(a, b):
#         return a+b
    
#     def sub(a,b):
#         return a-b

