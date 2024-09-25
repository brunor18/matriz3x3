import os

m1= []
m2= []

def numeros_Matriz_1():
     print("Digite a primeira linha da primeira matriz:")

     n1_linha1_matriz1 = int(input("Primeiro número:"))         
     n2_linha1_matriz1 = int(input("Secundo número:"))                           
     n3_linha1_matriz1 = int(input("Terceiro número:"))

     m1.append(n1_linha1_matriz1)
     m1.append(n2_linha1_matriz1)
     m1.append(n3_linha1_matriz1)

     os.system('cls')

     print("Digite a segunda linha da primeira matriz:")

     n1_linha2_matriz1 = int(input("Primeiro número:"))         
     n2_linha2_matriz1 = int(input("Secundo número:"))                           
     n3_linha2_matriz1 = int(input("Terceiro número:"))

     m1.append(n1_linha2_matriz1)
     m1.append(n2_linha2_matriz1)
     m1.append(n3_linha2_matriz1)     

     os.system('cls')

     print("Digite a terceira linha da primeira matriz:")

     n1_linha3_matriz1 = int(input("Primeiro número:"))         
     n2_linha3_matriz1 = int(input("Secundo número:"))                           
     n3_linha3_matriz1 = int(input("Terceiro número:"))

     m1.append(n1_linha3_matriz1)     
     m1.append(n2_linha3_matriz1)
     m1.append(n3_linha3_matriz1)

     os.system('cls')


numeros_Matriz_1()


def numeros_Matriz_2():
     print("Digite a primeira linha da segunda matriz:")

     n1_linha1_matriz2 = int(input("Primeiro número:"))         
     n2_linha1_matriz2 = int(input("Secundo número:"))                           
     n3_linha1_matriz2 = int(input("Terceiro número:"))

     m2.append(n1_linha1_matriz2)  
     m2.append(n2_linha1_matriz2)
     m2.append(n3_linha1_matriz2)

     os.system('cls')

     print("Digite a segunda linha da segunda matriz:")

     n1_linha2_matriz2 = int(input("Primeiro número:"))         
     n2_linha2_matriz2 = int(input("Secundo número:"))                           
     n3_linha2_matriz2 = int(input("Terceiro número:"))

     m2.append(n1_linha2_matriz2)     
     m2.append(n2_linha2_matriz2)
     m2.append(n3_linha2_matriz2)

     os.system('cls')

     print("Digite a terceira linha da segunda matriz:")

     n1_linha3_matriz2 = int(input("Primeiro número:"))         
     n2_linha3_matriz2 = int(input("Secundo número:"))                           
     n3_linha3_matriz2 = int(input("Terceiro número:"))

     m2.append(n1_linha3_matriz2)     
     m2.append(n2_linha3_matriz2)
     m2.append(n3_linha3_matriz2)

     os.system('cls')

numeros_Matriz_2()




def soma():
    print("A soma das matrizes é:\n")
    
    print(m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2])
    print(m1[3] + m2[3], m1[4] + m2[4], m1[5] + m2[5])
    print(m1[6] + m2[6], m1[7] + m2[7], m1[8] + m2[8])

soma()
