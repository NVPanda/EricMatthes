# coding: utf-8

# Exercício 2 - Faça você mesmo.

# Letras Maiúsculas e Minúsculas em nomes:
""" Armazene o nome de uma pessoa em uma variável e então apresente o nome dessa pessoa em letras minúsculas, em letras maiúsculas e somente com 
    a primeira letra maiúscula.
"""
# Início do Código

name = input('Digite seu nome: ')
minus_case = ("O seu nome em letras minúsculas fica assim:\n\t{}.".format(name.lower()))
maius_case = ("O seu nome em letras maiúsculas fica assim:\n\t{}.".format(name.upper()))
capit_case = ("O seu nome em letras capitalizadas fica assim: \n\t{}.".format(name.capitalize()))
mensagem = (minus_case+'\n'+maius_case+'\n'+capit_case)

print(mensagem)

# Fim do Código

# Nota: os itens '\n ' e ' \t ' fazem respectivamente uma quebra de linha e uma tabulação (acrescenta 4 espaços ao início da frase / nome na saída)
# Rode o programa caso queira descobrir o que significa.

