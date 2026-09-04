# Prática de memorização - IMC

nome = "Lucas"
sobrenome = "Martins"
ano_de_nascimento = 1998
idade = 2026 - ano_de_nascimento
peso = 60
altura = 1.80
imc = peso / (altura ** 2)

imc_fstrings = f"{nome} {sobrenome} tem {idade} anos de idade, pesa {peso} quilos e mede {altura:.2f} de altura, o seu IMC é: {imc:.2f}"

imc_format = "{} {} tem {} de idade, pesa {} quilos e mede {:.2f} de altura, o seu IMC é: {:.2f}" .format(
    nome, sobrenome, idade, peso, altura, imc
)

print("Com fstrings:", imc_fstrings)

print("Com .format:", imc_format)


