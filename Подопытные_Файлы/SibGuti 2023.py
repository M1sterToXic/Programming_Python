# class Dom:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def check_int(cls, padic):
#         return type(padic) in (int, float)
#
#     def set_coord(self, padic = 0, cvartir = 0):
#         if self.check_int(padic) and self.check_int(cvartir):
#             self.padic = padic
#             self.cvartir = cvartir
#         else:
#             raise ValueError("Это должно быть число!")
#
#     def vizov(self):
#         return self.padic, self.cvartir
#
# dom = Dom(1, 2)
# dom.set_coord(1, 20)
# print(dom.vizov())

class User:
    colvo = 0

    def __init__(self, name, salary, age):
        self.salary = salary
        self.age = age
        self.name = name
        User.colvo += 1

    def get_coord(self):
       print("Name: {}. Salary: {}. Age: {}".format(self.name, self.salary, self.age))

    def quantity(self):
        print("Всего сотрудников: %d"%User.colvo)

men1 = User("Nikita", 5000, 18)
men1.get_coord()
print("Всего сотрудников: %d"%User.colvo)