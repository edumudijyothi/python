#set operations
set={1,3,2}
print(set)#{1, 2, 3}
set.add(4)
print(set)#{1, 2, 3,4}
set.update([6,7,8])
print(set)#{1, 2, 3, 4, 6, 7, 8}
set.remove(3)
print(set)#{1, 2, 4, 6, 7, 8}
set.discard(2)
print(set)#{1,4, 6, 7, 8}
element=set.pop()
print(set)#{4, 6, 7, 8}
set.clear()
print(set)#set()