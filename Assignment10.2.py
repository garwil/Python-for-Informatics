# Find out who sent the most emails from a text file based on lines startiong with "From" but not "From:"
# Use mbox-short.txt

try:
    fname = raw_input("Enter file name: ")
    handle = open(fname)
except:
    print "Error: Invalid file name."
    exit()

lines = []
tally = dict()

for line in handle:
    if not line.startswith("From") or line.startswith("From:") : continue
    line = line.strip()
    lines = line.split()
    time = lines[5]
    time = time.split(":")
    hours = time[0].split()
    for hour in hours:
        if hour in tally:
            tally[hour] = tally[hour] +1
        else:
            tally[hour] = 1
    #print tally

tally = sorted([(k,v) for k,v in tally.items()])
for k,v in tally: print k, v
