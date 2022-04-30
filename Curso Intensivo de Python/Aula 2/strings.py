# Uma string é simplesmente uma sequência de caracteres. 
# É como formar palavras ou frase em português. 
# Mas podem ser utilizadas de várias formas diferentes.

# Portanto tudo o que estiver entre aspas (sejam simples ou duplas) é considerado string, 
# a menos que você defina previamente o tipo de dados. Mas isto é outro tópico que abordaremos mais adiante.

# Mudando para letras maiúsculas e minúsculas usando métodos. Métodos são pequenos comandos utilizados em strings para manipular suas formas.

# Ex:
#   name = "ada lovelace"
#   print(name.title())

from numpy import full


name = "ada lovelace"
print(name.title()) # Perceba que ao executarmos essa linha após definirmos nossa variável name, o nome que estava em minúsculas se tornou diferente.
                    # Tendo as duas iniciais do nome 'ada lovelace' alteradas para maiúsculas e preservando o restante em minúsculas.

# portanto método é todo 'comando' que permite o Python executar uma ação em um dado. 
# Neste exemplo o comando foi alterar as iniciais dos nomes para maiúsculas.

""" Podemos mudas caracteres entre maiúsculos e minúsculos de várias maneiras em Python.
    Por exemplo se quisermos todas as letras em maiúsculas ou em minúsculas podemos usar os métodos upper() e lower() respectivamente."""

# Ex:
#   name = "ada lovelace"
#   print(name.upper())
#   print(name.lower())

name = "ada lovelace"
print(name.upper())
print(name.lower())

# Estas exibiram respectivamente ADA LOVELACE e ada lovelace.

# Podemos também combinar ou concatenar strings, isto é juntar strings quando for necessário ou quando quisermos satisfazer algo pessoal.

# Ex:
#   first_name = "ada"
#   last_name = "lovelace"
#   full_name = first_name + " " + last_name
#   print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# Podemos usar a concatenação para exibir mensagens completas juntando palavras e métodos e até mesmo símbolos.

# Ex:
"""     first_name = 'ada'
        last_name = 'lovelace'
        full_name = first_name + ' ' + last_name 
        print("Hello, + full_name.upper() + '!')
"""

first_name = "ada"
last_name = "lovelace"
full_name = first_name + ' ' + last_name
message = "Hello, "+ full_name.title() + "!"

print(message)

# Podemos também acrescentar tabulação às saídas de strings.

# Ex: 
"""
    print('Python')

    acrescentando \t antes do nome Python a saída será uma tabulação, ou seja, haverá um espaço em branco antes do nome.

    print('\tPython')

    Execute abaixo e observe como funciona.
"""

print('Python')

print('\tPython')

# Quando queremos mostrar uma quebra de linha podemos utilizar os caracteres \n antecendendo o texto que queira exibir.
# ex:
"""
    print('Hello\nPython')

    isto resultará na mensagem: >>> Hello
                                    Python

# Faça e observe tal como na tabulação utilizamos o \t para criar tabulação o \n quebra uma linha.
"""

print('Hello\nPython')

# Podemos utilizar também a quebra de linha junto com a tabulação. Vejamos um exemplo de quebra de linha e posterior uso com tabulação.

print('\nPython\nJavascript\nC\nRubyOnRails') # Usamos a quebra de linha. Execute o teste.

# agora faremos a quebra de linha junto da tabulação. Execute tal como na anterior.

print('\n\tPython\n\tJavascript\n\tC\n\tRubyOnRails') # Perceba a diferença e use-as com sabedoria.

# Removendo espaços em Branco

""" 
Espaços em branco extras podem ser confusos em seus programas. Para os
programadores, 'python' e 'python ' parecem praticamente iguais.
Contudo, para um programa, são duas strings diferentes. Python identifica
o espaço extra em 'python ' e o considera significativo, a menos que você
informe o contrário.
"""

# Felizmente python consegue reconhecer espaços em branco e removê-los através de um método.
# Se o espaço em branco que você deseja eliminar seja à direita ou à esquerda. No caso de ser a Direita usamos o rstrip().

# Ex:

favorite_language = 'Python '
print(favorite_language)

# Com o uso do rstrip()

print(favorite_language.rstrip())

# Para removermos espaços em branco do lado esquerdo de uma string usamos o método lstrip(). 
# Podemos também remover os espaços em branco dos dois lados ao mesmo tempo usando o método strip().