print "which place you want to go place 1 press 1  place 2 press 2 "
place=raw_input(">")
if place == "1":
    print "which resturant you want to go? press c for chinese i for italian in for indian"
    rest=raw_input(">")
    if rest == "c" :
        print "you are in chinese"

    elif rest == "i":
        print "you are in italian"
    else:
        print "you are in indian"
elif place == "2":
   print "which club you want to go? h high m medium l low"
   club=raw_input('>')
   if club == "h":
       print "you are high"
   elif club == "m":
        print "you are medium"
   else:
        print "you are low"
else :
  print "you are nothing"
