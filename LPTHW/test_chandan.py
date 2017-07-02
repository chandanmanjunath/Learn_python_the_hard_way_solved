from sys import exit
from sys import settrace
print "enter the number for which number of 2s multiple to calculate"
n=int(raw_input())
i=1
while (2**i != n):
  i=i+1
  if(2**i > n):
     print n,"is not a multiple of 2"
     exit(0)

print "the 2 is repeated",i,"times"
