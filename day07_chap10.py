#10.1
class Thing():
    pass
example = Thing()
print(Thing, example)
#다르다 .

#10.2
class Thing2():
    letters = 'abc'
    pass
print(Thing2.letters)


#10.3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'
p1 = Thing3()
print(p1.letters) #이렇게 하면 출력이 된다.
# print(Thing3.letters) 출력이 안 된다. 오류. 인스턴스를 만들어야 한다.

#10.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

p = Element('Hydrogen', 'H', 1)


#10.5
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])

# #10.6
# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def dump(self):
#         print(f'{self.name}, {self.symbol}, {self.number}')
#
# hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
# print(Element.dump(hydrogen))


10.7
print(hydrogen)
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f"{self.name}, {self.symbol}, {self.number}"
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen)

# #10.8
# class Element():
#     def __init__(self, name, symbol, number):
#         self.__name = name
#         self.__symbol = symbol
#         self.__number = number
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def symbol(self):
#         return self.__symbol
#
#     @property
#     def number(self):
#         return self.__number
#
# # hydrogen = (**el_)
