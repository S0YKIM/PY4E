sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
	fh = float(sh)
	fr = float(sr)
except:
	print("Error, please enter numeric input")
	quit()

# print(fh, fr)
if fh > 40 :
	print("Overtime")
	reg = fh * fr
	otp = (fh - 40.0) * (fr * 0.5)
	xp = reg + otp
else :
	print("Regular")
	xp = fh * fr
print("Pay:", xp)
