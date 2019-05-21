"""
@file   formattxt.py
@author David James McCorrie

create kjv.index
"""
import parser, bible

#print "OT "+str(len(otnames))
#print "NT "+str(len(ntnames))

stopWords = ["we", "if", "us", "you", "our", "your",
             "let", "also", "at", "so", "into", "had",
             "an", "on", "then", "her", "hath", "there",
             "by", "when", "are", "this", "were", "but",
             "ye", "as", "have", "which", "from", "me",
             "was", "will", "thee", "their", "my", "thy",
             "him", "all", "not", "nither", "nor", "no",
             "may", "these", "do", "i", "thou", "with",
             "them", "is", "it", "be", "they", "a",
             "unto", "i", "for", "his", "he", "shall",
             "that", "in", "to", "of", "and", "the", "or",
             "said", "am", "yea", "now", "upon", "things",
             "while", "came", "come", "say", "saying",
             "over", "whent", "she", "son", "called",
             "see", "any", "put", "till", "saith", "did",
             "up", "other", "those", "art", "therefore",
             "more", "thing", "nothing", "shalt", "thine",
             "like", "can", "even", "began", "again"]

class createIndex():
    def __init__(self):
        self.Index = {}
        self.Barred = {}

        # Add the stopwords
        for b in stopWords:
            self.Barred[b] = 0

        self.BAR_LIM = 4000

    def index(self, w):
        # create index
        for word in w[1:]:
        
            if word == "" or word[0] == "[":
                continue

            if word in self.Barred.keys():
                self.Barred[word] += 1
                continue
            
            if word not in self.Index.keys():
                self.Index[word] = []

            if len(self.Index[word]) == self.BAR_LIM:
                self.Barred[word] = self.BAR_LIM
                self.Index.pop(word)
            
            else:
                self.Index[word].append(w[0])


    def saveIndex(self, filename):
        ifile = open(filename, "w")
        for word in self.Index:
            ifile.write("{0}\t{1}\n".format(word, " ".join(self.Index[word])))
        ifile.close()
            

    def saveBarred(self, filename):
        bfile = open(filename, "w")
        for word in self.Barred:
            bfile.write("{0}\t{1}\n".format(word, self.Barred[word]))
        bfile.close()


if __name__ == "__main__":
    ci = createIndex()

    p = parser.plaintext("data/AV1611Bible.ot.txt", bible.OTNames)

    p.parse(ci.index)

    ci.saveIndex("av.ot.index")
    ci.saveBarred("av.ot.barred")
