num=7
for i in range(1,101):
	if i % num !=0 and i%10!=7 and i//10!=7:
		print(i)
	else: 
		continue

