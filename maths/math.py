# # import math

# # # Use dir() to get a list of all attributes (functions, variables, etc.) in the math module
# # all_math_functions = dir(math)

# # # Print the list of functions
# # print(all_math_functions)

# import math

# # Use dir() to get a list of all attributes in the math module
# all_math_attributes = dir(math)

# # Filter to get only the functions
# math_functions = [attr for attr in all_math_attributes if callable(getattr(math, attr))]

# # Print the list of functions
# print(math_functions)

# math_f =['__loader__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nextafter', 'perm', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc', 'ulp']

# print(len(math_f))

import math

#using maximum and minimum
# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)


# Absolute 
# x = abs(-7.25)

# print(x)

# The pow(x, y) function returns the value of x to the power of y or (x**y).

# x = pow(4, 3)

# print(x)

# The math.sqrt() method for example, returns the square root of a number:

# x = math.sqrt(64)

# print(x)

# The math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest integer
# Round off krta hai -- matlab nearest whole number k paas value jayegi


x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

# The math.pi constant, returns the value of PI (3.14...)

x = math.pi

print(round(x,5))





