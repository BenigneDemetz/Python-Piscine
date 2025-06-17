import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    if start < 0:
        start = len(family) + start
    if end < 0:
        end = len(family) + end
    if start >= len(family) or end > len(family):
        print("Start and end indices are out of bounds.")
        return None
        
    
    print(f"My shape is : {np.array(family).shape}")
    new = slice(start, end)
    new = family[new]
    print (f"My new shape is : {np.array(new).shape}")
    return new  # Return the new list
    