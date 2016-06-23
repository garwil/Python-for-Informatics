# Search a string for a number and print it

text = "X-DSPAM-Confidence:    0.8475";
string = "0."
output = text.find(string)
number = float(text[output:])
print number