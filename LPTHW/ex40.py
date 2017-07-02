class test():
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_song(self):
        for abc in self.lyrics:
            print abc

trial_object=test(["abc fkafhksdfhkdshak",
                   "xyz jflsflsdfslag",
                   "ckdsfkdsghsakg"])
trial_object.sing_song();
