from typing import List 

Image = List[List[int]]

def flatten_images(image: Image)->List:
    flat_list = []
    for sublist in image:
        for item in sublist:
            flat_list.append(item)
    return flat_list



fl = flatten_images([[10,20,30],[100,200,300]])
print(fl)
