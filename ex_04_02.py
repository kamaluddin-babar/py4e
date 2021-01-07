
def computepay(h,r):
    if h > 40:
        temp1 = 40.0*r
        temp2 = (h-40.0)*r*1.5
        pay = temp1 + temp2
    else:
        pay = h*r
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate:")
try :
    h = float(hours)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
p = computepay(h,r)
print("Pay",p)
