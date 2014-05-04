import jieba.posseg as pseg
class sentence():
#    words={}
    def __init__(self,sentence=''):
        self.sentence = sentence
        self.words=[(w.word,w.flag) for w in pseg.cut(sentence)]

    def isquestion(self):
        return ('y' in [w[1] for w in self.words])


        
