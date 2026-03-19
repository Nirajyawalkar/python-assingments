# <<<<<<<<<< lab assignments 1 >>>>>>>>>>>>
# class Employee:
#     def __init__(self, name, age, salary, address):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.address = address
#
#     def display(self):
#         print(self.name, self.age, self.salary, self.address)
#
#
# class Manager(Employee):
#     pass
#
#
# managers = []
#
# for i in range(2):  # change to 10 if needed
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     salary = float(input("Enter salary: "))
#     address = input("Enter address: ")
#
#     m = Manager(name, age, salary, address)
#     managers.append(m)
#
# for m in managers:
#     m.display()

# <<<<<<< lab assignments2 >>>>>>>>>>>
# class Book:
#     def __init__(self, name):
#         self.name = name
#         self.available = True
#
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, name):
#         self.books.append(Book(name))
#
#     def lend_book(self, name):
#         for b in self.books:
#             if b.name == name and b.available:
#                 b.available = False
#                 print("Book issued")
#                 return
#         print("Not available")
#
#     def return_book(self, name):
#         for b in self.books:
#             if b.name == name:
#                 b.available = True
#                 print("Book returned")
#
#     def display(self):
#         for b in self.books:
#             print(b.name, "Available" if b.available else "Issued")
#
#
# lib = Library()
#
# while True:
#     print("\n1.Add 2.Lend 3.Return 4.Display 5.Exit")
#     ch = int(input("Enter choice: "))
#
#     if ch == 1:
#         lib.add_book(input("Enter book name: "))
#     elif ch == 2:
#         lib.lend_book(input("Enter book name: "))
#     elif ch == 3:
#         lib.return_book(input("Enter book name: "))
#     elif ch == 4:
#         lib.display()
#     else:
#         break