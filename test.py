from basic import Var,Constant
from functions import log
from operations import derivative

# print derivative(x**2**x)

x = Var('x')

print derivative(x**2**x)
print derivative(45+x**2+x+1)

print derivative(log(x))