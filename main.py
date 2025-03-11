from lexic import AnalizadorSintatico

code = """
var x = 10 + 3.14
if x > 5
while x < 20 AND x < 1 0
"""


def main():
    analizador_sintatico = AnalizadorSintatico(code)
    analizador_sintatico.tokenizar()

    print(analizador_sintatico.get_token())


if __name__ == '__main__':
    main()
