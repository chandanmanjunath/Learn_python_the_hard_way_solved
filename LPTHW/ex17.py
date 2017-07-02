from sys import argv
from os.path import exists

scriptfile,from_file,to_file=argv

print "copying from file %s to %s" %(from_file,to_file)

from_obj=open(from_file)
to_read=from_obj.read()

print "the length of file in bytes %d" % len(to_read)

print "is  output files exists %s" % exists(to_file)

print "ready to enter and ctrl c to abort"

raw_input()

to_obj=open(to_file,'w')
to_obj.write(to_read)

print "you are done"

to_obj=open(to_file,'r')


print to_obj.read()

from_obj.close()
to_obj.close()
