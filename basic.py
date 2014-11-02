# import operations

# def derivative(arg,var):
#     return operations.derivative(arg,var)

class Basic(object):
    def __add__ (self, other): return Add(self, other)
    def __radd__(self, other): return Add(other, self)

    def __mul__ (self, other): return Mul(self, other)
    def __rmul__(self, other): return Mul(other, self)

    def __sub__ (self, other): return Add(self,-other)
    def __rsub__(self, other): return Add(other,-self)

    def __div__ (self,other):  return (self*other**-1)
    def __rdiv__(self,other):  return (other*self**-1)

    def __neg__ (self):        return (-1*self)

    def __pow__ (self,other):  return Pow(self,other)
    def __rpow__(self,other):  return Pow(other,self)

    def sort(self):
        return self
    # def derivative(var):
    #     return 0

class Equation(object):
    
    pass

class Var(Basic):
    def __init__(self,name,units='',value='?'):
        self.name = name
        self.units = units
        self.value = value
    def __repr__(self):
        if self.value != '?':
            return str(self.value);
        return self.name
    def __eq__(self, other):
        return (type(self) == type(other) and self.name == other.name and
                self.units == other.units and self.value == other.value)
    # def derivative(self,var):
    #     if var==self:
    #         return 1
    #     else:
    #         return Symbol('(dy/dx)')

class Constant(Var):
    # def derivative(self,var):
    #     return 0
    pass

class Operator(Basic):
    def __init__(self, symbol, left, right):
        self.symbol = symbol
        self.left = left; self.right = right
    def __repr__(self):
        return '{0}{1}{2}'.format(self.left, self.symbol, self.right)
    def __eq__(self,other):
        return (type(self) == type(other) and self.symbol == other.symbol and
                self.left == other.left and self.right == other.right)
    def sort(self):
        left = self.left; right = self.right
        if issubclass(type(self.left),Basic):
            left = left.sort()
        if issubclass(type(self.right),Basic):
            right = right.sort()
        return type(self)(self.symbol,left,right)

class Pow(Operator):
    def __init__(self,base,power):
        Operator.__init__(self,'^',base,power)
    def __new__(self,*arg):
        if arg==():
            return super(Pow,self).__new__(self)

        base = arg[0]; power = arg[1]
        if power==0 or base==1: 
            return 1
        if power==1: 
            return base
        return super(Pow,self).__new__(self)
    # def derivative(self, var):
    #     from functions import log
    #     f = self.left; g = self.right
    #     return f**(g-1)*g*derivative(f,var=var)+f*log(f)*derivative(g,var=var)

class OperatorList(Basic):
    def __init__(self, symbol, elements, new = ''):
        if isinstance(elements,type(self)):
            arrayNew = elements.elements
        elif isinstance(elements,list):
            arrayNew = elements
        else:
            arrayNew = [elements]

        if new == '':
            pass
        elif isinstance(new,type(self)):
            arrayNew += new.elements
        elif isinstance(new,list):
            arrayNew += new
        else:
            arrayNew += [new]

        self.symbol = symbol
        self.elements = arrayNew
    def __eq__(self,other):
        return type(self)==type(other) and self.sort().elements == other.sort().elements

class Add(OperatorList):
    def __init__(self, old, new = 0):
        if new == 0: new = ''
        if old == 0: old = new; new =''
        OperatorList.__init__(self,'+',old,new)
    def __repr__(self):
        text = '('
        for i in self.elements:
            if i<0 and text[-1]=='+':
                text = text[0:-1]
            text += str(i) + self.symbol
        return text[0:-1]+')'
    # def derivative(self,var):
    #     return sum([derivative(i,var) for i in self.elements])

class Mul(OperatorList):
    def __init__(self, old, new = 1):
        if new == 1: new = ''
        if old == 1: old = new; new =''
        OperatorList.__init__(self,'*',old,new)
    def __new__(self,*arg):
        if arg==():
            return super(Mul,self).__new__(self)
        if arg[0]==0 or arg[1]==0:
            return 0
        return super(Mul,self).__new__(self)
    def __repr__(self):
        text = '-'
        for i in self.elements:
            if i<0:
                text = '-' + returnText; i = abs(i)
                if i==1: continue

            if text[-1].isdigit() and (isinstance(i,float) or isinstance(i,int)):
                text += '*' + str(i)
            else:
                text += str(i)
        return '(' + text[1:] + ')'
    # def derivative(self,var):
    #     return self[0]

# Add sort() for Add and Mul

# def derivative(arg, var=Var('x')):
#     if issubclass(type(arg),Basic):
#         return arg.derivative(var)
#     return 0


# class Test(object):
#     def __init__(self):
#         super(Test, self).__init__()
        