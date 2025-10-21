# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numero = int(input("escolha um numero de 1 a 7"))

if numero == 1:
    print("o dia escolhido e o domingo")
elif numero == 2:
    print("o dia escolhido e o segunda")
elif numero == 3:
    print("o dia escolhido e o terça")
elif numero == 4:
    print("o dia escolhido e o quarta")
elif numero == 5:
    print("o dia escolhido e o quinta")
elif numero == 6:
    print("o dia escolhido e o sexta")
elif numero == 7:
    print("o dia escolhido e o sabado")
else:
    print("o dia escolhido foi segunda")




