import random

vitoria = 0
aux= 1
while aux <=5:
	
	jogadaPlayer = input("SUA JOGADA [PEDRA - 0,PAPEL - 1, TESOURA - 2:")
	jogadaComputador = random.randrange(0,2)

	jogadas = ["pedra", "papel", "tesoura"]

	print("Player:", jogadaPlayer)
	print("Computador:", jogadas[jogadaComputador])

	if jogadaPlayer == jogadas[jogadaComputador]:
		print("Empate")

	if jogadaPlayer == "pedra" and jogadas[jogadaComputador] == "tesoura":
		print("Player venceu")
		vitoria += 1
	if jogadaPlayer == "papel" and jogadas[jogadaComputador] == "pedra":
		print("Player venceu")
		vitoria += 1
	if jogadaPlayer == "tesoura" and jogadas[jogadaComputador] == "papel":
		print("Player venceu")
		vitoria += 1

	if jogadaPlayer == "tesoura" and jogadas[jogadaComputador] == "pedra":
		print("Computador venceu")
	if jogadaPlayer == "pedra" and jogadas[jogadaComputador] == "papel":
		print("Computador venceu")
	if jogadaPlayer == "papel" and jogadas[jogadaComputador] == "tesoura":
		print("Computador venceu")

aux += 1

if (vitoria >=3):
	print("Player venceu!!")
else:
	print("Computador venceu!!")
