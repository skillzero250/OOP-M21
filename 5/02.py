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


@check_password('secret')
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


result = fib(5)
if result is not None:
    print(result)