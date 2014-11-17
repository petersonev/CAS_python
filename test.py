from basic 					import Var,Constant,Equation,Num
from functions 				import log,sin,cos
from calculus.derivatives 	import derivative
from operations 			import expand, sort, simplify, sim, evaluate
from calculus.linearAlgebra import Matrix,Vector,identityMatrix

x = Var('x')

print simplify(expand(Num(2)**(Num(3)*x**2)))