'''O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. 
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, 
de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de 
acordo com as seguintes condições: 
• IMC<17 - Muito abaixo do peso ideal 
• 17<=IMC<18,5 - Abaixo do peso 
• 18,5<=IMC<25 - Peso normal 
• 25<=IMC<30 - Acima do peso 
• 30<=IMC<35 - Obesidade I 
• 35<=IMC<40 - Obesidade II (severa) 
• IMC>=40 - Obesidade III (mórbida) '''

Idade = int(input("Introduza a sua idade\n:"))
Peso = float(input("Introduza o seu peso em Kg\n:"))
Altura = float(input("Introduza a sua altura em metros\n:"))

#IMC (kg/m2) = peso (kg) / altura2 (m)

IMC = Peso / (Altura**2)

if IMC<17:
   print (f" Muito abaixo do peso ideal")  
elif IMC >= 17 and IMC < 18.5:
       print (f" baixo do peso")  
elif IMC >= 18.5 and IMC <= 25:
    print (f"Peso normal")  
elif IMC >= 25 and IMC<30:
    print (f"Acima do peso")  
elif IMC >= 30 and IMC<35:
      print (f"Obesidade I") 
elif IMC >= 35 and IMC<40:
    print (f"Obesidade II (severa)") 
else: # IMC >=40
    print (f"besidade III (mórbida)")