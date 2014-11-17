from basic 					import Var,Constant,Equation,Num
from functions 				import log,sin,cos
from calculus.derivatives 	import derivative
from operations 			import expand, sort, simplify, sim, evaluate
from calculus.linearAlgebra import Matrix,Vector,identityMatrix

x = Var('x')

# a = Matrix([1,2,3],[4,5,6],[7,8,9])
b = Matrix([x,x**2,x**3])

# print a
# print b
# print b+Matrix([3,4,5])

c = Matrix([1],[4],[7])

d = Matrix([1,2,3],[4,5,6],[7,8,9])

# print b.dot(c)
# print Matrix([4,1,2],[-1,0,.5],[0,4,1])*Matrix([7,-1,0],[6,4,3],[-8,0,2])

# print c.norm()

# print Matrix([x],[2],[3])

# print d
# print d.col(1)

# print Matrix([-1,-1],[2,5./3])*Matrix([6,-2])
# print Matrix([-1,-1],[2,3])**20

# a = Var('a')
# b = Var('b')
# c = Var('c')
# d = Var('d')
# e = Var('e')
# f = Var('f')
# g = Var('g')
# h = Var('h')

# print Matrix([-1,0,3,1],[0,5,0,2],[1,2,3,3]).ref()
# print Matrix([-1,0,3,2],[0,5,0,3],[1,2,3,8]).rref()

print Matrix([1,-5,2],[5,1,3],[0,4,-2]).det()

a = Matrix([1,-5,2],[5,1,3],[0,4,-2])
# print a.augment(identityMatrix(3)).rref()

print a**-1

print Num(1)

# print Matrix([0,-1,1,1],[1,1,-1,0])*Matrix([a,b],[c,d],[e,f],[g,h])
