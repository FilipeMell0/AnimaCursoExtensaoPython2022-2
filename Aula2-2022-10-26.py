#comando input(): solicitar que o usuário digite algo
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

#comando de saída
print(f"\nSeu nome é {nome} e você tem {idade} anos")

# mostrar o dobro da idade
dobro = idade * 2
print(f"O dobro da sua idade é: {dobro}\n")

#Estrutura condicional = if
if idade>=18:
  print(f"Você pode beber ou dirigir!\n")

else:
  print(f"Infelizmente vai ficar só na carona e no refri\n")

#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)

genero = input("Qual seu gênero? ")

if idade >= 18 and (genero == "m" or genero == "M"):
  print("Você prestou o serviço militar!")
else:
  print("Você é mulher ou menor de idade :)")