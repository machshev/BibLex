from lxml import etree
import argparse

parser = argparse.ArgumentParser(description='Parse strongs dictionary')
parser.add_argument('strongsfile', type=file,
                    help='strongs dictionary file')

args = parser.parse_args()

tree = etree.parse(args.strongsfile)
root = tree.getroot()

ns={'h': 'http://www.w3.org/1999/xhtml'}

entries = root.xpath("//h:section[@id='ot']/*/h:li", namespaces=ns)

W = {}

for e in entries:
    sid =  e.get("value")
    word = e.xpath("./h:i", namespaces=ns)[0].text
    #print [e.tag for e in list(w.iter())]

    W[sid] = [word, None]
    
    #print etree.tostring(i)

    break

print W
