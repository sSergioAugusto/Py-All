import os, time

def setup_tela():
	os.system('cls')
	print('=' * 80, end='')
	for c in range(23,0,-1):
		if c == 12:
			print('|', end='')
			print(' ' * 31,'SETUP DA TELA',' ' * 32, end='')
			print('|', end='')
		elif c == 11:
			print('|', end='')
			print(' ' * 30,'Prosseguindo.....',' ' * 29, end='')
			print('|', end='')
		else:
			print('|', end='')
			print(' ' * 78, end='')
			print('|', end='')
	print('=' * 80)

def linha_topo():
	os.system('cls')
	print('=' * 10, '[ Sérgio Lima (deLima) ]', '=' * 16, '[ V. 0.2.12 ]', '=' * 13)

def logo_PYALL():
	linha_topo()
	def esp():
		return ' ' * 14
	print(esp(), ' _______  __       __         _______   __      __')
	print(esp(), '|   _   | \ \     / /        |   _   | |  |    |  |')
	print(esp(), '|  | |  |  \ \   / /         |  | |  | |  |    |  |')
	print(esp(), '|  |_|  |   \ \_/ /  _____   |  |_|  | |  |    |  |')
	print(esp(), '|    ___|    \   /  |_____|  |   _   | |  |    |  |')
	print(esp(), '|   |         | |            |  | |  | |  |    |  |')
	print(esp(), '|   |         | |            |  | |  | |  |    |  |')
	print(esp(), '|   |         | |            |  | |  | |  |__  |  |__')
	print(esp(), '|___|         |_|            |__| |__| |_____| |_____|')