#! /usr/bin/env python3

# def ftprint(value):
#     """Prints the value to the console."""
#     if value < 4:
#         return False
#     return True


def ft_filter(function, iterable) -> list:
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if function is None:
        return [item for item in iterable if item]
    else:
        return iter([item for item in iterable if function(item)])


# def main():
#     """Main function to execute the script."""
#     print(ft_filter.__doc__)
#     print(filter.__doc__)
#     print(ft_filter(ftprint, [0, 1, 2, 3, 4, 5]))
#     print(filter(ftprint, [0, 1, 2, 3, 4, 5]))


# if __name__ == "__main__":
#     main()
