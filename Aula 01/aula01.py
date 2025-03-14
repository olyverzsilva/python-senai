# Programa de Boas-Vindas
nome = input("Digite seu nome: ")
print("Seja Bem-Vindo(a)", nome + ", fico muito feliz por ter você aqui!")

# Programa da Tabuada
numero = int(input("Digite um número para ver sua tabuada: "))
print("Tabuada do número", numero)
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

# Programa do Antecessor e Sucessor
n = int(input("Digite um número inteiro: "))
antecessor = n - 1
sucessor = n + 1
print("O antecessor de", n, "é", antecessor)
print("O sucessor de", n, "é", sucessor)

# Programa de Formatação de Texto
texto = input("Digite um texto: ")
print("O texto \"" + texto + "\" em maiúsculo é", texto.upper())
print("O texto \"" + texto + "\" em minúsculo é", texto.lower())
print("O texto \"" + texto + "\" em título é", texto.title())
print("O texto \"" + texto + "\" com a primeira letra maiúscula é", texto.capitalize())
