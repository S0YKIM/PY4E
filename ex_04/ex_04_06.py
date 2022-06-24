def computepay(hours, rate) :
	print("In computepay", hours, rate)
	if fh > 40 :
		print("Overtime")
		reg = fh * fr
		otp = (fh - 40.0) * (fr * 0.5)
		pay = reg + otp
	else :
		print("Regular")
		pay = fh * fr
		print("Pay:", pay)
	return (pay)

sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
	fh = float(sh)
	fr = float(sr)
except:
	print("Error, please enter numeric input")
	quit()

xp = computepay(fh, fr)
print("Pay:", xp)
