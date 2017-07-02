if __name__ == '__main__':
    n = int(raw_input())
    i=2
    if n >= 1 and n <= 100:
        if n%2 == 0 :
            if n>=1 and n<=5:
                print "Not Weird"
            elif n>=6 and n<=20:
                print "Weird"
            else :
                print "Not Weird"
        else :
            print "Weird"
