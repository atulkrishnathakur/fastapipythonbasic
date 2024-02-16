#Note: run in terminal $mypy filename.py to check types
from typing import Union

a: list[Union[int,float]] = [10,20,30.5,2,40] # list we can directly used in newer version
b: list[int|float] = [10,20,30,25.43,20] # newer syntax in python 3.10+