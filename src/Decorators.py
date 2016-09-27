# Decorators
# Decorators all us to add functionality to our existing functions by adding it to the wrapper function
# We have decorated 2 functions with decorator_func but they have different numbers of arguments
# so we use *args and **kwargs to allow any number of arguments
# The 2 examples below are examples of decorator functions but we can also has decorator classes , see below
import time
from functools import wraps


def decorator_func(original_function):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_func


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method executed before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_func
def display():
    print('display one function ran from func')


@DecoratorClass
def display_class():
    print('display function ran from class')

# This can be used by directly coding the function call but because of the @decorator_func, it is not needed
# decorator_display = decorator_func(display)
# decorator_display()
display()


@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('john', 25)

display_class()

# Below are some practical examples of decorators
# this is a common use: logging
# This is a great example of just adding a decorator to a function that logs the results
# another example can be to use a timer decorator (again, see below)
# You can also stack the decorators together. However, if we didn't add the @wrap decorator
# we would see weird results depending on the order we stacked the decoractor annotations.
# If you unpack what the decorators are doing then you can see why the method in the log (for example)
# logs a message saying the wrapper function instead of the function being called. So use @wrap to resolve this issue


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with arges: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_logger
@my_timer
def display_emp_info(user_id, email):
    print('display_emp_info ran with arguments ({}, {})'.format(user_id, email))

display_emp_info('daviesr5', 'rob@mail.com')


@my_timer
@my_logger
def display_dev_info(userid, email, language):
    time.sleep(1)
    print('display_dev_info ran with arguments ({}, {})'.format(userid, email, language))

display_dev_info('sharpej', 'jamie@mail.com', 'java')
