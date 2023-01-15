# List methods:

basket = [1, 2, 3, 4, 5]
print(len(basket))

# we use var + . to use/access the list methods provided
# . anything works inplace for the var in memory

# adding/appending an element:
new_list = basket.append(100)
# print(basket.append(100))

print(basket)
print(new_list)

# inserting an element:
new_basket = basket.insert(5, 200)
print(basket)
print(new_basket)

# extending our list:
new_list = basket.extend([300, 301])
new_list = basket.extend([302])
print(basket)

# Removing elements from the list:
basket.pop()
print(basket)

basket.pop(0)
print(basket)

basket.remove(4)
print(basket)

# finding elements in list:
letter_basket = ['a', 'b', 'c', 'd', 'e']

print(letter_basket.index('d'))

# we can add optional parameters:

print(letter_basket.index('d', 0, 4))  # (elem to find, start, stop)

print('d' in letter_basket)

# count how many times an element occurs:
print(letter_basket.count('a'))