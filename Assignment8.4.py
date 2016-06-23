# Read a file into a list of words, sort alphabetically and remove duplicate words.
# Open the file "romeo.txt"

try:
    fname = raw_input("Enter file name: ")
    handle = open(fname)
except:
    print "Error: Invalid file name."
    exit()

words = []

for line in handle:
    line = line.rstrip()
    words.extend(line.split())
    words2 = sorted(set(words))
print words2