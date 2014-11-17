import basic
import functions

def der_Basic(var):

	return Num(0)

def der_Var(self,var):
    if var==self:
        return Num(1)
    else:
        return basic.Var('(dy/dx)')

def der_Constant(self,var):
	
	return Num(0)

def der_Pow(self, var):
    from functions import log
    f = self.left; g = self.right
    return f**(g-Num(1))*g*derivative(f,var=var)+f**g*functions.log(f)*derivative(g,var=var)

def der_Add(self,var):

    return sum([derivative(i,var) for i in self.elements])

def der_Mul(self,var):
    f = basic.Mul(self.elements[0]); g = basic.Mul(self.elements[1:])
    return f*derivative(g)+g*derivative(f)

def der_Equation(self,var):
    return basic.Equation(derivative(self.left),derivative(self.right))

basic.Basic.derivative = der_Basic
basic.Var.derivative = der_Var
basic.Constant.derivative = der_Constant
basic.Pow.derivative = der_Pow
basic.Add.derivative = der_Add
basic.Mul.derivative = der_Mul
basic.Equation.derivative = der_Equation


def der_log(self,var):
    
    return derivative(self.arg)/self.arg

def der_sin(self,var):

    return derivative(self.arg)*functions.cos(self.arg)

def der_cos(self,var):

    return -derivative(self.arg)*functions.sin(self.arg)

functions.log.derivative = der_log
functions.sin.derivative = der_sin
functions.cos.derivative = der_cos


def derivative(arg, var=basic.Var('x')):
    if issubclass(type(arg),basic.Basic):
        return arg.derivative(var)
    return Num(0)