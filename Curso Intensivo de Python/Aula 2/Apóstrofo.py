""" 
Evitando erros de sintaxe com strings
Um tipo de erro que você poderá ver com certa regularidade é um erro de
sintaxe. Um erro de sintaxe ocorre quando Python não reconhece uma
seção de seu programa como um código Python válido. Por exemplo, se
usar um apóstrofo entre aspas simples, você produzirá um erro. Isso
acontece porque Python interpreta tudo que estiver entre a primeira aspa
simples e o apóstrofo como uma string. Ele então tenta interpretar o
restante do texto como código Python, o que causa erros.
Eis o modo de usar aspas simples e duplas corretamente.
"""
message = "One of Python's strengths is its diverse community." 
# Se você mudar de aspas duplas pra simples, python retornará um erro. Troque, execute e observe atentamente.
print(message)

# Página 69