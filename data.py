import pickle



ad = {}


class Person:
    def __init__(self, name, tel, email):
        self.name = name
        self.tel = tel
        self.email = email


while 1:
    print('请输入姓名，等信息')
    name = input('姓名')
    tel = input('tel')
    email = input('email')
    ad[name] = Person(name, tel, email)

    for v in ad.values():
        print(v.name)
