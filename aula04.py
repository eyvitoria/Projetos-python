produtos= ["arroz", "feijao", "macarrao", "leite"]
valor= [2.20, 2.70, 3.00, 2.00]
cod = int (input("INFORME O CODIGO DO PRODUTO:\n"))
qnt = int (input("INFORME A QUANTIDADE:\n"))
total = valor[cod]*qnt
print ("PRODUTO:", produtos[cod])
print ("VALOR UNITARIO:", valor[cod])
print ("TOTAL", total)