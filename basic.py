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
    def __add__ (cls, other): return Add(cls, other)
    def __radd__(cls, other): return Add(other, cls)

    def __mul__ (cls, other): return Mul(cls, other)
    def __rmul__(cls, other): return Mul(other, cls)

    def __sub__ (cls, other): return Add(cls,-other)
    def __rsub__(cls, other): return Add(other,-cls)

    def __div__ (cls,other):  return (cls*other**Num(-1))
    def __rdiv__(cls,other):  return (other*cls**Num(-1))

    def __neg__ (cls):        return (Num(-1)*cls)

    def __pow__ (cls,other):  return Pow(cls,other)
    def __rpow__(cls,other):  return Pow(other,cls)

    def sort(cls):
        return cls

class Equation(object):
    def __init__(cls,left,right):
        left,right = toNum(left,right)
        cls.left = left
        cls.right = right
    def __repr__(cls):
        return "{0}={1}".format(cls.left,cls.right)
    def __eq__(cls):
        return 
    def copy(cls):
        return Equation(cls.left.copy(),cls.right.copy())

class Var(Basic):
    def __init__(cls,name,units='',value='?'):
        cls.name = name
        cls.units = units
        cls.value = value
    def __repr__(cls):
        if cls.value != '?':
            return str(cls.value);
        return cls.name
    def __eq__(cls, other):
        return (type(cls) == type(other) and cls.name == other.name and
                cls.units == other.units and cls.value == other.value)
    def copy(cls):
        return Var(cls.name,cls.units,cls.value)

class Num(Basic):
    # import fractions

    def __init__(cls,value):
        cls.value = float(value)

    # def __eq__(cls,other):
    #     if type(cls)==type(other):
    #         return cls.value==other.value
    #     return cls.value==other

    def __eq__(cls,other): return cls.value==other
    def __ne__(cls,other): return cls.value!=other
    def __lt__(cls,other): return cls.value<other
    def __le__(cls,other): return cls.value<=other
    def __gt__(cls,other): return cls.value>other
    def __ge__(cls,other): return cls.value>=other

    def __repr__(cls):
        if cls.value.is_integer():
            return str(int(cls.value))
        return str(cls.value)

    def copy(cls):
        return Num(cls.value)

class Constant(Var):

    pass

class Operator(Basic):
    def __init__(cls, symbol, left, right):
        left,right=toNum(left,right)
        cls.symbol = symbol
        cls.left = left; cls.right = right
    def __repr__(cls):
        return '({0}{1}{2})'.format(cls.left, cls.symbol, cls.right)
    def __eq__(cls,other):
        return (type(cls) == type(other) and cls.symbol == other.symbol and
                cls.left == other.left and cls.right == other.right)
    # def sort(cls):
    #     left = cls.left; right = cls.right
    #     if issubclass(type(cls.left),Basic):
    #         left = left.sort()
    #     if issubclass(type(cls.right),Basic):
    #         right = right.sort()
    #     return type(cls)(cls.symbol,left,right)
    def copy(cls):
        return type(cls)(cls.left.copy(),cls.right.copy())

class Pow(Operator):
    def __init__(cls,base,power):
        Operator.__init__(cls,'^',base,power)
    def __new__(cls,base,power):
        base,power = toNum(base,power)
        # print base,type(base),power,type(power)
        if power==0 or base==1: 
            return Num(1)
        if power ==-1:
            if base==1:
                return Num(1)
            elif base==-1:
                return Num(-1)
        if power==1: 
            return base
        return Operator.__new__(cls,'^',base,power)

class OperatorList(Basic):
    def __init__(cls, symbol, elements, new = ''):
        cls.elements = cls.elements
        cls.symbol = symbol
    def __new__(cls,elements,new):

        if isinstance(elements,cls):
            arrayNew = elements.elements
        elif isinstance(elements,list):
            arrayNew = elements
        else:
            arrayNew = [elements]

        if new == '':
            pass
        elif isinstance(new,cls):
            arrayNew += new.elements
        elif isinstance(new,list):
            arrayNew += new
        else:
            arrayNew += [new]

        if len(arrayNew)==1:
            return arrayNew[0]
        cls.elements = arrayNew

        return Basic.__new__(cls)

    def __eq__(cls,other):
        # return type(cls)==type(other) and cls.sort().elements == other.sort().elements
        return type(cls)==type(other) and compareList(cls.elements,other.elements)

    def copy(cls):
        return type(cls)([i.copy() for i in cls.elements])

class Add(OperatorList):
    def __init__(cls, old, new = 0):
        OperatorList.__init__(cls,'+',old,new)
    def __new__(cls,old,new=0):
        old,new = toNum(old,new)
        if new == 0: new = ''
        if old == 0 and new!='': old = new; new =''
        # if old == []: return Num(0)
        return OperatorList.__new__(cls,old,new)
    def __repr__(cls):
        text = '('
        for i in cls.elements:
            if i<0 and text[-1]=='+':
                text = text[0:-1]
            text += str(i) + cls.symbol
        return text[0:-1]+')'

class Mul(OperatorList):
    def __init__(cls, old, new = 1): 
        OperatorList.__init__(cls,'*',old,new)
    def __new__(cls,old,new=1):
        old,new = toNum(old,new)
        if old==0 or new==0:
            return Num(0)
        if new == 1: new = ''
        if old == 1 and new!='': old = new; new =''
        # if old == []: return Num(1)
        return OperatorList.__new__(cls,old,new)
    def __repr__(cls):
        text = ''
        for i in cls.elements:
            # print i,i<0,type(i)
            # print i,text,'!'
            if i<0:
                text = '-' + text; i = Num(abs(i.value))
                # print '[',text
                # if len(text)>1 and text[0:2]=='--':
                #     print '@',text,text[1:]
                #     text = text[2:]

                if i==1: continue
            if len(text)>0 and text[-1].isdigit() and str(i)[0].isdigit():
                text += '*' + str(i)
            else:
                # text += str(i)
                # if isinstance(i,Add):
                    # print i.elements[0]
                text += str(i)
        text = text.replace('--','')
        if len(text)==0:
            return '(1)'
        if text=='-':
            return '(-1)'
        return '(' + text[0:] + ')'

def toNum(*args):
    args = list(args)
    for i in range(len(args)):
        if isinstance(args[i],(int,long,float)):
            args[i]=Num(args[i])
        elif isinstance(args[i],list):
            args[i]=toNum(*args[i])
    return args


def compareList(list_1,list_2):
    list1 = list(list_1); list2 = list(list_2)
    while len(list1)>0:
        i = list1[0]
        done = False
        for j in list2:
            if j==i:
                done = True
                list1.remove(i); list2.remove(j)
                break
        if not done:
            list1.remove(i)
    if len(list1)==0 and len(list2)==0:
        return True
    if len(list1)==0 or len(list2)==0:
        return False


