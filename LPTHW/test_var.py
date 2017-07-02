#test a syntax
import random

test_list=['chandan','nithish','sanju']
test_list2=['abc','xyz']

new_var1=random.sample(test_list,1)
new_var2=random.sample(test_list2,1)

#print new_var1
#print new_var2

for loop_var in new_var1,new_var2:
    final_list=loop_var[:]
for i in range(0,len(final_list)):
   print final_list
