"""Урок №2: 16.04.24"""
# class Point:
#     color = 'green'
#     circle = 2
#
#
# #     def set_coords(self):
# #         print('вывод метода set_coords' + str(self))
# #
# # pt = Point()
# # Point.set_coords(pt)
# # print(pt.set_coords)
# # print(pt.set_coords())
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return(self.x, self.y)
#
# """Обычные методы и операции"""
# pt = Point()
# pt2 = Point()
# pt.set_coords(2, 9 )
# pt2.set_coords(20, 90 )
# print(pt.__dict__)
# print(pt2.__dict__)
# print(pt.color)
# print(pt.circle + 2)
# print(pt.circle)
#
# """Ввиде кортежа"""
# pt = Point()
# pt.set_coords(2, 9)
# print(pt.get_coords())
# f = getattr(pt, "get_coords")
# print(f)
# print(f())


"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""


# class Dog():
#     age = 7
#     color = "orange"
#
#     """Инициализация"""
#     def barking(self, voice, long):
#         self.voice = voice
#         self.long = long
#
#
#     def get_barking(self):
#         return(self.voice, self.long)
#
#
# pp = Dog()
# pp.barking(155, 1000)
# print(pp.get_barking())
# pp.barking(1, 2)
# print(pp.__dict__)

"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""

"""Урок 17.04.24"""
# class Point:
#     color = 'green'
#     circle = 2
#
#     def __init__(self, x = 0, y = 0):
#         print("__init__")
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра" + str(self))
#
#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#
# pt = Point(0, 3)
# print(pt.__dict__)



"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""21.04.24"""

# class Point():
#
#     def __new__(cls, *arkk, **kvarkk):
#         print("Вызов __new__ для " + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x = 0, y = 0):
#         self. x = x
#         self.y = y
#
# pt = Point(1, 2)
# print(pt.__dict__)

# class DataBase():
#     __instance = None
#
#     def __new__(cls, *ark, **vark):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __del__(self):
#         DataBase.__instance = None
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#
#
#     def connect(self):
#         print(f"Соединено с БД: {self.user}, {self.psw}, {self.port}")
#
#     def close(self):
#         print("Закрытие с БД")
#
#     def read(self):
#         return("Данные из БД")
#
#     def write(self, data):
#         print(f"Запись в БД: {data}")
#
#
# db = DataBase("gg9080", "1234", 100)
# db2 = DataBase("gg90", "12", 100)
# db.connect()
# db2.connect()


"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""24.06.24"""
# class Vector:
#     MIN_CORD = 0
#     MAX_CORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_CORD <= arg <= cls.MAX_CORD
#
#
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#
#         print("__init__ ; norm2", self.norm2(self.x, self.y))
#
#
#
#     def get_coord(self):
#         return self.x, self.y
#
#
#
#     @staticmethod
#     def norm2(x, y):
#         return (x*x) + (y*y)
#
#
#
#
# v = Vector(10, 20)
# print(Vector.norm2(5, 4))
# print(Vector.validate(5))
# res = Vector.get_coord(v)
# print(res)



"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""16.07.24"""
from accessify import private, protected
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами!")

    def get_coord(self):
        return self.__x, self.__y


pt = Point()
pt.set_coord(10, 20)
print(pt.get_coord())
print(dir(pt))
pt._Point__check_value(5)

"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
"""17.07.24"""



"""/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""