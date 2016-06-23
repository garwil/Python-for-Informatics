#Take a number as input, throw exception if out of range
try:
    score = float(raw_input("Enter a score between 0.0 & 1.0:"))
    if score >= 0.9:
    	grade = "A"
    elif score >= 0.8:
        grade  = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    print grade
except:
    print "Error"