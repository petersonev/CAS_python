import basic
import functions

def expand(arg):
	if isinstance(arg,basic.Mul):
		old = copy(arg).elements; new = []
		while len(old)>0:
			i = old[0]
			if isinstance(i,basic.Add):
				old = old[1:]
				return basic.Add([expand(basic.Mul(new+[j]+old)) for j in i.elements])
			else:
				new += [i]; old = old[1:]
		return basic.Mul(new)
	elif isinstance(arg,basic.Pow):
		if isinstance(arg.left,basic.Add) and isinstance(arg.right,basic.Num) and arg.right.value.is_integer():
			return expand(basic.Mul([arg.left]*arg.right))
		elif isinstance(arg.left,basic.Mul):
			return basic.Mul([expand(i**arg.right) for i in arg.left.elements])
	elif isinstance(arg,basic.Equation):
		return basic.Equation(expand(arg.left),expand(arg.right))
	# add expand for functions
	return arg

def sim_Basic(self):
	
	return self

def sim_Pow(self):
	base = simplify(self.left); exp = simplify(self.right)
	if isinstance(base,basic.Pow):
		exp = exp*base.right; base = base.left
	elif isinstance(base,basic.Num) and isinstance(exp,basic.Num) and exp.value.is_integer() and exp.value>=0:
		return basic.Num(base.value**exp.value)	# change so only happense when exp is integer and positive
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
		if isinstance(i, basic.Num):
			mult *= i.value
		else:
			new += [i] # potentially add recursion here to make copy
	return basic.Num(mult),basic.Mul(new)

def sim_Add(self):
	array = [simplify(i) for i in self.elements]; arrayNew = []
	while len(array)>0:
		i = array[0]
		if isinstance(i,basic.Add):
			array = i.elements+array[1:]; continue
		mult_i,new_i = multexpand(i)
		done = False
		for j in arrayNew:
			if isinstance(i,basic.Num) and isinstance(j,basic.Num):
				arrayNew[arrayNew.index(j)] = basic.Num(i.value+j.value)
				done = True; break

			mult_j,new_j = multexpand(j)
			if sort(expand(new_i))==sort(expand(new_j)):
				if mult_i+mult_j!=0:
					arrayNew[arrayNew.index(j)] = (mult_i+mult_j)*new_j # simplify?
				else:
					arrayNew.remove(j) 
				done = True; break
		if not done: # and i!=0  ?
			arrayNew += [i]
		array = array[1:]
	if len(arrayNew)==0: return Num(0)
	return basic.Add(arrayNew)

def powexpand(arg):
	if isinstance(arg,basic.Pow):
		return arg.left,arg.right
	return arg,basic.Num(1)

def sim_Mul(self):
	array = [simplify(i) for i in self.elements]; arrayNew = []
	while len(array)>0:
		i = array[0]
		if isinstance(i,basic.Mul):
			array = i.elements+array[1:]; continue
		base_i,exp_i = powexpand(i)
		mult_i,new_i = multexpand(base_i)
		done = False
		if i==1:
			array = array[1:]; continue
		for j in arrayNew:
			if isinstance(i,basic.Num) and isinstance(j,basic.Num):
				arrayNew[arrayNew.index(j)] = basic.Num(i.value*j.value)
				done = True; break

			base_j,exp_j = powexpand(j)
			mult_j,new_j = multexpand(base_j)
			if sort(expand(new_i)) == sort(expand(new_j)):
				if exp_i+exp_j!=0:
					if new_i==1 and mult_i==mult_j:
						new_i = mult_i; mult_i=1;mult_j=1
					new = simplify((mult_i**exp_i*mult_j**exp_j)*new_i**(exp_i+exp_j))
					if new==1:
						arrayNew.remove(j)
					elif new==0:
						return Num(0)
					# elif isinstance(new.left,basic.Num) and isinstance(new.right,basic.Num):
					# 	arrayNew[arrayNew.index(j)] = New(new.left.value**new.right.value)
					else:
						arrayNew[arrayNew.index(j)] = new
				else:
					arrayNew.remove(j)
				done = True; break
		if not done: # and i!=0  ?
			arrayNew += [i]
		array = array[1:]
	if len(arrayNew)==0: return Num(1)
	return basic.Mul(arrayNew)

# def sim_Equation(self):
# 	left = simplify(self.left); right = simplify(self.right)
# 	if isinstance(left,basic.Mul) and isinstance(right,basic.Mul):
# 		i1 = 0;
# 		while i1<len(right.elements):
# 			i = right.elements[i1]
# 			simplified = simplify(left/i)
# 			print sort(simplified),'--',sort(left*simplify(i**-1))
# 			if not sort(simplified)==sort(left*simplify(i**-1)):
# 				left = simplified; right.elements.remove(i)
# 			else:
# 				i1+=1
# 		return basic.Equation(left,right)
# 	print left,'-',right
# 	pass

def sim_Equation(self):
	left = simplify(self.left); right = simplify(self.right)
 	if not (isinstance(left,basic.Add) or isinstance(left,basic.Add)):
 		i1 = 0
 		if isinstance(left,basic.Mul):
 			list_i = left.elements
 		else:
 			list_i = [left]
 		if isinstance(right,basic.Mul):
	 			list_j = right.elements
 		else:
 			list_j = [right]
 		while len(list_i)>i1:
 			i=list_i[i1]
 			base_i,exp_i = powexpand(i)
			mult_i,new_i = multexpand(base_i)
 			j1 = 0
 			
 			while len(list_j)>j1:
 				j=list_j[j1]
 				base_j,exp_j = powexpand(j)
				mult_j,new_j = multexpand(base_j)
				# print new_i,new_j
				if new_i==1 and new_j==1 and exp_j==exp_i:
					list_i[i1]=i/j
					# print list_j
					list_j.remove(j)
					# print list_j,'-'
				elif new_i==new_j and new_i!=1 and new_j!=1:
					# print i,'-',j
					list_i[i1]=i/j
					list_j.remove(j)
				# print list_i,'=',list_j
				j1+=1
			i1+=1
		return basic.Equation(simplify(simplify(basic.Mul(list_i))),simplify(basic.Mul(list_j)))



basic.Basic.simplify = sim_Basic
basic.Var.simplify = sim_Basic
basic.Constant.simplify = sim_Basic
basic.Pow.simplify = sim_Pow
basic.Add.simplify = sim_Add
basic.Mul.simplify = sim_Mul
basic.Equation.simplify = sim_Equation

def simplify(arg):
	if issubclass(type(arg),basic.Basic) or isinstance(arg,basic.Equation):
		return arg.simplify()
	return arg

def sort(arg):
	if isinstance(arg,basic.Pow):
		return sort(arg.left)**sort(arg.right)
	elif isinstance(arg,(basic.Add,basic.Mul)):
		return type(arg)(sorted([sort(i) for i in arg.elements]))
	elif isinstance(arg,basic.Equation):
		return basic.Equation(sort(arg.left),sort(arg.right))
	elif isinstance(arg,functions.Function):
		return type(arg)(sort(arg.arg))
	return arg

def copy(arg):
	if issubclass(type(arg),basic.OperatorList):
		return type(arg)([copy(i) for i in arg.elements])
	if issubclass(type(arg),basic.Operator):
		return type(arg)(copy(arg.left),copy(arg.right))
	return arg

def sim(arg):
	
	return sort(simplify(expand(arg)))

# def combine(arg):
# 	if isinstance(arg,Mul):


# Combine functions
# Multiplication
# 	functions ex: (sin/cos = tan)
# 	exponents ex: (3^x*4^x = (3/4)^x)
# Addition
#	Factorization ex: (x + x^2 = x(x+1)) (x^2 + 2x + 1 = (x+1)*(x+1) = (x+1)^2), x(x+1) + (x+1) = (x+1)(x+1)

def evaluate(expr,*args):
	# copy?
	for i in args:
		exec(i)

	if isinstance(expr,basic.Var):
		try: eval(expr.name)
		except (NameError): return expr
		else: return eval(expr.name)   
	elif isinstance(expr,basic.OperatorList):
		return type(expr)([evaluate(i,*args) for i in expr.elements])
	elif isinstance(expr,(basic.Operator,basic.Equation)):
		return type(expr)(evaluate(expr.left,*args),evaluate(expr.right,*args))
	elif isinstance(expr,functions.Function):
		return expr.evaluate()
	elif isinstance(expr,basic.Num):
		return expr.value
	return expr



