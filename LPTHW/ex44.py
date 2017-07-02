#implicit inheritance
class Parent(object):

 def implicit_fun(self):
    print "this is implicit_fun"

class Child(Parent):
    pass

Dad=Parent()

Son=Child()

Dad.implicit_fun()

Son.implicit_fun()

#Overriding to change the defination
class Parent(object):

 def Overriding_fun(self):
    print "this is Overriding_fun of parent"

class Child(Parent):
 def Overriding_fun(self):
     print "this is Overriding_fun of child"

Dad=Parent()

Son=Child()

Dad.Overriding_fun()

Son.Overriding_fun()

#explicitely calling parent class function

class Parent(object):

 def alter_fun(self):
    print "this is alter_fun of parent"

class Child(Parent):
 def alter_fun(self):
     print "this is alter_fun of child before parent call"
     super(Child,self).alter_fun()
     print "this is alter_fun of child after parent call"

Dad=Parent()

Son=Child()

Dad.alter_fun()

Son.alter_fun()
