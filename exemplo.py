numero = int(input("digite um numero: ")) 
status = False
for i in range(2,numero-1):     
    if(numero % i==0):         
        status = False         
        break    
    status = True          
    if(status):         
        print(f"0 {numero} é um numero primo")    
    else:         
        print(f"0 {numero} não é um numero primo")