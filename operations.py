import basic
import functions

def der_Basic(var):

	return 0

def der_Var(self,var):
    if var==self:
        return 1
    else:
        return basic.Var('(dy/dx)')

def der_Constant(self,var):
	
	return 0

def der_Pow(self, var):
    from functions import log
    f = self.left; g = self.right
    return f**(g-1)*g*derivative(f,var=var)+f*functions.log(f)*derivative(g,var=var)

def der_Add(self,var):

    return sum([derivative(i,var) for i in self.elements])

def der_Mul(self,var):
    
    return self[0]

basic.Basic.derivative = der_Basic
basic.Var.derivative = der_Var
basic.Constant.derivative = der_Constant
basic.Pow.derivative = der_Pow
basic.Add.derivative = der_Add
basic.Mul.derivative = der_Mul


def der_log(self,var):
    
    return 1/self.arg

functions.log.derivative = der_log


def derivative(arg, var=basic.Var('x')):
    if issubclass(type(arg),basic.Basic):
        return arg.derivative(var)
    return 0