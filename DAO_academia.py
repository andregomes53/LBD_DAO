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

def reservaSala():

	q = 'S'
	while q == 'S' or q == 's':
		data = getData()
		d = (socio,sala,data,)
		verificaDisponibilidade()
		try:
			c.execute('INSERT INTO socio_reserva_sala_squash VALUES	(?,?,?,?)',d)
		except:
			print("Nao foi possivel fazer esta reserva")
		else:
			print("Reserva efetuada!")
		q = input("Quer fazer mais uma reserva: (S/N)")
	conn.commit()

def verificaDisponibilidade():
	data = getData()
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
    switcher = {
        1: reservaSala(),
        2: verificaReservas(),
        3: verificaDisponibilidade(),
    }
    switcher.get(op,"Voce digitou um valor inválido")

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
