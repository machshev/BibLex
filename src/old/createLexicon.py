"""
@file   formattxt.py
@author David James McCorrie

create kjv.index
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
        refs = []
        
        # create index
        for word in set(w[1:]):
        
            if word == "" or word[0] == "[":
                continue

            if word in self.Index:
                refs.append(self.Index[word])

        # get list of unique refs
        arefs = list(itertools.chain(*refs))
        urefs = set(arefs)

        # are there any shared refs
        if len(arefs) == len(urefs):
            return

        # compare refs
        for r in urefs:
            count = 0
            for wordref in refs:
                if r in wordref:
                    count += 1

            if count > 3:
                self.qfile.write("{0} {1} {2}\n".format(w[0], r, count))

                print w[0], r, str(count)



if __name__ == "__main__":
    cq = createQuotes("av.ot.index", "av.quotes")

    p = parser.plaintext("data/AV1611Bible.nt.txt", bible.NTNames)

    p.parse(cq.findquotes)
    
