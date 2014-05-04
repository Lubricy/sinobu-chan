import utils.io as io
from sentence import sentence

class robot:
    historylist=[]
    def think(self,inputstr):
        self.historylist.append(sentence(inputstr))
        if self.historylist[-1].isquestion():
            self.answer();
        else:
            self.imagine(self.historylist[-1]);
    
    def add(self,a,b):
        print a+b

    def history(self,back='10'):
        for h in self.historylist[-int(back):]:
            io.info(h.sentence)


    def console(self,inputstr):
        l = inputstr.strip().split(" ")
        try:
            func=getattr(self,l[0])
        except:
            io.error("No method called '" + l[0] + "'")
            return


        try:
            l=l[1:]
            io.info(l)
            func(*l)
        except:
            io.error("Wrong params")

    def answer(self):
        io.info("answer:")
        #TODO
        

    def imagine(self,sentence):
        io.info("imaging")
        for word in self.historylist[-1].words:
            io.info(word[0])
            io.info(word[1])


