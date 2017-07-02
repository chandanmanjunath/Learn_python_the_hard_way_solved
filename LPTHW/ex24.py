
print "you\'d be the best guy \\in the world newline\n  tab \t"

poem = """
aaaaaaaaaaaaaaaaaa
ccccccccccccccccccccc
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ssssssssssssssssss
ssssssssssssssssssssssss"""

print poem


def trial(start_var):
    a=start_var*1
    b=a-4
    c=b+4
    d=c/1
    return a,b,c,d


a,b,c,d=trial(10000)


print "the values a %d b %d c %d d %d" % (a,b,c,d)


print " a %d b %d c %d d %d" % trial(10000)
