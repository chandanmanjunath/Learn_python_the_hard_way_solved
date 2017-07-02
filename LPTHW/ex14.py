from sys import argv
script,user_name,last_name=argv
prompt = '......... '

print "hi im %s,i have %s script" % (user_name,script)
print "i would like to answer few questions"
print "do you like me %s" % user_name
likes=raw_input(prompt)
print "where do you love %s" % user_name
lives=raw_input(prompt)
print "what kind of computer do you like ?"
computer=raw_input(prompt)
print """you are liking %r,
your home %r,
your computer %r """%(likes,lives,computer)
