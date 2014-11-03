from basic import Basic
import math

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
    def __new__(self,*arg):
        if arg[0]==math.e:
            return 1
        else:
            return Function.__new__(self,arg)