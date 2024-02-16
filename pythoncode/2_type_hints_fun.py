def total_price1(price1, price2):
    return f"Total Price Rs {price1 + price2}/-"

print(total_price1(100,200))


def total_price2(price1, price2):
    return f"Total Price Rs {price1 + price2}/-"

print(total_price2("100","200"))


#install pip install mypy from https://pypi.org/project/mypy/ 
#Note: run in terminal $mypy filename.py to check types
def total_price3(price1: int, price2: int)->str:
    return f"Total Price Rs {price1 + price2}/-"

tottalp = total_price3("100",200)




