from basic import Basic
import math

pi = math.pi
e  = math.e

class Function(Basic):
    def __init__(cls, name, arg):
        cls.arg = arg
        cls.name = name
    def __repr__(cls):
        return '{0}({1})'.format(cls.name,cls.arg)
    def __eq__(cls,other):
        if type(cls)==type(other) and cls.arg==other.arg:
            return True
        return False
    def copy(cls):
        return type(cls)(cls.name,cls.arg.copy)

class log(Function):
    def __init__(cls,arg,base=10):
        cls.base = base
        Function.__init__(cls,'log',arg)
    def __new__(cls,arg):
        if arg==e:
            return Num(1)
        return Function.__new__(cls,arg)

class sin(Function):
    def __init__(cls,arg):
        Function.__init__(cls,'sin',arg)
    def __new__(cls,arg):
        if arg==pi:
            return Num(0)
        if arg==pi/2:
            return Num(1)
        return Function.__new__(cls,arg)

class cos(Function):
    def __init__(cls,arg):
        Function.__init__(cls,'cos',arg)
    def __new__(cls,arg):
        if arg==pi:
            return Num(1)
        if arg==pi/2:
            return Num(0)
        return Function.__new__(cls,arg)