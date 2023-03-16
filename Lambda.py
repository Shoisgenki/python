# function written in 1 line using lambda keyword

# accepts any number of arguments, but only has one expression

# think of it as a shortcut function

# useful if needed for a short period of time



# lambda parameters: expression

double = lambda x: x * 2

multiply = lambda x, y: x * y

add = lambda x, y, z: x + y + z

full_name = lambda fn, ln: fn + " " + ln

age_check = lambda age: True if age >= 18 else False

print(age_check(18))
