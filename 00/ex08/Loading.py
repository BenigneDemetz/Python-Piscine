#!/usr/bin/env python3


def set_string(i, lst) -> str:
    """
    Set the string to be printed in the progress bar.
    """
    size = len(lst)-1
    try:
        char = '█'
    except OSError:
        char = '='
    termsize = 80
    data = ""
    
    begin = f"{int(i/size*100)}%|"
    end = f"| {i}/{size+1}"
    total = termsize - len(begin + end)
    for j in range(int(i * (total) / size)):
        data += char
    fill = termsize - len(data) - len(begin) - len(end)
    for j in range(fill):
        data += " "
    string = begin + data + end
    return string


def ft_tqdm(lst: range) -> None:
    speed = None
    for i in lst:
        string = set_string(i, lst)
        print('\r' + string, end="", flush=True)
        yield i
    string = set_string(i+1, lst)
    print('\r' + string, end="", flush=True)
    # print()
    return None
