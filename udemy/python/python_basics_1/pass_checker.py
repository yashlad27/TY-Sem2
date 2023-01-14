# Password checker:

username = input("Enter Username: \n")
password = input("Enter password: \n")

pass_len = len(password)

out_pass = '*' * len(password)

print(f"{username}, your password {out_pass} is {pass_len} letters long")