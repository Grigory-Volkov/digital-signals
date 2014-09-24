from optparse import OptionParser
import re


parser = OptionParser()
parser.add_option("-i", "--infile", dest="infilename", metavar="FILE", help="Input data integer;integer;.. file with \r\n")
parser.add_option("-o", "--outfile", dest="outfilename", metavar="FILE", help="Output data hex;hex;.. file with \r\n")

(options, args) = parser.parse_args()

with open(options.infilename) as f:
	content = f.read().splitlines()

for indx in range(len(content)):
	content[indx] = map(lambda item: hex(int(round(float(item)))), re.compile(r',').sub('.', content[indx]).split(';'))

open(options.outfilename, 'w').write('\r\n'.join(map(lambda arr: ';'.join(arr), content)))

content_hex = content

for indx in range(len(content_hex)):
	content[indx] = map(lambda item: ( bin(int(item, 16))[2:] ).zfill(16), content[indx])

for indx in range(len(content)):
	content[indx] = "{0:b}".format(indx).zfill(16) + ''.join(content[indx])

open(options.outfilename + '_bin', 'w').write('\r\n'.join(content))
