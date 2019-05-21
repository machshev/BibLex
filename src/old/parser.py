
import string
import bible
import sys

class plaintext():
    def __init__(self, infile, names):
        self.infile = infile

        self.header = True
        self.chapterNum = 0
        self.bookNum = 0

        self.names = names

        self.chapters = {}


    def parse(self, fn):
        f = open(self.infile, "r")

        for l in f.readlines():
            w = l.strip().translate(string.maketrans("",""),
                                    string.punctuation
                                    ).lower().split(" ")

            if self.header is True:
                if w[0] == "chapter" or w[0] == "psalm":
                    self.header = False

                    if w[1] == "1":
                        name = self.names[self.bookNum]

                        if self.bookNum != 0:
                            self.chapters[name] = self.chapterNum
                            print "\t[{0}]".format(self.chapterNum)
                    
                        sys.stdout.write("parsing {0}".format(name))

                        self.bookNum += 1
                        self.chapterNum = 0

                    self.chapterNum += 1

                # Ignore theest or the header
                continue

                
            if len(w[0]) == 0:
                self.header = True

            else:

                # Create full verse ref
                w[0] = "{0}:{1}:{2}".format(
                    self.bookNum,
                    self.chapterNum,
                    w[0])

                # exec
                fn(w)

        print "\t[{0}]".format(self.chapterNum+1)
        
        f.close()
