from basic 					import Var,Constant,Equation,Num,Mul
from functions 				import log,sin,cos
from calculus.derivatives 	import derivative
from operations 			import expand, sort, simplify, sim, evaluate
from calculus.linearAlgebra import Matrix,Vector,identityMatrix
from inputs 				import numNum
from equations				import solve

# # x = Var('x')

# # # print simplify(expand(Num(2)**(Num(3)*x**Num(2))))
# # # print eval(numNum('simplify(expand(2**(3*x**2/9)))'))

# # a1 = numNum('Matrix([1,-5,2],[5,1,3],[0,4,-2])')
# # aa = eval(a1)
# # # print a.augment(identityMatrix(3)).rref()
# # # print a1
# # # print a

# # a = Var('a')
# # b = Var('b')
# # c = Var('c')
# # d = Var('d')

# # aa = Matrix([1,2],[3,4])
# # # aa = Matrix([a,b],[c,d])

# # # print (aa.ref()).simplify()

# # # print type(simplify(Num(1)-Num(1)))

# # w = numNum('((1+(3-1(3+(3-1))**-1-1))')
# # # print w

# # # r = (Num(1)+(Num(3)-Num(1)*(Num(3)+(Num(3)-Num(1)))**-Num(1)-Num(1)))

# # # print r
# # # print simplify(r)
# # # print simplify(simplify(r))

# # # print derivative((Num(2)).copy())

# # # print (d-b*c/a)

# # print -1<0
# # print Num(-1)==-1

# # # print Vector(Num(1),x**Num(2),Num(3)).dot(Vector(Num(1),Num(2),x))
# # print Vector(1,2,3).dot(Vector(1,2,x))
# # # print Num(-1)*Num(-1)*Num(1)*Num(-1)
# a = numNum('(4+(-2*3)+(-(4+(-2*3))*(4+(-2*3))*(4+(-2*3))**-1))')

# print simplify(eval(a))

# print Matrix([1,2,1,0],[3,4,0,1],[3,4,0,1]).ref()
# # print eval(numNum('Matrix([1,2,1,0],[3,4,0,1],[3,4,0,1])')).ref()

E = Var('E')
pi = Constant('pi')
e_0 = Constant('e_0')
q = Var('q')
r = Var('r')

E_field = Equation(E,(Num(1)/(Num(4)*pi*e_0)) * q/r**2)

# print solve(E_field,r)

# (-(4pie_0)^-1qr^2^-1) (((4pie_0)^-1qr^-2)+(-E)+(-(4pie_0)^-1qr^-2))

# print simplify(((Num(1)/(Num(4)*pi*e_0)) * q/r**2)**-Num(1))
# print
# print sim(((Num(1)/(Num(4)*pi*e_0)) * q/r**2)**-Num(1))

a = Var('a')
b = Var('b')
c = Var('c')

print a+b+c

# a = b^2*c  -->  b = (a/c)^.5

# print solve(Equation(a,b**Num(2)*c),b)

# print sim(b**Num(-2)/b**Num(-2))

# print expand(-a/(-b**Num(2)*c))
# print sim(-a/(-b**Num(2)*c))

# w = (c**(Num(-1)))**(Num(2)**Num(-1))
# w = (Num(-1)*(Num(2)**Num(-1)))

# # print type(w)
# # print w
# print simplify(w)

# q = [(Num(4)**Num(-1)), (pi**Num(-1)), (e_0**Num(-1))]
# q1 = [(pi**Num(-1)), (Num(4)**Num(-1)), (e_0**Num(-1))]
# print Mul(q)==Mul(q1)

# r = (((Num(4)*pi*e_0)**Num(-1))*q*((r**Num(2))**Num(-1)))+(-E)+(-(((Num(4)*pi*e_0)**Num(-1))*q*((r**Num(2))**Num(-1))))
# print r
# print sim(r)

