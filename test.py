from basic 					import Var,Constant
from functions 				import log
from calculus.derivatives 	import derivative
from operations 			import expand, sort, simplify
# import math

# print derivative(x**2**x)

x = Var('x')

# print derivative(x**2**x)
# print derivative(45+x**2+x+1)

# print derivative(2-x*(x+x)*(x+x*(x+2*x)+2)*2+2)


# a = 2-x*(x+x)*(x+x*(x+2*x)+2)*2+2
# print derivative(a)
# print a

a = Constant('a')
b = Constant('b')

print sort(simplify(derivative(a*x**b/log(x))))