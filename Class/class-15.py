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

usuario = input("Usuário: ")
senha = input("Senha: ")

usuario_adm = "lucas"
senha_adm = "123456"

# validação de usuário e senha
if usuario == usuario_adm and senha == senha_adm:
    print(f"Olá {usuario}, sua conta está pronta para ser utilizada!")

else: # Credenciais incorretas
    print("Usuário e senha incorretos, tente novamente.")