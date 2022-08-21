#<title>Log in to Facebook | Facebook</title>
#<title>Content not found</title>
import requests as r
def idgen(len,size):
	ones = len
	twices = size
	m = r.get('https://m.facebook.com/profile.php?id=10007948689668')
	find = m.text
	count = 1
	for x in range(ones,twices):
		m = r.get('https://m.facebook.com/profile.php?id=1000'+str(x))
		find = m.text
		if '<title>Content not found</title>' in find or '<title>Log in to Facebook | Facebook</title>' in find:
			print(f'{[count]}\033[31m\033[1m Invalid Id: 1000{x}')
		else:
			print(f'{[count]}\033[32m Valid Id: 1000{x}')
			file = open('valid_Id.txt','a')
			file.write(f'1000{x}\n')
			file.close()
		count += 1	
idgen(24298102018,99999999999)		