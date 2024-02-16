def dec_msg(fn):
    def inner(x,y,z):
        if x == 0 and y == 0:
            return "Please enter x and y greater than 0"
        else:    
            return fn(x,y,z)
    return inner


@dec_msg
def mymsg(a, b, c):
    return f"sum = {a + b + c}"


print(mymsg(10,20,100))    