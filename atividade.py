numero = int(input("digite um numero: "))

if numero <= 1:
    print('não é primo nem composto: ')
else:
    primo = True
    
    for i in range(2, numero):
        if(numero % 2 ==0):
            primo = False
            break
      
    if primo:
        print("é primo")
    else:
        print("é composto")