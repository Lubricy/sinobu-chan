from sentence import sentence
class robot:
    history=[]
    def think(self,inputstr):
        self.history.append(sentence(inputstr))
        if self.history[-1].isquestion():
            return self.answer();
        else:
            return self.imagine();
    
    def console(self,inputstr):
        try:
            a=getattr(self,inputstr)
            a()
        except:
            print "No method called '" + inputstr + "'"

        

    def answer(self):
        #TODO 
        return "answer!"

    def imagine(self):
        #TODO
        return "imagine!"

