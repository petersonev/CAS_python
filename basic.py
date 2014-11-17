# from __future__ import absolute_import

# COMPLETED
# Basic
#   Creation, Addition/subtraction, multiplication/division, powers, negative
#   Sort placeholder
# Equation
#   Creation
# Var
#   Creation with name/units/value, equals
# Constant
#   Same as Var
# Operator
#   Creation, equals, sort
# Pow
#   Creation
#   Simplify to 1 or base upon creation
# OperatorList
#   Creation, equals
#   

class Basic(object):
    def __add__ (self, other): return Add(self, other)
    def __radd__(self, other): return Add(other, self)

    def __mul__ (self, other): return Mul(self, other)
    def __rmul__(self, other): return Mul(other, self)

    def __sub__ (self, other): return Add(self,-other)
    def __rsub__(self, other): return Add(other,-self)

    def __div__ (self,other):  return (self*other**Num(-1))
    def __rdiv__(self,other):  return (other*self**Num(-1))

    def __neg__ (self):        return (Num(-1)*self)

    def __pow__ (self,other):  return Pow(self,other)
    def __rpow__(self,other):  return Pow(other,self)

    def sort(self):
        return self

class Equation(object):
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def __repr__(self):
        return "{0}={1}".format(self.left,self.right)
    def __eq__(self):
        return 

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

class Num(Basic):
    import fractions

    def __init__(self,value):
        self.value = float(value)

    def __eq__(self,other):
        if type(self)==type(other):
            return self.value==other.value
        return self.value==other

    def __repr__(self):
        if self.value.is_integer():
            return str(int(self.value))
        return str(self.value)

class Constant(Var):

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
    def __new__(self,base,power):
        if power==0 or base==1: 
            return 1
        if power==1: 
            return base
        return Operator.__new__(self,'^',base,power)

class OperatorList(Basic):
    def __init__(self, symbol, elements, new = ''):
        self.elements = self.elements
        self.symbol = symbol
    def __new__(self,elements,new):

        if isinstance(elements,self):
            arrayNew = elements.elements
        elif isinstance(elements,list):
            arrayNew = elements
        else:
            arrayNew = [elements]

        if new == '':
            pass
        elif isinstance(new,self):
            arrayNew += new.elements
        elif isinstance(new,list):
            arrayNew += new
        else:
            arrayNew += [new]

        if len(arrayNew)==1:
            return arrayNew[0]
        self.elements = arrayNew

        return Basic.__new__(self)

    def __eq__(self,other):
        return type(self)==type(other) and self.sort().elements == other.sort().elements

class Add(OperatorList):
    def __init__(self, old, new = 0):
        OperatorList.__init__(self,'+',old,new)
    def __new__(self,old,new=0):
        if new == 0: new = ''
        if old == 0: old = new; new =''
        if old == []: return 0
        return OperatorList.__new__(self,old,new)
    def __repr__(self):
        text = '('
        for i in self.elements:
            if i<0 and text[-1]=='+':
                text = text[0:-1]
            text += str(i) + self.symbol
        return text[0:-1]+')'

class Mul(OperatorList):
    def __init__(self, old, new = 1): 
        OperatorList.__init__(self,'*',old,new)
    def __new__(self,old,new=1):
        if old==0 or new==0:
            return 0
        if new == 1: new = ''
        if old == 1: old = new; new =''
        if old == []: return 1
        return OperatorList.__new__(self,old,new)
    def __repr__(self):
        text = '-'
        for i in self.elements:
            if i<0:
                text = '-' + text; i = abs(i)
                if i==1: continue
            if text[-1].isdigit() and str(i)[0].isdigit():
                text += '*' + str(i)
            else:
                text += str(i)
        return '(' + text[1:] + ')'
        
