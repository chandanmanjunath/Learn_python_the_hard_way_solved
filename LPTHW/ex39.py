#Dictionaries
#import collections
from collections import OrderedDict
short_codes = OrderedDict()
short_codes={'sirsi':'si','siddapur':'sid','shimoga':'shi','bangalore':'ban'}
for name,scode in short_codes.items():
 print "the value of name %s the value of shortcode %s" % (name,scode)

print "*" * 10
ordered_dict=OrderedDict(short_codes)

for name,scode in ordered_dict.items():
 print "the value of name %s the value of shortcode %s" % (name,scode)

#getting the value from get method

new_var=short_codes.get('sirsi','no shortcode')

print "the value of sirsi short_code is %s" % (new_var)

new_var=short_codes.get('abc','no shortcode')

print "short code for abc is %s" % (new_var)
