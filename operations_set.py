a={4,5,6}
b={2,3,1}
union_set=a.union(b)#{1, 2, 3, 4, 5, 6}
print(union_set)
intersection_set=a.intersection(b)#set()
print(intersection_set)
difference_set=a.difference(b)#{4, 5, 6}
print(difference_set)
sym_diff_set=a.symmetric_difference(b)#{1, 2, 3, 4, 5, 6}
print(sym_diff_set)

#set operations
x={3,4,5}
y={7,8,9}
is_subset={1,2}.issubset(x)
print(is_subset)
is_subsuperset=x.issuperset({2,8})
print(is_subsuperset)
disjoint=x.isdisjoint({3,7})
print(disjoint)

s={45,67,7}
size=len(s)#lenth of the set
print(s)