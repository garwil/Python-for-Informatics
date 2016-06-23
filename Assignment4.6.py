#Calculate gross pay based on user input, pay enhanced rate for overtime

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))

def computepay(h,r):
	o = 0.0
	ovr = 0
	if h > 40:
    	o = h - 40
    	ovr = r * 1.5
    	h=40
        overtime = o * ovr
        pay = (r * h)
        pay = pay + overtime
        return pay

p = computepay(45,10.50)
print p