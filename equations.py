import basic
import functions
import operations

def solve(eqn,var):
	l = find(eqn.left,var)
	r = find(eqn.right,var)
	sumVar = (sum([l[3*i-1] for i in range(1,len(l)/3+1)])  
			+ sum([r[3*i-1] for i in range(1,len(r)/3+1)]))
	if sumVar == 1:
		return operations.simplify(oneVarSolve(eqn,var))

def oneVarSolve(eqn,var):
	right = eqn.right; left = eqn.left
	print '*',left,'=',right
	findVal = find(left,var)
	# print '*',type(left),left
	if len(findVal)==0:# or findVal[2]!=0:
		right -= left; left = basic.Num(0)
		item = find(right,var)[1]
		print right-item
		print '    ',operations.sim(right-item),'&'
		left -= item; right = operations.sim(right-item)
		print
	else:
		if type(left)==basic.Add:
			right = operations.sim(right-left); left = basic.Num(0)
			item = find(right,var)[1]
			left -= item; right = operations.sim(right-item)
		elif type(left)==basic.Mul:
			right = operations.sim(right/left); left = basic.Num(1)
			# print '--',right.elements
			item = find(right,var)[1]
			left = operations.sim(left/item); right = operations.sim(right/item)
		elif type(left)==basic.Pow:
			a = find(left,var)
			# print '+',a
			if a[0]==0:
				# print '==',(basic.Num(1)/left.right)
				# print '--',(operations.expand(right**(basic.Num(1)/left.right)))
				right = operations.sim(right**(basic.Num(1)/left.right)); left = left.left
			if a[0]==1:
				right = functions.log(right)/functions.log(left); left = right,left
		elif type(left)==functions.Function:
			print 'add for functions'
		elif left==var:
			return eqn
		else:
			'error type not found'
	# print '>',left,'=',right
	# return
	return oneVarSolve(basic.Equation(left,right),var)

def find(arg,var):
	listVars = []
	if issubclass(type(arg),basic.OperatorList):
		for i in arg.elements:
			temp = find(i,var)
			if len(temp)!=0:
				listVars+=[arg.elements.index(i),i,sum([temp[3*j-1] for j in range(1,len(temp)/3+1)])]
	if issubclass(type(arg),basic.Operator):
		l = find(arg.left,var); r = find(arg.right,var)
		if len(l)!=0:
			listVars+=[0,arg.left,sum([l[3*j-1] for j in range(1,len(l)/3+1)])]
		if len(r)!=0:
			listVars+=[1,arg.right,sum([r[3*j-1] for j in range(1,len(r)/3+1)])]
	if type(arg)==functions.Function:
		a = find(arg.arg,var)
		if len(a)!=0:
			listVars+=[0,arg.arg,sum([a[3*j-1] for j in range(1,len(a)/3+1)])]
	if type(arg)==basic.Var:
		if arg==var:
			listVars+=[0,arg,1]
	return listVars
