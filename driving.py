country = input('Please input your country:')
age = input('Please input your age:')
age = int(age)
if country == "taiwan":
    if age >= 18:
        print('You can driving', age)
    else:
    	print('You can not driving', age)
if country == "usa":
	if age >= 16:
		print('You can driving', age)
    else:
    	print('You can not driving', age)