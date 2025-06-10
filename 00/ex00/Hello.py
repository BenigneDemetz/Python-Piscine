#!/usr/bin/env python3

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list.pop(1)
ft_tuple = list(ft_tuple)
ft_tuple.pop(1)
ft_set.remove("tutu!")


ft_list.append("World!")
ft_tuple.append("France!")
ft_tuple = tuple(ft_tuple)
ft_set = list(ft_set)
ft_set.append("Paris!")
ft_set = set(ft_set)
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)