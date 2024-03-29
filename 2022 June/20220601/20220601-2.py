class Person(object):

    # 限定Person對像只能綁定_name, _age和_gender屬性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩象棋.' % self._name)
        else:
            print('%s正在玩大老二.' % self._name)


def main():
    person = Person('陳叮', 30)
    person.play()
    person._gender = '女'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True