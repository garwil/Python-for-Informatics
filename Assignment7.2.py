# Search a file for the numbers following "X-DSPAM-Confidence:" and calculate a floating point average 
# Use the file name mbox-short.txt as the file name
try:
    fname = raw_input("Enter file name: ")
    handle = open(fname)
except:
    print "Error: Invalid file name."
    exit()

numbers = []
count = 0

for line in handle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    line = line[line.find("0"):]
    numbers.insert(count, float(line))
    count = count+1

mean = str(sum(numbers)/len(numbers))
print "Average spam confidence: " + mean

    

