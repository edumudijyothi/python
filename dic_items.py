my_dict={'a':1,'b':2,'c':3}
print(my_dict.items())          # dict_items([('a', 1), ('b', 2), ('c', 3)])
print(my_dict.pop('b'))#2
print(my_dict)#{'a': 1, 'c': 3}
print(my_dict.popitem())#('c', 3)
print(my_dict)#{'a': 1}
my_dict.update({'b':9})
print(my_dict) #{'a': 1, 'b': 9}
my_dict.clear()
print(my_dict)#{}
my_dict1={'a':1,'b':2,'c':3}
copy_dict=my_dict1()
print(copy_dict)