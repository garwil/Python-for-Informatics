# Find out who sent the most emails from a text file based on lines startiong with "From" but not "From:"
# Use mbox-short.txt

try:
    fname = raw_input("Enter file name: ")
    handle = open(fname)
except:
    print "Error: Invalid file name."
    exit()

lines = []
emails = dict()
most = 0

for line in handle:
    if not line.startswith("From") or line.startswith("From:") : continue
    lines = line.split()
    #Get rid of data we don't need, there's probably a way of doing this without losing data but I don't know how!
    del lines[0]
    del lines[1:]
    for email in lines:
        emails[email] = emails.get(email,0) + 1 
    
v, k = max((v, k) for k,v in emails.items())
print str(k) + " " + str(v)

