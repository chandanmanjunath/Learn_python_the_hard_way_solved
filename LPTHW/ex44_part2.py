#Composition
#Doing implicit and accessing base class without inheritance
class Base(object):

    def implicit_fun(self):
           print "parent class implicit"
    def alter_fun(self):
          print "this is alter_fun of parent"
    def Overriding_fun(self):
          print "this is Overriding_fun of parent"

class Child(object):

    def __init__(self):
        self.base_var=Base()

    def implicit_fun(self):
        self.base_var.implicit_fun()

    def Overriding_fun(self):
        print "this is Overriding_fun of child"

    def alter_fun(self):
        print "this is alter_fun of child before parent"
        self.base_var.alter_fun()
        print "this is alter_fun of child after parent"

Son=Child()

Son.implicit_fun()
Son.Overriding_fun()
Son.alter_fun()
