num = int (input("NUMERO"))
op= input("OPERACAO")
aux = 1
while aux <= 20:
    if op =="+":
        print (num, "+", aux,"=", num+aux)
    if op =="-":
        print (num, "-", aux,"=", num-aux)
    if op =="*":
        print (num, "*", aux,"=", num*aux)
    if op =="/":
        print (num, "/", aux,"=", num/aux)
    aux += 1