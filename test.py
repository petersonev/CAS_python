from basic 					import Var,Constant,Equation
from functions 				import log,sin,cos
from calculus.derivatives 	import derivative
from operations 			import expand, sort, simplify, sim, evaluate
from calculus.linearAlgebra import Matrix,Vector

x = Var('x')

# a = Matrix([1,2,3],[4,5,6],[7,8,9])
b = Matrix([x,x**2,x**3])

# print a
# print b
# print b+Matrix([3,4,5])

c = Matrix([1],[4],[7])

d = Matrix([1,2,3],[4,5,6],[7,8,9])

# print b.dot(c)
print Matrix([4,1,2],[-1,0,.5],[0,4,1])*Matrix([7,-1,0],[6,4,3],[-8,0,2])