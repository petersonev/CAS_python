# from basic import Basic,Var
from basic import Basic

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
    # def derivative(self,var):
    #     return

class log(Function):
    def __init__(self,arg,base=10):
        self.base = base
        Function.__init__(self,'log',arg)
    def __new__(self,*arg):
        if arg==():
            return super(log,self).__new__(self)
        # if arg[0]==e:
        #     return 1
        else:
            return super(log,self).__new__(self)
    # def derivative(self):
    #     return 1/self.arg


# def testmethod(self):
#     print 2

# basic.Test.method = testmethod


# basic.Test().method()