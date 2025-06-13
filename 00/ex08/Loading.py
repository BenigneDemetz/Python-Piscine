#!/usr/bin/env python3

from time import time
import os

def set_string(i, speed, start_time, lst) -> str:
    """
    Set the string to be printed in the progress bar.
    """
    remaining_time = "?"
    size = len(lst)-1
    try:
        termsize = os.get_terminal_size().columns
        char = '█'
    except OSError:
        char = '='
        termsize = 80
    if i > 1:
        remaining_time = (time() - start_time) * (size - i) / i
        if remaining_time < 0:
            remaining_time = 0
        min = int(remaining_time // 60)
        snd = int(remaining_time % 60)
        remaining_time = str(f"{min:02}:{snd:02}")
    data = ""
    elapsed_time = time() - start_time
    min = int(elapsed_time // 60)
    snd = int(elapsed_time % 60)
    elapsed_time = str(f"{min:02}:{snd:02}")
    if speed is not None:
        speed = (time() - speed)
        speed = f"{1 / speed:.2f}"
    else:
        speed = '?'

    speedpad = ' ' if len(speed) < 5 else ''
    
    begin = f"{int(i/size*100)}%|"
    end = f"| {i}/{size+1} [{elapsed_time}<{remaining_time}, {speedpad}{speed}it/s]"
    total = termsize - len(begin + end)
    for j in range(int(i * (total) / size)):
        data += char
    fill = termsize - len(data) - len(begin) - len(end)
    for j in range(fill):
        data += " "
    string = begin + data + end
    return string


def ft_tqdm(lst: range) -> None:
    start_time = time()
    speed = None
    for i in lst:
        string = set_string(i, speed, start_time, lst)
        print('\r' + string, end="", flush=True)
        speed = time()
        yield i
    string = set_string(i+1, speed, start_time, lst)
    print('\r' + string, end="", flush=True)
    # print()
    return None
