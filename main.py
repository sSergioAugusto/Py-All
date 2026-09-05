import os, time, random, ui
from hashlib import sha256

# LARGURA: 80
# ALTURA: 23

erro_main = ' '

while True:
	ui.setup_tela()
	time.sleep(5)

	while True:
		ui.logo_PYALL()
		print(f'\n\n{erro_main}\n\n [ 1 ] Criptografia\n\n [ 2 ] Calculadora\n\n [ 3 ] Jogos (TERMINAL)')
		try:
			escolher = int(input('\n\n-> '))
		except:
			erro_main = 'ERRO: Digite um valor válido'
		else:
			if escolher not in [1,2,3]:
				erro_main = 'ERRO: Digite uma opção válida'
			else:
				erro_main = ' '
				if escolher == 1: # CRIPTOGRAFIA (SHA-256)
					while True:
						ui.logo_PYALL()
						print(f'\n\n [ 0 ] Voltar\n\n [ 1 ] SHA-256')
						try:
							cpta_esclh = int(input(f'\n\n{erro_main}\n\n\n\n-> '))
						except:
							erro_main = 'ERRO: Digite um valor válido'
						else:
							if cpta_esclh not in [0,1]:
								erro_main = 'ERRO: Digite uma opção válida'
							else:
								erro_main = ' '
								if cpta_esclh == 1:
									while True:
										crptgfa = None
										ui.logo_PYALL()
										print('\n\n [ 0 ] Voltar\n\n [ 1 ] Criptografar')
										try:
											cpt_tp_esclh = int(input(f'\n\n{erro_main}\n\n\n\n-> '))
										except:
											erro_main = 'ERRO: Digite um valor válido'
										else:
											if cpt_tp_esclh not in [0,1]:
												erro_main = 'ERRO: Digite uma opção válida'
											else:
												erro_main = ' '
												if cpt_tp_esclh == 1:
													while True:
														ui.logo_PYALL()
														print(f'\n{erro_main}\n [ 0 ] Voltar\n\n Digite seu texto...\n SHA-256 Hash: {crptgfa}')
														try:
															sha_cptg = str(input('\n\n-> '))
														except:
															erro_main = 'ERRO: Digite um valor válido'
														else:
															erro_main = ' '
															if sha_cptg == '0':
																break
															else:
																crptgfa = sha256(sha_cptg.encode('utf-8')).hexdigest()
												elif cpt_tp_esclh == 0:
													break
								elif cpta_esclh == 0:
									break


				elif escolher == 2:
					while True:
						ui.logo_PYALL()
						print(f'\n\n [ 0 ] Voltar\n\n [ 1 ] Matemática básica\n\n [ 2 ] Equações\n\n {erro_main}')
						try:
							esc_math = int(input('\n\n-> '))
						except:
							erro_main = 'ERRO: Digite um valor válido'
						else:
							erro_main = ' '
							if esc_math == 1:
								n1 = '_'
								n2 = '_'
								while True:
									ui.logo_PYALL()
									print(f'\n{erro_main}\n [ 0 ] Voltar\n\n Operadores:\n\n + (soma), - (subtração)\n\n x (multiplicação), / (divisão), 00 = Zero')
									try:
										inpt_calc_n = str(input('\n\n-> '))
									except:
										erro_main = 'ERRO: Digite um valor válido'
									else:
										erro_main = ' '
										if inpt_calc_n == '+':
											while True:
												ui.logo_PYALL()
												print(f'\n{erro_main}\n [ 0 ] Voltar\n\n Cálculo: {n1} + {n2}')
												try:
													soma_n1 = int(input('\n\n\n\n\n\n-> '))
												except:
													erro_main = 'ERRO: Digite um número válido'
												else:
													if soma_n1 == 0:
														erro_main = ' '
														break
													erro_main = ' '
													n1 = soma_n1
													while True:
														ui.logo_PYALL()
														print(f'\n{erro_main}\n [ 0 ] Voltar\n\n Cálculo: {n1} + {n2}')
														try:
															soma_n2 = int(input('\n\n\n\n\n\n-> '))
														except:
															erro_main = 'ERRO: Digite um número válido'
														else:
															if soma_n2 == 0:
																erro_main = ' '
																break
															erro_main = ' '
															n2 = soma_n2
															soma = n1 + n2
															while True:
																ui.logo_PYALL()
																print(f'\n\n [ 0 ] Voltar\n\n Cálculo: {n1} + {n2} = {soma}\n\n{erro_main}')
																try:
																	fim_soma = int(input('\n\n\n\n-> '))
																except:
																	erro_main = ' ERRO: Apenas volte'
																else:
																	erro_main = ' '
																	if fim_soma == 0:
																		break
										elif inpt_calc_n == '0':
											erro_main = ' '
											break
							elif esc_math == 0:
								erro_main = ' '
								break
							else:
								erro_main = 'ERRO: Digite uma opção válida'
								