#Note: run in terminal $mypy filename.py to check types
from typing import Union

def inr_to_usd(inr_price:float)->Union[float,None]:
    try:
        conversion_factor = 75
        usd = inr_price/conversion_factor
        return usd
    except TypeError:
        return None  # if you retrun "atul" it will give error 


print(inr_to_usd(200))



def inr_to_usd1(inr_price:float)->float|None: # Use in newer version
    try:
        conversion_factor = 75
        usd = inr_price/conversion_factor
        return usd
    except TypeError:
        return None  # if you retrun "atul" it will give error 


print(inr_to_usd1(300))

