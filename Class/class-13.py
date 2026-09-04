# Python - Aula 13

#Introdução a blocos de código e operadores condicionais.

# if /    elif   / else
# se / se não se / se não

# if - checagem da primeira condição
# elif - se não for a primeira condição, pode ser a segunda
# else - acionado se nenhuma das condições forem atendidas

#Exemplo de uso:

login = input("Você quer entrar ou sair? ")

if login == "entrar": # Condição pode existir sózinha
    print("Você entrou no sistema!")

elif login == "sair": # Condição precisa de um if para poder existir
    print("O sistema foi fechado")

else: # Condição que é acionada apenas quando nenhuma das condições acima são validadas
    print("Você não digitou uma opção válida.")