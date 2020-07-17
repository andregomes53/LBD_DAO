import sqlite3
from datetime import datetime, date, time, timedelta

import time


conn = sqlite3.connect('modelo_academia.db')

c = conn.cursor()

start = time.time()
#c.execute('SELECT idSocio, nome, hora from socio_reserva_sala_squash, socio where idSocio = Socio_idSocio ')
#c.execute('SELECT idSocio, nome, hora from socio_reserva_sala_squash inner join socio on idSocio = Socio_idSocio ')

end = time.time()
print(end-start)


def insereSalasSquash():

    data = date(4700, 11, 22)
    for i in range(1000000):
        
        data -= timedelta(days=1)
        print("foram"+str(i))
        d = (7,3,data,'15:00',)
        c.execute('INSERT INTO socio_reserva_sala_squash VALUES	(?,?,?,?)',d)
    
    conn.commit()
        
    

#insereSalasSquash()

conn.close()


