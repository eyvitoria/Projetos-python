from datetime import datetime 

hora1 = input ("Hora um")
hora2 = input ("Hora dois")
#nada aquis
formato = '%H:%M'#9:00 
hora1c = datetime.strptime(hora1, formato)
hora2c = datetime.strptime(hora2, formato) 

tempo = (hora2c - hora1c).total_seconds()/3600  #/3600-hora  , /60-minutos
print (tempo)