import sys
import pikalang

filename = sys.argv[-1]
print(filename)
sourcecode = pikalang.load_source(filename)

if sourcecode:
    pikalang.evaluate(sourcecode)
