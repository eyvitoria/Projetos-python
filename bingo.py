import random 


num = int(input("Informe um numero"))
adivinha = random.randrange(0,10)

    if(adivinha != num):
	   print("Tente novamente")
	if (adivinha == num):
	   print("Parabéns")
	if (adivinha > num):
		print ("Maior")
	if (adivinha < num):
		print("menor")
	aux += 1




