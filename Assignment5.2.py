#Calculate largest and smallest numbers from a range, check for invalid input

largest = None
smallest = None
while True:
    
    #Take input
    num = raw_input("Enter a number: ")
    if num == "done" : break
    if len(num) <1 : break
    
    #Test input is valid
    try:
        inp = int(num)
    except:
        print "Invalid input"
    
    #Do the assignment!
    if largest is None:
    	largest = inp
    elif largest < inp:
    	largest = inp
    if smallest is None:
        smallest = inp
    elif smallest > inp:
        smallest = inp
        
print "Maximum is", largest
print "Minimum is", smallest