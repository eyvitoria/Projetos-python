nome= input ("nome do aluno:")
np = input ("informe a nota da prova:\n")
print(np)
nt = input("informe a nota do trabalho:\n")
print(nt)
nq = input ("informe a nota da qualitativa:\n")
print(nq)

media = (float (np) * 6 + float (nt) * 3 + float (nq) )/10 

if media >= 6:
	print ("aprovado")
else:
	print ("reprovado")	 


print ("A media de ", nome, " e ", media) 