class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 訪問器 - getter方法
    @property
    def name(self):
        return self._name

    # 訪問器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩象棋.' % self._name)
        else:
            print('%s正在玩大老二.' % self._name)


def main():
    person = Person('陳叮', 12)
    person.play()
    person.age = 30
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()