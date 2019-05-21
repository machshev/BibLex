from optparse import OptionParser

OTNames = ["Gen", "Exo", "Lev", "Num", "Deut",
           "Josh", "Judges", "Ruth", "1 Sam", "2 Sam",
           "1 Kin", "2 Kin", "1 Chron", "2 Chron",
           "Ez", "Neh", "Est", "Job", "Psa",
           "Prov", "Eccl", "Song",
           "Isa", "Jer", "Lam", "Ezek",
           "Dan", "Hos", "Joel", "Amos", "Obad", "Jon",
           "Mic", "Nah", "Hab", "Zeph", "Hag",
           "Zech", "Mal"]

NTNames = ["Mat", "Mark", "Luke", "John", "Acts",
           "Rom", "1 Cor", "2 Cor",
           "Gal", "Eph", "Philip",
           "Col", "1 Thes", "2 Thes",
           "1 Tim", "2 Tim", "Tit", "Philemon",
           "Heb", "James", "1 Peter", "2 Peter",
           "1 John", "2 John", "3 John", "Jude", "Rev"]

OTChapters = [50, 40, 27, 36, 34, 24, 21, 4, 31,
              24, 22, 25, 29, 36, 10, 13, 10, 42,
              150, 31, 8, 12, 66, 52, 5, 48, 12,
              14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4]

if __name__ == "__main__":
    parser = OptionParser()
    # parser.add_option("-f", "--file", dest="filename",
    #                   help="write report to FILE", metavar="FILE")
    # parser.add_option("-q", "--quiet",
    #                   action="store_false", dest="verbose", default=True,
    #                   help="don't print status messages to stdout")

    (options, args) = parser.parse_args()

    index = int(args[0])-1

    print index, OTNames[index], NTNames[index]
