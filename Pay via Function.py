def computepay(h,r):
  if h > 40:
     reg = 40*r
     otp = (h-40)*(r*1.5)
     pay = reg + otp
  else:
      pay = h*r     
  return pay # return the pay
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
pay = computepay(h,r) # call the function
print("Pay",pay)      