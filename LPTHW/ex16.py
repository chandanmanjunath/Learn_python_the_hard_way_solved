from sys import argv

script_name,filename=argv

print "we are going to erase the file %r" %filename
print "if you dont want press ctrl+c"
print "if you do want press enter"

raw_input("?")
print "opening the file"
target=open(filename,'w')

print "erasing the file"
target.truncate()

print "enter the three lines"

line1=raw_input("enter the line 1")
line2=raw_input("enter the line 2")
line3=raw_input("enter the line 3")

print "writing lines to file"

target.write(line1+"\n"+line2+"\n"+line3)
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target=open(filename,'r')



print target.read()

target.close()
