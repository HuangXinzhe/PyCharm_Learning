I = 1 + 2


class Person(object):
    def get_name(self):
        pass

    def get_age(self):
        raise NotImplementedError

    def __str__(self) -> str:  # ctrl + o
        return 'Person...'


def sum1():
    return I


try:
    f = open('test', 'r')
except:
    pass


# ctrl + alt + t

class Manager(Person):

    def get_age(self):  # ctrl + i
        pass


tom = Person()
tom.get_name()  # alt + enter   自动添加不存在的方法

lst = [1, 2, 3, 4]

for x in lst:  # ctrl + J
    print(x)
