#Note: run in terminal $mypy filename.py to check types
#There is a shortcut way though for this pattern. 
#We could have written Optional[float] which is exactly the same as Union[float,None].

from typing import Optional

def inr_to_usd(inr_price:float)->Optional[float]:
    try:
        conversion_factor = 75
        usd = inr_price/conversion_factor
        return usd
    except TypeError:
        return None  # if you retrun "atul" it will give error 


print(inr_to_usd("200"))



