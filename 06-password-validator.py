def length_checker(password):
    if len(password) < 6 or len(password) > 10:
        return 'Password must be between 6 and 10 characters'


def letters_and_digits(password):
    for i in password:
        if 48 <= ord(i) <= 57 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            continue
        else:
            return 'Password must consist only of letters and digits'



def digit_count_check(password):
    digit_count = 0
    for n in password:
        if 48 <= ord(n) <= 57:
            digit_count += 1
    if digit_count < 2:
        return 'Password must have at least 2 digits'


def valid_checker(password):
    validators = [length_checker,
                 letters_and_digits,
                 digit_count_check]
    errors = []
    for valid_checker in validators:
        result = valid_checker(password)
        if result is not None:
            errors.append((result))
    if len(errors) == 0:
        return 'Password is valid'
    else:
        return '\n'.join(errors)


password = input()
result = valid_checker(password)
print(result)
