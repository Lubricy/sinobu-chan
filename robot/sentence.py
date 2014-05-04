import jieba.posseg as pseg
class sentence():
    words=[]
    def __init__(self,sentence=''):
        self.words=pseg.cut(sentence)

    def isquestion(self):
        return ('y' in [w.flag for w in self.words])


        
