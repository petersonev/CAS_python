from basic import Basic
import math

pi = math.pi
e  = math.e

class Function(Basic):
    def __init__(self, name, arg):
        self.arg = arg
        self.name = name
    def __repr__(self):
        return '{0}({1})'.format(self.name,self.arg)
    def __eq__(self,other):
        if type(self)==type(other) and self.arg==other.arg:
            return True
        return False

class log(Function):
    def __init__(self,arg,base=10):
        self.base = base
        Function.__init__(self,'log',arg)
    def __new__(self,arg):
        if arg==e:
            return Num(1)
        return Function.__new__(self,arg)

class sin(Function):
    def __init__(self,arg):
        Function.__init__(self,'sin',arg)
    def __new__(self,arg):
        if arg==pi:
            return Num(0)
        if arg==pi/2:
            return Num(1)
        return Function.__new__(self,arg)

class cos(Function):
    def __init__(self,arg):
        Function.__init__(self,'cos',arg)
    def __new__(self,arg):
        if arg==pi:
            return Num(1)
        if arg==pi/2:
            return Num(0)
        return Function.__new__(self,arg)