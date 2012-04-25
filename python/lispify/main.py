from optparse import OptionParser
import os.path
from lispify.lispify import lispify
from lispify.tests import runtests
from lispify.parsers import astparser, simpleparser

parser = OptionParser(usage='Usage: %prog [options] filename')
parser.add_option('-r', action='store_true', dest='simplify', default=False,
                  help='simplify expressions as much as possible')
parser.add_option('-t', action='store_true', dest='runtests', default=False,
                  help='run tests')
parser.add_option('-p', action='store_true', dest='customparser', default=False,
                  help='use homemade parser instead of ast')
(options, args) = parser.parse_args()

treeparser = simpleparser if options.customparser else astparser 

if options.runtests:
    runtests(simplify=options.simplify, parser=treeparser)
    exit()
    
if len(args) == 0:
    parser.print_help()
    exit()
    
filename, = args
if not os.path.exists(filename):
    print 'File not found'
    exit()

with open(filename) as fd:
    for line in fd.readlines():
        line = line.strip()
        print line
        try:
            print lispify(line, simplify=options.simplify, parser=treeparser)
        except:
            print 'Unable to parse expression'
        print '\n'