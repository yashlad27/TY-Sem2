# Sets:
# unordered and unique values -> i.e. in one location in memory
# doesnot support indexing

my_set = {1, 2, 3, 4, 5, "yash", True, True}

print(my_set)

my_set.add(100)
my_set.add(2)


my_list = [1, 2, 3, 4, 5, 5]

# convert list into set:
print(set(my_list))   # useful in unames and emails

print(1 in my_set)
print(len(my_set))

new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)