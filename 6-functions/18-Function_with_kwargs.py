#Create a function that accepts any number of keyword arguments and prints them in the format key: value.


def p_kwargs(**kwargs):
    for key, values in kwargs.items():
        print(f"{key}: {values}")

p_kwargs(name = "Tina", roll_no = "43", sem = 3)
p_kwargs(name = "Mina", roll_no = 56)
p_kwargs(name = "Diya")