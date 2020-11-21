user_names = input().split(", ")

def len_checker(user):
    if 3 <= len(user) <= 16:
        return True
    return False


def symbol_checker(user):
    user_check = ''
    for el in user:
        if el.isalnum() or el == '-' or el == '_':
            user_check += (el)
    if user_check == user:
        return True
    return False


def redundant_checker(user):

    if user[0].isalnum() and user[-1].isalnum():
        return True
    return False



valid_users = []
for user in user_names:
    if len_checker(user) and symbol_checker(user) and redundant_checker(user):
        valid_users.append(user)

for valid_user in valid_users:
    print(valid_user)



