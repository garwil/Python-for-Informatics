# Open a file, print its contents in upper case
# Use words.txt as the file name

try:
    filename = raw_input("Enter file name: ")
    handle = open(filename)
except:
    print "Invalid file name."
    exit()

text = text.upper()
text = text.strip()
print text