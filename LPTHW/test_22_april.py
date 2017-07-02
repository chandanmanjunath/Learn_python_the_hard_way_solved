''' print  this
is a paragraph
a saturday afternoon in bangalore

print "enter a filename"
name=raw_input()
temp=open(name)

print "contents of file %s are " % name

print "%s" %  temp.read() '''

#function recall
'''def test(arg1,arg2) :
    print arg1
    print arg2


test('chandan',1)'''

'''from sys import argv
from os.path import exists


file_name=argv[1]
to_file=open(file_name)
#print "the entered file exists %s" % exists(to_file)
print "is  output files exists %s" % exists(file_name)

pos =int(raw_input("which position content is required"))

def content_file(file_pointer,pos):
    file_pointer.seek(pos,0)
    print file_pointer.read(1);
content_file(to_file,pos)'''


'''test =raw_input("enter the strng")

print test.split(' ')

list_test=list(test)

for x in range(0, len(list_test)):
    print list_test[x]
list_test.sort();
print list_test

print list_test.pop(0)

print list_test.pop(-1)
#defining own list

list_chandan=[1,2,3,4,5,6,7]

sorted(list_chandan)
for x in range(0,len(list_chandan)):
 print list_chandan[x]'''



#append and join

list_things=['chandan','abc','new','xyz','def']
#for appending
new_list=['ggg','new','fff']

while(len(list_things) != 8):
     append_var=new_list.pop(0)
     list_things.append(append_var)

for x in range(0,len(list_things)):
 print list_things[x]

#converting list into sentences

sentence_var=' '.join(list_things)

print sentence_var

#slicing the values from list

new_var_sliced=list_things[3:4]

for x in range(0,len(new_var_sliced)):
 print new_var_sliced[x]
