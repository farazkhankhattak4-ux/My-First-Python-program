hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h > 40:
    reg = 40*r            # reg means regular pay
    otp = (h-40)*(r*1.5)  # otp means over time pay
    pay = reg + otp       # Thats the total pay
else:
    pay = h*r
print(pay)    