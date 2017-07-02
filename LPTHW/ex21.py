def add(a,b):
    print "addition of %d and %d" % (a,b)
    return a+b

def sub(a,b):
    print "subtraction of %d and %d" % (a,b)
    return a-b

def mul(a,b):
    print "multiply of %d and %d" % (a,b)
    return a*b

def div(a,b):
    print "division  of %d and %d" % (a,b)
    return a/b

age=add(10,20)
height=sub(25,10)
weight=mul(3,4)
id=div(10,5)

print "values age  %d  height %d weight %d id   %d" % (age,height,weight,id)

value=add(age,(sub(height,(mul(weight,div(id,2))) )))

print "the value is %d" % value
