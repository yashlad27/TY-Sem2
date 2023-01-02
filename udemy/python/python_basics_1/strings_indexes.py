selfish = "01234567"

# [start : stop : stepover]

print(selfish[0:8:2])

print(selfish[3:])

print(selfish[:5])

print(selfish[::3])

print(selfish[-1])

print(selfish[::-1]) # reverse the string 

# Strings in python are immutable!

selfish = selfish + '8'

print(selfish)