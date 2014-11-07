import basic

class Matrix(object):
	def __init__(self,*args):
		self.elements = [i for i in args]
		self.size = [len(args),len(args[0])]
	def __new__(self,*args):
		if len(args)==1:
			return Vector(*args[0])
		for i in args:
			if len(i)!=len(args[0]): raise SyntaxError
		if len(args[0])==1:
			return Vector(*(i[0] for i in args))
		return object.__new__(self)

	def __add__ (self,other): return matAdd(self,other)
	def __radd__(self,other): return matAdd(other,self)

	def __mul__ (self,other): return matMul(self,other)
	def __rmul__(self,other): return matMul(other,self)

	# Add powers?
	def row(self,num):
		return Vector(*self.elements[num])

	def col(self,num):
		return Vector(*(i[num] for i in self.elements))

	def __repr__(self):
		return '['+'\n '.join([str(i) for i in self.elements]) +']'

def matAdd(self,other):
	if not (isinstance(self,(Matrix,Vector)) and isinstance(other,(Matrix,Vector))) or self.size != other.size:
		raise
	return Matrix(*([x+y for x,y in zip(self.elements[i],other.elements[i])] 
					for i in range(len(self.elements))))

def dot(self,other):
	if not (isinstance(self,Vector) and isinstance(other,Vector)) or self.size != other.size:
		raise
	return sum([[x*y for x,y in zip(self.elements[i],other.elements[i])] 
					for i in range(len(self.elements))][0])

def matMul(self,other):
	if isinstance(other,(int, long, float, basic.Basic)):
		return Matrix(*([y*other for y in self.elements[i]] for i in range(len(self.elements))))
	elif isinstance(self,(int, long, float, basic.Basic)):
		return matMul(other,self)

	if self.size[1]!=other.size[0] and other.size[0]!=1:
		raise SyntaxError

	return Matrix(*[[self.row(i).dot(other.col(j)) for j in range(other.size[1])] for i in range(self.size[0])])

class Vector(object):
	def __init__(self,*elements):
		self.elements = [[i for i in elements]]
		self.size = [1,1]

	def __add__ (self,other): return matAdd(self,other)
	def __radd__(self,other): return matAdd(other,self)

	def dot(self,other):
		return dot(self,other)

	def col(self,num):
		return Vector(*self.elements[0])
	def row(self,num):
		return Vector(*self.elements[0])

	def __repr__(self):
		return str(self.elements[0])