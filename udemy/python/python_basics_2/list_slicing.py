# list slicing:
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart)

print(amazon_cart[0:2])

print(amazon_cart[0::2])

# lists are mutable!

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# if we want to copy a list from memory do this:
new_cart = amazon_cart[:]

# instead of:
new_cart = amazon_cart

# 2nd method causes the original amazon cart to change as well which is in our memory