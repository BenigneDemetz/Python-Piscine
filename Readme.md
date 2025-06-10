# Python Piscine  


## What am I learning new ?


#### Tuples
Tuples are const (change to list to modify)  

#### Sets
Sets don't care about order. The order is never preserved and can change  

#### Floats
"\<var>:,f" allows to add ',' to big numbers (4242 -> 4,242) and "\<var>:.xf" add x decimals (\<42>:.2f -> 42.21) (",.xf" combined)  
":e" instead of ":f" after a float set it to scientific notation  
":.xe" set x nb after comma for decimal  

#### Isinstance
We can think "type(\<var>) == type" is best way to check the type but no.
Isinstance check the type of the object but also parents's classes
type() will return the value of the current type without giving attention to parents
ex. isinstance(my_animal, Dog) True
ex. isinstance(my_animal, Animal) True
ex. type(my_animal) == Dog True
ex. type(my_animal) == Animal False

# Data sturctures methods

### List methods
| Method | Description |
|:-------|:------------|
| append() | Adds an element at the end of the list |
| clear() | Removes all the elements from the list |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the first item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |

### Tuple methods
| Method | Description |
|:-------|:------------|
| count() | Returns the number of times a specified value occurs in a tuple |
| index() | Searches the tuple for a specified value and returns the position of where it was found |

### Set methods
| Method | Operator | Description |
|:-------|:--------:|:------------|
| add() | | Adds an element to the set |
| clear() | | Removes all the elements from the set |
| copy() | | Returns a copy of the set |
| difference() | - | Returns a set containing the difference between two or more sets |
| difference_update() | -= | Removes the items in this set that are also included in another, specified set |
| discard() | | Remove the specified item |
| intersection() | & | Returns a set, that is the intersection of two other sets |
| intersection_update() | &= | Removes the items in this set that are not present in other, specified set(s) |
| isdisjoint() | | Returns whether two sets have a intersection or not |
| issubset() | <= | Returns whether another set contains this set or not |
| | < | Returns whether all items in this set is present in other, specified set(s) |
| issuperset() | >= | Returns whether this set contains another set or not |
| | > | Returns whether all items in other, specified set(s) is present in this set |
| pop() | | Removes an element from the set (random) |
| remove() | | Removes the specified element |
| symmetric_difference() | ^ | Returns a set with the symmetric differences of two sets |
| symmetric_difference_update() | ^= | Inserts the symmetric differences from this set and another |
| union() | \| | Return a set containing the union of sets |
| update() | \|= | Update the set with the union of this set and others |

### Dict methods
| Method | Description |
|:-------|:------------|
| clear() | Removes all the elements from the dictionary |
| copy() | Returns a copy of the dictionary |
| fromkeys() | Returns a dictionary with the specified keys and value |
| get() | Returns the value of the specified key |
| items() | Returns a list containing a tuple for each key value pair |
| keys() | Returns a list containing the dictionary's keys |
| pop() | Removes the element with the specified key |
| popitem() | Removes the last inserted key-value pair |
| setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| update() | Updates the dictionary with the specified key-value pairs |
| values() | Returns a list of all the values in the dictionary |





## Datetime 

### Datetime strftime

The table below shows all the codes that you can pass to the strftime() method.

| Directive | Meaning | Example |
|:----------|:--------|:--------|
| %a | Abbreviated weekday name. | Sun, Mon, ... |
| %A | Full weekday name. | Sunday, Monday, ... |
| %w | Weekday as a decimal number. | 0, 1, ..., 6 |
| %d | Day of the month as a zero-padded decimal. | 01, 02, ..., 31 |
| %-d | Day of the month as a decimal number. | 1, 2, ..., 30 |
| %b | Abbreviated month name. | Jan, Feb, ..., Dec |
| %B | Full month name. | January, February, ... |
| %m | Month as a zero-padded decimal number. | 01, 02, ..., 12 |
| %-m | Month as a decimal number. | 1, 2, ..., 12 |
| %y | Year without century as a zero-padded decimal number. | 00, 01, ..., 99 |
| %-y | Year without century as a decimal number. | 0, 1, ..., 99 |
| %Y | Year with century as a decimal number. | 2013, 2019 etc. |
| %H | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, ..., 23 |
| %-H | Hour (24-hour clock) as a decimal number. | 0, 1, ..., 23 |
| %I | Hour (12-hour clock) as a zero-padded decimal number. | 01, 02, ..., 12 |
| %-I | Hour (12-hour clock) as a decimal number. | 1, 2, ... 12 |
| %p | Locale's AM or PM. | AM, PM |
| %M | Minute as a zero-padded decimal number. | 00, 01, ..., 59 |
| %-M | Minute as a decimal number. | 0, 1, ..., 59 |
| %S | Second as a zero-padded decimal number. | 00, 01, ..., 59 |
| %-S | Second as a decimal number. | 0, 1, ..., 59 |
| %f | Microsecond as a decimal number, zero-padded on the left. | 000000 - 999999 |
| %z | UTC offset in the form +HHMM or -HHMM. | |
| %Z | Time zone name. | |
| %j | Day of the year as a zero-padded decimal number. | 001, 002, ..., 366 |
| %-j | Day of the year as a decimal number. | 1, 2, ..., 366 |
| %U | Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, ..., 53 |
| %W | Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0. | 00, 01, ..., 53 |
| %c | Locale's appropriate date and time representation. | Mon Sep 30 07:06:05 2013 |
| %x | Locale's appropriate date representation. | 09/30/13 |
| %X | Locale's appropriate time representation. | 07:06:05 |
| %% | A literal '%' character. | %