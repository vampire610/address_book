import pickle
import os
import pypinyin

datafile = 'person.data'
line = '======================================='


class Person(object):
    """通讯录联系人"""

    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email


# 获取数据排序
def get_data(filename=datafile):
    return dic_sort(get_data_1(filename))


# 获取数据

def get_data_1(filename=datafile):
    # 文件存在且不为空
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None

# 字典排序
def dic_sort(dic):
    sort_dic = {}
    if dic:
        for v in sorted(dic):
            sort_dic[v] = dic[v]
        return sort_dic
    else:
        return dic




# 写入数据


def set_data(name, number, email, filename=datafile):

    personList = {} if get_data() == None else get_data()

    with open(filename, 'wb') as f:
        personList[name] = Person(name, number, email)

        pickle.dump(personList, f)

# 保存字典格式的数据到文件


def save_data(dictPerson, filename=datafile):
    with open(filename, 'wb') as f:
        pickle.dump(dictPerson, f)

# 显示所有联系人


def show_all():
    personList = get_data()
    if personList:
        for v in personList.values():
            print(v.name, v.number, v.email)
        print(line)
    else:
        print('not yet person,please add person')
        print(line)

# 添加联系人


def add_person(name, number, email):
    set_data(name, number, email)


# 编辑联系人
def edit_person(name, number, email):
    personList = get_data()
    if personList:
        personList[name] = Person(name, number, email)
        save_data(personList)


# 删除联系人
def delete_person(name):
    personList = get_data()
    if personList:
        if name in personList:
            del personList[name]
            save_data(personList)

        else:
            pass


# 搜索联系人
def search_person(name):
    personList = get_data()
    if personList:
        if name in personList.keys():
            print(personList.get(name).name, personList.get(
                name).number, personList.get(name).email)
        else:
            print('No this person of ', name)
        print(line)
