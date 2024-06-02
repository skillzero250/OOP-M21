def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            correct_password = password
            user_password = input('Enter password: ')
            if user_password != correct_password:
                print('Access denied')
                return None
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator


@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print(f'Making a burger with {typeOfMeat} meat, with onion={withOnion}, and with tomato={withTomato}')


result = make_burger('beef', withOnion=True, withTomato=False)
if result is not None:
    print(result)