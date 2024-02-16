#The part Callable[[int,int],float] means that the 
#func parameter expects 2 integer values, 
#and returns 1 floating point number.
from typing import Callable

def smart_divide(func:Callable[[int,int],float]):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(9, 3)