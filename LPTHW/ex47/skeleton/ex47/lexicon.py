direction = {'north':('direction', 'north'), 'south':('direction', 'south'),'east': ('direction', 'east'),'west':('direction', 'west')]
'''verbs     = ['go', 'stop', 'kill', 'eat']
stop      = ['the', 'in', 'of', 'from', 'at', 'it']
nouns     = ['door', 'bear', 'princess', 'cabinet']
numbers   = [i for i in range(10)]'''


class lexicon(object):

    def scan(self, sentence):
        self.sentence = sentence
        self.words    = sentence.split()
        for key in direction:

                print direction(key)

            return direction(key)
