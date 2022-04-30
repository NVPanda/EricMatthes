# Este curso usa como base o Livro Curso Intensivo de Python do Autor Eric Matthes

# Variáveis e tipos de dados simples

# Na primeira parte deste módulo aprendemos a fazer o famoso Hello World.

"""Consiste em criarmos um arquivo Hello_World.py
no mesmo abrimos o console interativo via google collab, 
usamos o idle python ou até mesmo um editor de código de sua preferência para
criar o arquivo Hello_World.py e nele digitarmos o seguinte código:

print('Hello World!') * Nota: Podemos usar aspas simples '' ou duplas "" e o interpretador irá reconhecer da mesma maneira.

Bem neste arquivo iremos abordar o conceito de variáveis.
"""

# Variáveis são todo valor que é armazenado previamente que possui a propriedade de serem alterados. Ou seja, eles irão variar conforme
# a vontade do programador. ;)

# Ex 01:

mensagem = "Olá amigo!"
print(mensagem)

mensagem = input('Digite o seu nome:\n')
print(type(mensagem))
nome = (mensagem)
print('{}'.format(nome))

""" No nosso Ex 01, criamos uma variável chamada 'mensagem' e nela definimos o valor "Olá Amigos", após isso alteramos o valor da variável mensagem
transformando ela num input, input significa solicitar uma informação ao usuário. Neste solicitamos seu nome e em seguida atribuímos a 'mensagem' o
nome do mesmo, na última linha nós colocamos uma formatação, que nada mais é do que usar o nome e solicitar o mesmo através do console.
Neste caso fizemos a impressão na tela com print, colocamos as chaves {} para ser nosso escopo do que será mostrado e formatamos o escopo,
trazendo assim o nome do usuário que foi solicitado anteriormente através do input. Simples né?"""

# Então concluímos que variável é todo valor que pode variar conforme solicitarmos ou quisermos. :D

# Existem regras para criação de variáveis. 
# """ Estas são definidas a seguir:
# Regra 1 : Nomes de variáveis podem conter apenas Letras, Números e Underscores " _ " (usa-se a tecla shift e aperta o botão de hífen do teclado).
        #   Por exemplo, podemos chamar uma variável de message_1, mas não de 1_message.

# Regra 2 : Espaços não são permitidos em nomes de variáveis, mas underscores podem ser usados para separar palavras em nomes de variáveis.
        #   Por exemplo, greeting_message funciona, mas greeting message causará erros.

# Regra 3 : Evite usar palavras reservadas e nomes de funções em Python como nomes de variáveis, ou seja, não use palavras que Python reservou para um propósito particular de programação, por exemplo, a palavra print.
        #  (Veja a seção “Palavras reservadas e funções embutidas de Python”.) * Nota: Esta sessão encontra-se no livro do Eric Matthes ;)

# Regra 4 : Nomes de variáveis devem ser concisos, porém descritivos.
        #   Por exemplo, name é melhor que n, student_name é melhor que s_n e name_length é melhor que length_of_persons_name.

# Regra 5 : Tome cuidado ao usar a letra minúscula l e a letra maiúscula O, pois elas podem ser confundidas com os números 1 e 0.