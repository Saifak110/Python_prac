import unittest
from User import User
class UserTest(unittest.TestCase):

    def setUp(self):
        print("setup method called ....")
        self.user1 = User()
        self.user2 = User()
        self.user1.setname('Alex', 'Wil')
        self.user1.setregno(100)
        self.user2.setname('John', 'Smith')
        self.user2.setregno(200)

    def test_fullname(self):
        print("testing full name")
        self.assertEqual(self.user1.getname(), 'Alex Wil')
        self.assertEqual(self.user2.getname(), 'John Smith')


    def test_regno(self):
        print("testing reg no")
        self.assertEqual(self.user1.getregno(), 100)
        self.assertEqual(self.user2.getregno(), 200)

if __name__ == '__main__':
    unittest.main()

# import unittest
# from User import User
# class UserTest(unittest.TestCase):

#     def test_fullname(self):
#         print("testing name")
#         user1 = User()
#         user1.setname('Alex', 'Wil')
        
#         self.assertEqual(user1.getname(), 'Alex Wil')

#         user2 = User()
#         user2.setname('John', 'Smith')
#         self.assertEqual(user2.getname(), 'John Smith')

#     def test_regno(self):
#         user1 = User()
#         user1.setregno(100)
#         self.assertEqual(user1.getregno(), 100)

#         user2 = User()
#         user2.setregno(200)
#         self.assertEqual(user2.getregno(), 200)

# if __name__ == '__main__':
#     unittest.main()
