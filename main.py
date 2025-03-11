from lexic import AnalizadorLexico
from parser import Parser

code = """
var x = 10 + 1 * 3
if x > 5
    x = 4 + 2
while x < 20 AND x > 7
    x = x + 3
"""


def main():
    # Transforma o código em tokens e os armazena em um array
    analizador_sintatico = AnalizadorLexico(code)
    analizador_sintatico.tokenizar()

    # Verifica a sintaxe desses tokens
    parser = Parser(analizador_sintatico.get_token())
    ast = parser.analisar()

    # Printa estrutura da arvore
    ast.print_ast()


if __name__ == '__main__':
    main()
