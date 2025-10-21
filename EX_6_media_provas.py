# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("| ______________________________ |")
print("| SISTEMA DE PROVAS |")
print("| ______________________________ |")
aluno = input("Qual o nome do aluno")
p1 = float(input("Qual a primeira nota"))
p2 = float(input("Qual a segunda nota"))
p3 = float(input("Qual a terceira nota"))
soma = p1 + p2 + p3
media = soma / 3
print("| ______________________________ |")
print(f"Aluno:{aluno}")
print(f"Media:{media}")
print("Aluno aprovado")
print("| ______________________________ |")