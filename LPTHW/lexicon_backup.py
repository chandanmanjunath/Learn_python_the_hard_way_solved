from itertools import izip
direction = {'north':('direction','north'), 'south':('direction','south'),'east':('direction','east'), 'west':('direction','west')}
verbs     = {'go':('verb', 'go'), 'stop':('verb', 'stop'), 'kill':('verb', 'kill'), 'eat':('verb', 'eat')}
stop      = {'the':('stop','the'), 'in':('stop','in'), 'of':('stop','of'), 'from':('stop','from'), 'at':('stop','at'), 'it':('stop','it')}
nouns     = {'door':('noun','door'),'bear':('noun','bear'),'princess':('noun','princess'),'cabinet':('noun','cabinet')}
numbers   = {'1234':('number', 1234),'3':('number', 3),'91234':('number', 91234)}
#error     ={               }

class lexicon(object):

    def scan(self, sentence):
        self.flag=''
        self.list_var=[]
        self.sentence = sentence
        self.words    =self.sentence.split()
        for k1,k2,k3 in izip(direction,verbs,nouns):
        #for key in direction:
             print 'in for'
             print direction[k1][1]
             #print 'stop values',stop[k3][1]
             self.j=0
             while self.j < len(self.words):
                    print 'in while'
                    if direction[k1][1] == self.words[self.j] :
                         print 'in if'
                         self.flag='d'
                         break
                    elif verbs[k2][1] == self.words[self.j] :
                        print 'in elif'
                        self.flag='v'
                        break
                    elif nouns[k3][1] == self.words[self.j] :
                        print "in stop elif"
                        self.flag='n'
                        break
                    self.j=self.j+1
        for k4 in numbers:
            print 'in for'
            print numbers[k4][1]
            #print 'stop values',stop[k3][1]
            self.j=0
            while self.j < len(self.words):
                   print 'in while'
                   if str(numbers[k4][1]) == self.words[self.j] :
                        print 'in if set flag'
                        self.flag='nu'
                        break
                   self.j=self.j+1
        for k5 in stop:
           print 'in for'
           print stop[k5][1]
           #print 'stop values',stop[k3][1]
           self.j=0
           while self.j < len(self.words):
                  print 'in while'
                  if stop[k5][1] == self.words[self.j] :
                       print 'in if set flag'
                       self.flag='s'
                       break
                  self.j=self.j+1

        print self.flag
        print 'word length',len(self.words)
        if self.flag =='d':
          if len(self.words) == 1:

              print self.words[0]
              self.list_var.append(direction.get(self.words[0]))
              print  self.list_var
              return self.list_var
          else :
              print "else"
              self.i = 0
              #print self.words
              while self.i < len(self.words):
                     #print 'while inside self i',self.i
                     #print len(self.words)
                     self.list_var.append(direction.get(self.words[self.i]))
                     self.i=self.i+1;
                     #i=i+1;
              return self.list_var
                      #print 'while'
                      #print len(self.words)
                      #print self.i
                      #print self.words[self.i]
                      #self.list_var.append(direction.get(self.words[self.i])
             # print self.list_var

             # return "["+str(self.list_var[0])+"]"
              #print self.abc
              #return self.abc
        elif self.flag == 'v':
           print 'in else part'
           if len(self.words) == 1:

               print self.words[0]
               self.list_var.append(verbs.get(self.words[0]))
               print  self.list_var
               return self.list_var
           else :
               print "else"
               self.i = 0
               #print self.words
               while self.i < len(self.words):
                      #print 'while inside self i',self.i
                      #print len(self.words)
                      self.list_var.append(verbs.get(self.words[self.i]))
                      self.i=self.i+1;
                      #i=i+1;
               return self.list_var
        elif self.flag == 'n':
           print 'in else part stops'
           if len(self.words) == 1:

               print self.words[0]
               self.list_var.append(nouns.get(self.words[0]))
               print  self.list_var
               return self.list_var
           else :
               print "else"
               self.i = 0
               #print self.words
               while self.i < len(self.words):
                      #print 'while inside self i',self.i
                      #print len(self.words)
                      self.list_var.append(nouns.get(self.words[self.i]))
                      self.i=self.i+1;
                      #i=i+1;
               return self.list_var
        elif self.flag == 'nu':
           print 'in else part number'
           if len(self.words) == 1:

               print self.words[0]
               self.list_var.append(numbers.get(self.words[0]))
               print  self.list_var
               return self.list_var
           else :
               print "else"
               self.i = 0
               #print self.words
               while self.i < len(self.words):
                      #print 'while inside self i',self.i
                      #print len(self.words)
                      self.list_var.append(numbers.get(self.words[self.i]))
                      self.i=self.i+1;
                      #i=i+1;
               return self.list_var
        elif self.flag == 's':
                  print 'in else part stop'
                  if len(self.words) == 1:

                      print self.words[0]
                      self.list_var.append(stop.get(self.words[0]))
                      print  self.list_var
                      return self.list_var
                  else :
                      print "else"
                      self.i = 0
                      #print self.words
                      while self.i < len(self.words):
                             #print 'while inside self i',self.i
                             #print len(self.words)
                             self.list_var.append(stop.get(self.words[self.i]))
                             self.i=self.i+1;
                             #i=i+1;
                      return self.list_var
