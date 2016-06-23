#Calculate gross pay including overtime

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
h = float(hrs)
r = float(rate)
o = 0.0
ovr = 0
if h > 40:
    o = h - 40
    ovr = r * 1.5
    h=40
    
overtime = o * ovr
pay = (r * h)
pay = pay + overtime
print pay