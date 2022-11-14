#Criação de funções

preco = 19.90

#Calcular 5% de imposto, guardar variavel imposto e exibir na tela

imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#Aqui é o uso... aqui é imposto a calcular
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

#Explicação de variaveis local x global

print(preco) #???
preco_produto = 100
print(preco_produto) #???

#Agora calcular imposto a alíquota agora 7%

valores = [1.99,24.50,50.0,1515.5]

#Se eu quisser calcular o imposto dos 4 valores e exibir na tela assim:"O imposto de ... é ..."
for valor in valores:
  
  print(f"O imposot de {valor} é {calcular_imposto(valor)}")

#Declarar uma função calcular_imposto_aliquota que recebe dois parâmetros: o preço e a alíquota de imposto a ser aplicado. Se a alíquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

#E se agora o imposto for 10%?
for valor in valores:
  
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")