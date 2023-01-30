# Tuples:

my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)

new_tuple = my_tuple[1:3]
print(new_tuple)

x, y, z, *other = (5, 6, 7, 8, 9, 10)
print(other)

print(my_tuple.count(2))
print(my_tuple.index(5))
print(len(my_tuple))

