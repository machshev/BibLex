"""
@file   createquotes.py
@author David James McCorrie

create av.quotes
"""
import parser, bible
import itertools

#print "OT "+str(len(otnames))
#print "NT "+str(len(ntnames))

class createQuotes():
    def __init__(self, ifile, qfile):
        self.Index = {}

        self.loadIndex(ifile)

        self.qfile = open(qfile, "w")


    def __del__(self):
        self.qfile.close()


    # Load Index from .index file
    def loadIndex(self, qfile):
        f = open(qfile, "r")
        for q in f:
            (word, refs) = q.strip().split("\t")

            self.Index[word] = refs.split(" ")

        f.close()


    # Find quotes against an index file
    def findquotes(self, w):
        verse = w[0]
        refs = {}
        arefs = []

        # create index
        # retrieve the index entry for each word
        for word in set(w[1:]):
        
            if word == "" or word[0] == "[":
                continue

            if word in self.Index:
                refs[word] = self.Index[word]
                arefs.append(self.Index[word])

        # get list of unique refs
        arefs = list(itertools.chain(*arefs))        
        urefs = set(arefs)
        uwords = set(refs.keys())        

        # are there any shared refs
        if len(arefs) == len(urefs):
            return

        # compare refs
        for r in urefs:
            count = 0
            
            for w in refs:                
                if r in refs[w]:
                    count += 1

            if count > 3:
                words = []
                
                for w in uwords:
                    if r in refs[w]:
                        words.append(w)
                
                s = "{0}\t{1}\t{2}\t{3}".format(verse, r, count, " ".join(words))
                
                self.qfile.write(s+"\n")

                #print s


if __name__ == "__main__":
    cq = createQuotes("av.ot.index", "av.quotes")

    p = parser.plaintext("data/AV1611Bible.nt.txt", bible.NTNames)

    p.parse(cq.findquotes)
    
