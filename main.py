from lexic import AnalizadorLexico
from parser import Parser

code = """
var x = 10 + 3.14
if x > 5
    var x = 4 + 2
while x < 20 AND x > 1
    var x = x + 3
"""


def main():
    analizador_sintatico = AnalizadorLexico(code)
    analizador_sintatico.tokenizar()

    parser = Parser(analizador_sintatico.get_token())
    parser.analisar()


if __name__ == '__main__':
    main()
