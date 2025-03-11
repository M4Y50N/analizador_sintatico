import re
import sys


class AnalizadorSintatico:
    TOKENS = {
        'palavras_reservadas': r'\b(var|if|while|F|V)\b',  # \b é para garantir que sejam palavras inteiras
        'numero': r'\b\d+(\.\d+)?\b',  # números inteiros e flutuantes
        'variavel': r'[a-zA-Z_]\w*',
        'literal': r'"[^"]*"',  # strings com aspas, qualquer coisa entre aspas
        'operador': r'[+\-*/**//]',  # operadores aritméticos
        'operador_definicao': r'=',
        'operador_logico': r'OR|AND|NOT',
        'operador_relacionais': r'==|<>|>|<|>=|<='
    }

    def __init__(self, code):
        self.code = code

    def structure_validation(self):
        linhas = self.code.strip().split("\n")

        def check(i, linha_to_check, linha_index):
            if len(linha_to_check) == i:
                return


            comando = linha_to_check[i]
            for tipo_token, regex in self.TOKENS.items():
                padrao = re.compile(regex)
                resultado = padrao.fullmatch(comando)
                if resultado is not None:
                    print(tipo_token + ": " + comando)
                    return check(i + 1, linha_to_check, linha_index)
            print(f"Error de sintaxe na linha: {linha_index + 1}", file=sys.stderr)
            exit()

        for index, linha in enumerate(linhas):
            linha_splitada = [l for l in linha.split(" ") if l != ""]

            check(0, linha_splitada, index)
