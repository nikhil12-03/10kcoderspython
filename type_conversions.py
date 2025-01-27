#### Conversion from `int`
# To float
x = 3
float_x = float(x)  # 3.0

# To str
y = str(x)  # "3"

# To bool
z = bool(x)  # True

# To tuple
# tuple_x = tuple(x)  # Error (TypeError)

# To dict
# dict_x = dict(x)  # Error (TypeError)

# To set
# set_x = set(x)  # Error (TypeError)

# To list
# list_x = list(x)  # Error (TypeError)

# To range
range_x = range(x)  # range(0, 3)


#### Conversion from `float`
# To int
x = 3.5
int_x = int(x)  # 3

# To str
y = str(x)  # "3.5"

# To bool
z = bool(x)  # True

# To tuple
# tuple_x = tuple(x)  # Error (TypeError)

# To dict
# dict_x = dict(x)  # Error (TypeError)

# To set
# set_x = set(x)  # Error (TypeError)

# To list
# list_x = list(x)  # Error (TypeError)

# To range
# range_x = range(x)  # Error (TypeError)


#### Conversion from `str`
# To int
x = "3"
int_x = int(x)  # 3

# To float
y = "3.5"
float_y = float(y)  # 3.5

# To bool
z = "True"
bool_z = bool(z)  # True

# To tuple
tuple_x = tuple(x)  # ('3',)

# To dict
# dict_x = dict(x)  # Error (TypeError)

# To set
set_x = set("hello")  # {'h', 'e', 'l', 'o'}

# To list
list_x = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# To range
# range_x = range(x)  # Error (TypeError)


#### Conversion from `bool`
# To int
x = True
int_x = int(x)  # 1

# To float
float_x = float(x)  # 1.0

# To str
str_x = str(x)  # "True"

# To tuple
# tuple_x = tuple(x)  # Error (TypeError)

# To dict
# dict_x = dict(x)  # Error (TypeError)

# To set
# set_x = set(x)  # Error (TypeError)

# To list
# list_x = list(x)  # Error (TypeError)

# To range
# range_x = range(x)  # Error (TypeError)


#### Conversion from `tuple`
# To int
# int_x = int((1, 2))  # Error (TypeError)

# To float
# float_x = float((1, 2))  # Error (TypeError)

# To str
x = (1, 2)
str_x = str(x)  # "(1, 2)"

# To bool
bool_x = bool(x)  # True

# To dict
# dict_x = dict(x)  # Error (unless tuple of pairs)

# To set
set_x = set((1, 2))  # {1, 2}

# To list
list_x = list((1, 2))  # [1, 2]

# To range
# range_x = range((1, 2))  # Error (TypeError)
