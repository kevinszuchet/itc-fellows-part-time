"""
- Implement print_params_and_return_value decorator function that will wrap any other function,
    and will print all the input params and the return value of the function it wraps.
- Decorate the 2 functions below
- Make sure it will behave as the original function, and code that worked with any original function
    will continue working when replaced with a wrapped function
The wrapper function will print the following:
    - Bonus: what function is being wrapped
    - number of positional parameters (args)
    - Index, type and values of the positional parameters
    - number of named parameters (kwargs)
    - index, name, type and value of the named parameter
    - the return value of the function
"""


def print_params_and_return_value(func):
    def wrapper(*args, **kwargs):
        print(f"Is time to evaluate {func} function")

        print(f"Number of positional args: {len(args)}")
        for i, arg in enumerate(args):
            print(f"Positional arg #{i}. Type: {type(arg)} - Value: {arg}")

        print(f"Number of named args: {len(kwargs)}")
        for i, arg in enumerate(kwargs.items()):
            print(f"Named arg #{i}. Name: {arg[0]} - Type: {type(arg[1])} - Value: {arg[1]}")

        result = func(*args, **kwargs)

        print(f"The result of evaluating the function was: {result}")

        return result

    return wrapper


@print_params_and_return_value
def add_4(param1, param2, param3, param4):
    return param1 * 1000 + param2 * 100 + param3 * 10 + param4


@print_params_and_return_value
def just_print():
    print('Hi')


assert add_4(1, 2, param4=4, param3=3) == 1234
assert just_print() is None

"""
Output example:
Calling function: <function add_4 at 0x01EEAD18>
There are 2 positioned parameters:
Positional arg 0 (type <class 'int'>): 1
Positional arg 1 (type <class 'int'>): 2
There are 2 named parameters:
Named arg 0 name "param4" (type <class 'int'>): 4
Named arg 1 name "param3" (type <class 'int'>): 3
Return value: 1234
Calling function: <function just_print at 0x01EEAC88>
There are 0 positioned parameters:
There are 0 named parameters:
Hi
Return value: None
"""
