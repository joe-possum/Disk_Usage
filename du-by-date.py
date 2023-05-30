import os
import sys

cmd = 'du --max-depth=1'
for arg in sys.argv[1:] :
    cmd += ' "' + arg + '"'
    
fh = os.popen(cmd, 'r')
text = fh.read()
fh.close()

lines = text.split('\n')
for line in lines :
    if 0 == len(line) : continue
    tokens = line.split()
    if 2 != len(tokens) : raise RuntimeError('bad token count: "%s"'%(line))
    usage = tokens[0]
    path = tokens[1]
    cmd = 'find "%s" -type f -printf "%%T+\n" | sort | tail -n 1'%(path)
    fh = os.popen(cmd, 'r')
    text = fh.read()
    fh.close()
    tokens = text.split('+')
    date = tokens[0]
    print('%s\t%s\t%s'%(usage,date,path))
    
