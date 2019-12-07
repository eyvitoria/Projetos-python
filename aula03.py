nome= input ("informe seu nome:")
print (nome)
peso = input ("informe seu peso:")
print (peso)
altura = input ("informe sua altura:")
print (altura) 

imc = float (peso) / (float(altura) * float (altura))


if imc < 16:
     print ("magreza") 
elif imc <18:
    print ("abaixo do peso")
elif imc <25: 
	print ("saudavel")
elif imc <30:
	print ("acima do peso")
elif imc <35:
	print ("obesidade 1")
elif imc <40:
	print ("obesidade 2")
elif imc >40:
    print ("obesidade 3")	

print ("O imc de", nome, "e", imc)