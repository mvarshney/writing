import sys
lines = open(sys.argv[1], "r").readlines()
print(" ".join([x.strip() for x in lines[1::3]]))
