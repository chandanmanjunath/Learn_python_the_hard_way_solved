from sys import argv

script,filename=argv
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(linecount,f):
   print linecount, f.readline()

current_file=open(filename)

print "lets print the contents of file",

print_all(current_file)

print "lets rewind the whole file",

rewind(current_file)

print "lets print line by line",

current_line=1

print_a_line(current_line,current_file)

current_line+=1

print_a_line(current_line,current_file)

current_line+=1

print_a_line(current_line,current_file)
