"""
@file   createquotes.py
@author David James McCorrie

create av.quotes
"""
import parser, bible
import itertools

from optparse import OptionParser

#print "OT "+str(len(otnames))
#print "NT "+str(len(ntnames))

class exportQuotes():
    def __init__(self, quotesfilename):
        self.qfile = open(quotesfilename, "r")

    def __del__(self):
        self.qfile.close()


    # Load Index from .index file
    def export(self):
        
        for q in self.qfile.readlines():
            (nt_ref, ot_ref, count, words) = q.strip().split("\t")

            o = [int(i) for i in ot_ref.split(":")]
            n = [int(i) for i in nt_ref.split(":")]

            print "{0} {1}:{2},{3} {4}:{5},{6},{7}".format(bible.NTNames[n[0]-1], n[1], n[2],
                                                       bible.OTNames[o[0]-1], o[1], o[2],
                                                       count, words)



if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-t", "--type", type="str", dest="type")
 
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("Missing filename")

    eq = exportQuotes(args[0])
    eq.export()
