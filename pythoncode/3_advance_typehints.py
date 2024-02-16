# For python version <=3.9
# if you are using python version <=3.9 then import List, Tuple , Dict
# from typing import List, Tuple, Dict 

#Note: run in terminal $mypy filename.py to check types
from typing import List, Tuple, Dict

price: List[int] = [213,234,984] # write List in capital letter in python version <=3.9
immutable_price: Tuple[int,int,int] = (231,983,704) # write Tuple in capital letter in python version <=3.9
price_dict: Dict[str,int] = {  # write Dict in capital letter in python version <=3.9
    'item_1' : 340,
    'item_2' : 500,
}


