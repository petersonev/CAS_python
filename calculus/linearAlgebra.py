import basic
import operations

# COMPLETED
# Matrix
# 	Creation, addition, multiplication, positive powers, row echelon, reduced row echelon
# 	Access row/col/pos/size, division by constants
# 	Zeros matrix, identity matrix
# 	Augment, inverse
# Vector
# 	Creation, addition, multiplication, dot product
# 	Return magnitude/normal vector

# TODO
# Matrix
# 	Solve, return vector form
# Fix long rounding
# Whatever the hell we are doing now in calc

class Matrix(object):
	def __init__(cls,*args):
		args = basic.toNum(*args)
		cls.elements = [i for i in args]
		# cls.size = [len(args),len(args[0])]
	def __new__(cls,*args):
		args = basic.toNum(*args)
		if len(args)==1:
			return Vector(*args[0])
		for i in args:
			if len(i)!=len(args[0]): raise SyntaxError

		if len(args[0])==1:
			a = Vector(*(i[0] for i in args))
			a.vertical = True; return a
		return object.__new__(cls)

	def __add__ (cls,other): return matAdd(cls,other)
	def __radd__(cls,other): return matAdd(other,cls)

	def __mul__ (cls,other): return matMul(cls,other)
	def __rmul__(cls,other): return matMul(other,cls)

	def __sub__ (cls, other): return matAdd(cls,-other)
	def __rsub__(cls, other): return matAdd(other,-cls)

	def __div__ (cls,other):  return (cls*other**basic.Num(-1))
	def __rdiv__(cls,other):  return (other*cls**basic.Num(-1))

	def __neg__ (cls):        return (cls*basic.Num(-1))

	def __pow__ (cls,other):
		if other<0:
			return (matInverse(cls))
		final = identityMatrix(cls.size()[0])
		if other==1:
			return cls
		for i in range(other):
			final = final*cls
		return final

	# Add powers?

	def augment(cls,other):
		# print cls
		# print other
		new = cls.copy()
		if new.size()[0]!=other.size()[0]:
			raise SizeError
		for i in range(cls.size()[0]):
			new.elements[i] += other.elements[i]
		return new

	def row(cls,num):
		return Vector(*cls.elements[num-1])

	def col(cls,num):
		a = Vector(*(i[num-1] for i in cls.elements))
		a.vertical = True; return a

	def pos(cls,n,m):
		return cls.elements[n-1][m-1]

	def size(cls):
		if cls.elements == []:
			return [0,0]
		return [len(cls.elements),len(cls.elements[0])]

	def ref(cls):
		# cycle through pivot colums
		# move row with pivot position to top
			# if no col with pivot position move to next col
		# change all rows below so pos's below pivot pos are 0

		# move to next row and next col

		new = []
		old = cls.copy() # copy
		for i in range(old.size()[1]):
			for j in range(0,old.size()[0]): # + 1?
				if old.elements != [] and old.pos(j+1,i+1) != 0:
					new += old.row(j+1).elements
					old.elements.remove(old.elements[j])
					for k in range(0,old.size()[0]):
						if old.pos(k+1,i+1) != 0:
							mul = old.pos(k+1,i+1)/new[-1][i]
							# print old.row(k+1)
							# print (Matrix(new[-1])*mul).simplify().simplify()
							# print old.row(k+1) - Matrix(new[-1])*mul
							print old.elements[k],i,j,k
							old.elements[k] = (old.row(k+1) - (Matrix(new[-1])*mul)).elements[0]
							print '-',old.elements[k]
							# old.elements[k] = [0,1]

					break
		return Matrix(*(new+old.elements))

	def rref(cls):
		# start with last row, loop through each row moving up
		# find pivot col in that row
		# divide row by pivot pos
		# loop through each row add -pivot pos * pivot row 

		old = cls.ref()

		for i in range(old.size()[0]-1,-1,-1):
			pivot = -1;
			for j in range(old.size()[1]):
				if old.pos(i+1,j+1)!=0:
					pivot = j; break
			if pivot==-1:
				continue
			old.elements[i] = (old.row(i+1)/old.pos(i+1,pivot+1)).simplify().elements[0]
			for k in range(i):
				# print old.row(k+1),'---'
				# print type(old.pos(k+1,pivot+1));print
				old.elements[k] = ((old.row(k+1) - old.row(i+1)*old.pos(k+1,pivot+1)).simplify().elements[0])

		return old

	def det(cls):
		# same as ref() plust tracking det
		# det*-1 when flipped row
		det = 1

		new = []
		old = cls.copy() # copy
		for i in range(old.size()[1]):
			for j in range(0,old.size()[0]): # + 1?
				if old.elements != [] and old.pos(j+1,i+1) != 0:
					if j!=0:
						det*=-1
					new += old.row(j+1).elements
					old.elements.remove(old.elements[j])
					for k in range(0,old.size()[0]):
						if old.pos(k+1,i+1) != 0:
							mul = 1.*old.pos(k+1,i+1)/new[-1][i]
							old.elements[k] = (old.row(k+1) - Matrix(new[-1])*mul).elements[0]
							# old.elements[k] = [0,1]

					break

		a = Matrix(*(new+old.elements))
		for i in range(a.size()[0]):
			det*=a.pos(i,i)
		return det

	def simplify(cls):
		return Matrix(*[[i.simplify() for i in j] for j in cls.copy().elements])

	def copy(cls):
		return Matrix(*[[i.copy() for i in j] for j in cls.elements])

	def __repr__(cls):
		return '['+'\n '.join([str(i)[1:-1] for i in cls.elements]) +']'

class Vector(object):
	def __init__(cls,*elements):
		elements = basic.toNum(*elements)
		cls.elements = [[i for i in elements]]
		cls.vertical = False

	def __add__ (cls,other): return matAdd(cls,other)
	def __radd__(cls,other): return matAdd(other,cls)

	def __mul__ (cls,other): return matMul(cls,other)
	def __rmul__(cls,other): return matMul(other,cls)

	def __sub__ (cls, other): 
		# print type(other)
		return matAdd(cls,-other)
	def __rsub__(cls, other): return matAdd(other,-cls)

	def __div__ (cls,other):  return (cls*other**basic.Num(-1))
	def __rdiv__(cls,other):  return (other*cls**basic.Num(-1))

	def __neg__ (cls):        return matMul(cls,basic.Num(-1))

	def dot(cls,other):
		if not (isinstance(cls,Vector) and isinstance(other,Vector)) or cls.size() != other.size():
			raise
		# print zip(cls.elements,other.elements)
		# print [y*x for x,y in zip(cls.elements[0],other.elements[0])] 
		# print
		new = cls.copy()
		return sum([[x*y for x,y in zip(new.elements[i],other.elements[i])] 
						for i in range(len(new.elements))][0])

	def mag(cls):
		total = 0;
		for i in cls.elements[0]:
			total+=i**2
		return (total)**(1./2)

	def norm(cls):
		return cls*cls.mag()**-1

	def col(cls,num):
		return Vector(*cls.elements[0])
	def row(cls,num):
		return Vector(*cls.elements[0])

	def size(cls):
		return [1,1]

	def simplify(cls):
		return Matrix(*[[i.simplify() for i in j] for j in cls.copy().elements])

	def copy(cls):
		return Matrix(*[[i.copy() for i in j] for j in cls.elements])

	def __repr__(cls):
		if cls.vertical:
			return '('+'\n '.join([str(i) for i in cls.elements[0]]) +')'
		return '(' + str(cls.elements[0])[1:-1] +')'

def matAdd(self,other):
	# print type(other),other.elements
	if not (isinstance(self,(Matrix,Vector)) and isinstance(other,(Matrix,Vector))) or self.size() != other.size():
		raise
	return Matrix(*([x+y for x,y in zip(self.copy().elements[i],other.copy().elements[i])] 
					for i in range(len(self.copy().elements))))

def matMul(self,other):
	if isinstance(other,(basic.Basic)):
		return Matrix(*([y*other for y in self.elements[i]] for i in range(len(self.elements))))
	elif isinstance(self,(basic.Basic)):
		return matMul(other,self)

	# print self.size()
	# print other
	if self.size()[1]!=other.size()[0] and other.size()[0]!=1:
		raise SyntaxError
	return Matrix(*[[self.copy().row(i+1).dot(other.copy().col(j+1)) for j in range(other.size()[1])] for i in range(self.size()[0])])

def matInverse(self):
	# if self.det()==0:
	# 	return
	self = self.copy().augment(identityMatrix(self.size()[0])).rref()
	for i in range(self.size()[0]):
		self.elements[i] = self.elements[i][self.size()[0]:]
	return self

def zerosMatrix(n,m):

	return Matrix(*tuple([[basic.Num(0)]*(n)])*m)

def identityMatrix(n):
	return Matrix(*([basic.Num(0)]*(i)+[basic.Num(1)]+[basic.Num(0)]*(n-i-1) for i in range(n)))

