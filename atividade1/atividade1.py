# pip install ply
import ply.lex as lex

# Gramática definida:
# <ID> ::= <L> ( <L> | <D> )
# <L> ::= a-z
# <D> ::= 0-9

# Definição dos tokens utilizados
tokens = ('ID',)

# Regras léxicas para o token ID
t_ID = r'[a-z][a-z0-9]'

# Ignorar espaços, tabulações e quebras de linha
t_ignore = ' \t\n'

# Função para tratamento de erros
def t_error(t):
    t.lexer.skip(1)  # Avança para o próximo caractere

# Criação do analisador léxico com as regras definidas
lexer = lex.lex()

# Função para validar cada palavra com base na gramática
def validar_palavra(palavra):
    lexer.input(palavra)
    token = next(lexer, None)  # Obtém o primeiro token reconhecido
    if token and token.type == 'ID' and token.value == palavra:
        return True  # A palavra é válida segundo a gramática
    return False  # A palavra é inválida

# Entrada de teste
entrada = "ab a1 zz q3 abc a 123 aa"
palavras = entrada.split()

# Validar cada palavra da entrada
for palavra in palavras:
    if validar_palavra(palavra):
        print(f"'{palavra}' é válida")
    else:
        print(f"'{palavra}' NÃO é válida")
