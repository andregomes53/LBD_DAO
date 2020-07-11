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

#socio = input("Digite seu código de sócio:")

socio = 7

conn = sqlite3.connect('modelo_academia.db')
#TESTANDO PULL
c = conn.cursor()

def verificaReservas(socio):
	s = (socio,)
	query = c.execute('SELECT * FROM socio_reserva_sala_squash where Socio_idSocio = ?', s)
	results = c.fetchall()
	if len(results) == 0:
		print("Vc nao tem nenhuma reserva ainda.")
	else:
		print("Estas sao as suas reservas:\n")
		print(results)
	conn.commit()

def reservaSala(socio,sala):
	data = getData()
	d = (socio,sala,data,hora,)
	verificaDisponibilidade()
	try:
		c.execute('INSERT INTO socio_reserva_sala_squash VALUES	(?,?,?,?)',d)
	except:
		print("Nao foi possivel fazer esta reserva")
	else:
		print("Reserva efetuada!")
	conn.commit()

def verificaDisponibilidade():
	data = getData()

def getData():
	dia = int(input("Digite o dia da reserva:"))
	mes = int(input("Digite o mes da reserva:"))
	ano = int(input("Digite o ano da reserva:"))
	hora = int(input("Digite o horario da reserva:"))
	data = datetime(ano,mes,dia,hora,0)
	return data
	

print(getData())
conn.close()
