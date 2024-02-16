# In the newer versions of Python, we can directly use the list, tuple, and dict keywords.
#Note: run in terminal $mypy filename.py to check types
price: list[int] = [213,234,984]
immutable_price: tuple[int,int,int] = (231,983,704)
price_dict: dict[str,int] = { 
    'item_1' : 340,
    'item_2' : 500,
}