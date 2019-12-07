veiculos = ["carro", "moto"]
valor = [12.00, 8.00]
cod = int (input("Carro 0 , moto 1\n"))
placa = input ("informe a placa")


from datetime import datetime 

hora1 = input ("Hora de entrada")
hora2 = input ("Hora de saida")

formato = '%H:%M'
hora1c = datetime.strptime(hora1, formato)
hora2c = datetime.strptime(hora2, formato) 

tempo = (hora2c - hora1c).total_seconds()/3600


total = (valor[cod]*tempo)

print ("Veiculo:", placa)
print ("Tempo", tempo)
print ("Total a pagar", total)