#from sys import argv
#script_name,filename = argv
print "enter the filenme"
filename=raw_input(">")
txt=open(filename)



print "the contents of file %r" % filename
print txt.read()

print "type the filename again"

print "enter the newfilenme"

new_filename=raw_input(">")

txt_new=open(new_filename)

print "displaying the contents again"
print txt_new.read()
txt_new.close()
