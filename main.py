from lexic import AnalizadorLexico
from interpretador import Interpretador
from parser import Parser

code = """
var x = 10 + 3.14
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
    # ast.print_ast()

    # Chama o interpretador
    interpretador = Interpretador()
    interpretador.executar(ast)

    print(interpretador.variaveis)


if __name__ == '__main__':
    main()
