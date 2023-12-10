# zip(*iterables) = aggregate elements from two or  ore iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("password", "abc123", "guest")

users_dict = dict(zip(usernames, passwords))

users_tuple = zip(usernames, passwords)

print(users_dict)
print(users_tuple)

for user, password in users_tuple:
    print(user, password)
