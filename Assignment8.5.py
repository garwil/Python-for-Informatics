# Parse a file for email addresses, print them along with a total count.

try:
    fname = raw_input("Enter file name: ")
    handle = open(fname)
except:
    print "Error: Invalid file name."
    exit()

emails = []
count = 0

for line in handle:
    if not line.startswith("From") or line.startswith("From:") : continue
    emails = line.split()
    count = count+1
    print emails[1]
print "There were", count, "lines in the file with From as the first word"