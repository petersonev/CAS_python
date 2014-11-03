import basic
import functions

def expand(arg):
	# mul of add
	# mul to pow
	# add to pow
	pass

def sim_Basic(self):
	return self

def sim_Pow(self):
	base = simplify(self.left); exp = simplify(self.right)

	if isinstance(type(base),basic.Pow):
		exp = exp*base.right; base = base.left
	else:
		return base**exp
	return simplify(base)**simplify(exp)

def multexpand(arg):
	mult = 1; new = []
	if isinstance(arg,basic.Mul):
		arg = arg.elements
	else:
		arg = [arg]
	for i in arg:
		if isinstance(i, (int, long, float)):
			mult *= i
		else:
			new += [i] # potentially add recursion here to make copy
	return mult,basic.Mul(new)

def sim_Add(self):
	array = [simplify(i) for i in self.elements]; arrayNew = []
	while len(array)>0:
		i = array[0]
		if isinstance(i,basic.Add):
			array = i.elements+array[1:]; continue
		mult_i,new_i = multexpand(i)
		done = False
		for j in arrayNew:
			mult_j,new_j = multexpand(j)
			if sort(new_i)==sort(new_j):
				if mult_i-mult_j!=0:
					arrayNew[arrayNew.index(j)] = (mult_i+mult_j)*new_j # simplify?
				else:
					arrayNew.remove(j) 
				done = True; break
		if not done: # and i!=0  ?
			arrayNew += [i]
		array = array[1:]
	if len(arrayNew)==0: return 0
	return basic.Add(arrayNew)

def powexpand(arg):
	if isinstance(arg,basic.Pow):
		return arg.left,arg.right
	return arg,1

def sim_Mul(arg):
	array = [simplify(i) for i in arg.elements]; arrayNew = []
	while len(array)>0:
		i = array[0]
		if isinstance(i,basic.Mul):
			array = i.elements+array[1:]; continue
		base_i,exp_i = powexpand(i)
		done = False
		for j in arrayNew:
			base_j,exp_j = powexpand(j)
			mult_i,new_i = multexpand(base_i); mult_j,new_j = multexpand(base_j)
			if sort(new_i) == sort(new_j):
				if exp_i+exp_j!=0:
					if new_i==1 and mult_i==mult_j:
						new_i = mult_i; mult_i=1;mult_j=1
					arrayNew[arrayNew.index(j)] = (mult_i**exp_i*mult_j**exp_j)*new_i**(exp_i+exp_j)
				else:
					arrayNew.remove(j)
				done = True; break
		if not done: # and i!=0  ?
			arrayNew += [i]
		array = array[1:]
	if len(arrayNew)==0: return 1
	return basic.Mul(arrayNew)

basic.Basic.simplify = sim_Basic
basic.Var.simplify = sim_Basic
basic.Constant.simplify = sim_Basic
basic.Pow.simplify = sim_Pow
basic.Add.simplify = sim_Add
basic.Mul.simplify = sim_Mul
# basic.Equation.simplify = 

def simplify(arg):
	if issubclass(type(arg),basic.Basic):
		return arg.simplify()
	return arg

def sort(arg):
	if isinstance(arg,basic.Pow):
		return sort(arg.left)**sort(arg.right)
	elif isinstance(arg,(basic.Add,basic.Mul)):
		return type(arg)(sorted([sort(i) for i in arg.elements]))
	elif isinstance(arg,basic.Equation):
		return Equation(sort(arg.left),sort(arg.right))
	elif isinstance(arg,functions.Function):
		return type(arg)(sort(arg.arg))
	return arg