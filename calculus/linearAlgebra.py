import basic

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
	def __init__(self,*args):
		self.elements = [i for i in args]
		# self.size = [len(args),len(args[0])]
	def __new__(self,*args):
		if len(args)==1:
			return Vector(*args[0])
		for i in args:
			if len(i)!=len(args[0]): raise SyntaxError

		if len(args[0])==1:
			a = Vector(*(i[0] for i in args))
			a.vertical = True; return a
		return object.__new__(self)

	def __add__ (self,other): return matAdd(self,other)
	def __radd__(self,other): return matAdd(other,self)

	def __mul__ (self,other): return matMul(self,other)
	def __rmul__(self,other): return matMul(other,self)

	def __sub__ (self, other): return matAdd(self,-other)
	def __rsub__(self, other): return matAdd(other,-self)

	def __div__ (self,other):  return (self*other**-1)
	def __rdiv__(self,other):  return (other*self**-1)

	def __neg__ (self):        return (-1*self)

	def __pow__ (self,other):
		if other<0:
			return (matInverse(self))**(abs(other))
		final = identityMatrix(self.size()[0])
		if other==1:
			return self
		for i in range(other):
			final = final*self
		return final

	# Add powers?

	def augment(self,other):
		if self.size()[0]!=other.size()[0]:
			raise
		for i in range(self.size()[0]):
			self.elements[i] += other.elements[i]
		return self

	def row(self,num):
		return Vector(*self.elements[num-1])

	def col(self,num):
		a = Vector(*(i[num-1] for i in self.elements))
		a.vertical = True; return a

	def pos(self,n,m):
		return self.elements[n-1][m-1]

	def size(self):
		if self.elements == []:
			return [0,0]
		return [len(self.elements),len(self.elements[0])]

	def ref(self):
		# cycle through pivot colums
		# move row with pivot position to top
			# if no col with pivot position move to next col
		# change all rows below so pos's below pivot pos are 0

		# move to next row and next col

		new = []
		old = self # copy
		for i in range(old.size()[1]):
			for j in range(0,old.size()[0]): # + 1?
				if old.elements != [] and old.pos(j+1,i+1) != 0:
					new += old.row(j+1).elements
					old.elements.remove(old.elements[j])
					for k in range(0,old.size()[0]):
						if old.pos(k+1,i+1) != 0:
							mul = 1.*old.pos(k+1,i+1)/new[-1][i]
							old.elements[k] = (old.row(k+1) - Matrix(new[-1])*mul).elements[0]
							# old.elements[k] = [0,1]

					break
		return Matrix(*(new+old.elements))

	def rref(self):
		# start with last row, loop through each row moving up
		# find pivot col in that row
		# divide row by pivot pos
		# loop through each row add -pivot pos * pivot row 

		old = self.ref()

		for i in range(old.size()[0]-1,-1,-1):
			pivot = -1;
			for j in range(old.size()[1]):
				if old.pos(i+1,j+1)!=0:
					pivot = j; break
			if pivot==-1:
				continue
			old.elements[i] = (old.row(i+1)/old.pos(i+1,pivot+1)).elements[0]
			for k in range(i):
				old.elements[k] = (old.row(k+1) - old.pos(k+1,pivot+1)*old.row(i+1)).elements[0]

		return old

	def det(self):
		# same as ref() plust tracking det
		# det*-1 when flipped row
		det = 1

		new = []
		old = self # copy
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


	def __repr__(self):
		return '['+'\n '.join([str(i)[1:-1] for i in self.elements]) +']'

class Vector(object):
	def __init__(self,*elements):
		self.elements = [[i for i in elements]]
		self.size = [1,1]
		self.vertical = False

	def __add__ (self,other): return matAdd(self,other)
	def __radd__(self,other): return matAdd(other,self)

	def __mul__ (self,other): return matMul(self,other)
	def __rmul__(self,other): return matMul(other,self)

	def __sub__ (self, other): return matAdd(self,-other)
	def __rsub__(self, other): return matAdd(other,-self)

	def __div__ (self,other):  return (self*other**-1)
	def __rdiv__(self,other):  return (other*self**-1)

	def __neg__ (self):        return (-1*self)

	def dot(self,other):
		if not (isinstance(self,Vector) and isinstance(other,Vector)) or self.size != other.size:
			raise
		return sum([[x*y for x,y in zip(self.elements[i],other.elements[i])] 
						for i in range(len(self.elements))][0])

	def mag(self):
		total = 0;
		for i in self.elements[0]:
			total+=i**2
		return (total)**(1./2)

	def norm(self):
		return self*self.mag()**-1

	def col(self,num):
		return Vector(*self.elements[0])
	def row(self,num):
		return Vector(*self.elements[0])

	def __repr__(self):
		if self.vertical:
			return '('+'\n '.join([str(i) for i in self.elements[0]]) +')'
		return '(' + str(self.elements[0])[1:-1] +')'

def matAdd(self,other):
	if not (isinstance(self,(Matrix,Vector)) and isinstance(other,(Matrix,Vector))) or self.size != other.size:
		raise
	return Matrix(*([x+y for x,y in zip(self.elements[i],other.elements[i])] 
					for i in range(len(self.elements))))

def matMul(self,other):
	if isinstance(other,(int, long, float, basic.Basic)):
		return Matrix(*([y*other for y in self.elements[i]] for i in range(len(self.elements))))
	elif isinstance(self,(int, long, float, basic.Basic)):
		return matMul(other,self)

	if self.size[1]!=other.size[0] and other.size[0]!=1:
		raise SyntaxError

	return Matrix(*[[self.row(i+1).dot(other.col(j+1)) for j in range(other.size[1])] for i in range(self.size[0])])

def matInverse(self):
	# if self.det()==0:
	# 	return
	self = self.augment(identityMatrix(3)).rref()
	for i in range(self.size()[0]):
		self.elements[i] = self.elements[i][self.size()[0]:]
	return self

def zerosMatrix(n,m):

	return Matrix(*tuple([[0]*(n)])*m)

def identityMatrix(n):
	return Matrix(*([0]*(i)+[1]+[0]*(n-i-1) for i in range(n)))