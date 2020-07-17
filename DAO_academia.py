'''
Nomes:
André 
Guilherme
Kevin

Aplicação para Reserva de salas da Academia
'''

import sqlite3
from datetime import datetime, date, time

print("#SISTEMA DE RESERVA#")


conn = sqlite3.connect('modelo_academia.db')

c = conn.cursor()

def verificaReservas():
	socio = input("Digite o numero do socio")
	s = (socio,)
	query = c.execute('SELECT * FROM socio_reserva_sala_squash where Socio_idSocio = ?', s)
	results = c.fetchall()
	if len(results) == 0:
		print("Vc nao tem nenhuma reserva ainda.")
	else:
		print("Estas sao as suas reservas:\n")
		toString(results)
	conn.commit()

def toString(results):
	for i in range(len(results)):
		data = results[i][2]
		print("Reserva na sala {} na data: {}".format(results[i][1],results[i][2]))

def reservaSala():
	sala = input("Digite o numero da sala")
	socio = input("Digite o numero do socio")
	q = 'S'
	while q == 'S' or q == 's':
		data = getData()
		d = (socio,sala,data,'')
		if not verificaDisponibilidade(data):
			print("Essa sala já está reservada neste horário")
			return
		try:
			c.execute('INSERT INTO socio_reserva_sala_squash VALUES	(?,?,?,?)',d)
		except:
			print("Nao foi possivel fazer esta reserva")
		else:
			print("Reserva efetuada!")
		q = input("Quer fazer mais uma reserva: (S/N)")
	conn.commit()

def verificaDisponibilidade(data):
	
	d = (data,)
	query = c.execute('SELECT * FROM socio_reserva_sala_squash where data = ?',d)
	results = c.fetchone()
	if results:
		return False
	else:
		return True

def getData():
	dia = int(input("Digite o dia da reserva:"))
	mes = int(input("Digite o mes da reserva:"))
	ano = int(input("Digite o ano da reserva:"))
	hora = int(input("Digite a hora da reserva:"))
	data = datetime(ano,mes,dia,hora,0)
	return data

def selecionaFuncao(op):
	op = int(op)

	if op == 1: 
		reservaSala()
	elif op == 2:
		verificaReservas()
	elif op == 3:
		data = getData()
		input("Digite o numero da sala: ")
		if verificaDisponibilidade(data):
			print("Sala disponível")
		else:
			print("A sala está indisponível")
	else:
		print("Você digitou um código inválido, tente novamente")

q = 'S'
while q == 'S' or q == 's':
	print("O que deseja fazer?")
	print("1 - Fazer uma reserva")
	print("2 - Verificar suas reservas")
	print("3 - Verificar se um horário esta disponivel")
	op = input()
	selecionaFuncao(op)
	q = input("Deseja fazer mais alguma operação? (S/N)")

conn.close()
