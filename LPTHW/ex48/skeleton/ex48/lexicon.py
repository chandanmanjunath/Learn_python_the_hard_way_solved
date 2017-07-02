from itertools import izip
direction = {'north':('direction','north'), 'south':('direction','south'),'east':('direction','east'), 'west':('direction','west')}
verbs     = {'go':('verb', 'go'), 'stop':('verb', 'stop'), 'kill':('verb', 'kill'), 'eat':('verb', 'eat')}
stop      = {'the':('stop','the'), 'in':('stop','in'), 'of':('stop','of'), 'from':('stop','from'), 'at':('stop','at'), 'it':('stop','it')}
nouns     = {'door':('noun','door'),'bear':('noun','bear'),'princess':('noun','princess'),'cabinet':('noun','cabinet')}
numbers   = {'1234':('number', 1234),'3':('number', 3),'91234':('number', 91234)}


class lexicon(object):

    def scan(self, sentence):
        self.flag=''
        self.list_var=[]
        self.sentence = sentence
        self.words    =self.sentence.split()
        for k1,k2,k3 in izip(direction,verbs,nouns):
             self.j=0
             while self.j < len(self.words):
                    if direction[k1][1] == self.words[self.j] :
                         self.flag='d'
                         break
                    elif verbs[k2][1] == self.words[self.j] :
                         self.flag='v'
                         break
                    elif nouns[k3][1] == self.words[self.j] :
                         self.flag='n'
                         break
                    self.j=self.j+1
        for k4 in numbers:
            self.j=0
            while self.j < len(self.words):
                   if str(numbers[k4][1]) == self.words[self.j] :
                        self.flag='nu'
                        break
                   self.j=self.j+1
        for k5 in stop:
           self.j=0
           while self.j < len(self.words):
                 if stop[k5][1] == self.words[self.j] :
                       print 'in if set flag'
                       self.flag='s'
                       break
                 self.j=self.j+1

        if self.flag =='d':
          if len(self.words) == 1:
              self.list_var.append(direction.get(self.words[0]))
              return self.list_var
          else :
              self.i = 0
              while self.i < len(self.words):
                     self.list_var.append(direction.get(self.words[self.i]))
                     self.i=self.i+1;
              return self.list_var
        elif self.flag == 'v':
           if len(self.words) == 1:
               self.list_var.append(verbs.get(self.words[0]))
               return self.list_var
           else :
               print "else"
               self.i = 0
               while self.i < len(self.words):
                      self.list_var.append(verbs.get(self.words[self.i]))
                      self.i=self.i+1;
               return self.list_var
        elif self.flag == 'n':
           if len(self.words) == 1:
               self.list_var.append(nouns.get(self.words[0]))
               return self.list_var
           else :
               self.i = 0
               while self.i < len(self.words):
                      self.list_var.append(nouns.get(self.words[self.i]))
                      self.i=self.i+1;
               return self.list_var
        elif self.flag == 'nu':
           if len(self.words) == 1:
               self.list_var.append(numbers.get(self.words[0]))
               return self.list_var
           else :
               self.i = 0
               while self.i < len(self.words):
                      self.list_var.append(numbers.get(self.words[self.i]))
                      self.i=self.i+1;
               return self.list_var
        elif self.flag == 's':
            if len(self.words) == 1:
                  self.list_var.append(stop.get(self.words[0]))
                  return self.list_var
            else :
                self.i = 0
                while self.i < len(self.words):
                   self.list_var.append(stop.get(self.words[self.i]))
                   self.i=self.i+1;
                return self.list_var
