# Operadores lógicos "and"

"""
and (e) or (ou) not (não)

and - todas as condições são verdadeiras
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
São considerados Falsy

0 ou o.o False

Também existe o tipo None, que é usado para representar um não valor.

Exercício prático abaixo:
"""
sem_senha = "Sem senha."
usuario = input("Usuário: ")
senha = input("Senha: ") or sem_senha
print(senha) # Interessante a utilização de or cmo uma espécie de if em uma única linha.
# O operador or, permite que o código fique mais dinâmico ao exercer a função de um if, como na linha 19.

usuario_adm = "lucas"
senha_adm = "123456"

# validação de usuário e senha
if usuario == usuario_adm and senha == senha_adm:
    print(f"Olá {usuario}, sua conta está pronta para ser utilizada!")

elif senha == sem_senha:
    print("Você não digitou a senha.")

else: # Credenciais incorretas
    print("Usuário e senha incorretos, tente novamente.")