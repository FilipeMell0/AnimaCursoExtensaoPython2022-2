#Pede o nome do aluno e sua nota de 0 a 10
nome = input("Qual seu nome? ")
a1 = float(input("Qual sua nota da A1?"))
a2 = float(input("Qual sua nota da A2?"))
a3 = float(input("Qual sua nota da A3?"))

media = (a1 + a2 + a3) / 3

print("Sua média é de {:.1f}".format(media))

if media >=7:
  print("Você passou de semestre!")
else:
  print("Você rodou!")