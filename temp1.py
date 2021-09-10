class BadName(Exception):
	pass

def greet(name):
	if name[0].isupper():
		return 'Hello, '+name
	else:
		raise BadName(name+' is inappropriate name')

# print(greet('Sasha'))
# print(greet('sasha'))

while True:
	try:
		name = input('enter your name: ')
		greeting = greet(name)
		greeting
	except BadName:
		print('try one more time...')
	else:
		break
