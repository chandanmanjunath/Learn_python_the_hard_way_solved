#function with runtime arguments
def arg_run(*args):
    arg1,arg2=args
    print "the two arguments %r and %r" % (arg1,arg2)

def arg_one(arg1):
    print "the argument one is %r"  % (arg1)

def arg_two(arg1,arg2):
   print "the two arguments are %r and %r" % (arg1,arg2)

def arg_none():
  print "function with no arguments"


arg_run("chandan","nithish")
arg_one("chetan")
arg_two("guru","ganesh")
arg_none()
