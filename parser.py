from ast import OperacaoBinaria, Numero, Variavel, Atribuicao, Programa


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.linha = 1

    def analisar(self):
        comandos = []
        while self.pos < len(self.tokens):
            comandos.append(self.comando())
            return Programa(comandos)

    def comando(self):
        if self.tokens[self.pos].tipo == "palavras_reservadas":
            if self.tokens[self.pos].valor == "if":
                return self.condicional()
            elif self.tokens[self.pos].valor == "while":
                return self.repeticao()
            elif self.tokens[self.pos].valor == "var":
                return self.atribuicao()

        elif self.tokens[self.pos].tipo == "variavel":
            return self.atribuicao()

        elif self.tokens[self.pos].tipo == "nova_linha":
            self.linha += 1
            return self.consumir("nova_linha")


        else:
            raise SyntaxError(f"Erro de sintaxe: comando inválido na linha {self.linha}")

    def condicional(self):
        self.consumir("palavras_reservadas")  # confirma se recebe o if e passa para o próximo token
        self.expressao_if_while()
        self.consumir("nova_linha")  # quebra de linha obrigatória
        self.linha += 1
        self.bloco()

    def repeticao(self):
        self.consumir("palavras_reservadas")  # while
        self.expressao_if_while()
        self.consumir("nova_linha")  # quebra de linha obrigatória
        self.linha += 1
        self.bloco()

    def bloco(self):
        while self.pos < len(self.tokens) and self.tokens[self.pos].tipo != "nova_linha":
            self.comando()

    def atribuicao(self):
        if self.tokens[self.pos].valor == "var" and self.tokens[self.pos].tipo == "palavras_reservadas":
            self.consumir("palavras_reservadas")

        variavel = Variavel(self.consumir("variavel").valor)
        self.consumir("operador_definicao")
        expressao = self.expressao()

        return Atribuicao(variavel, expressao)

    def expressao(self):
        esquerda = self.termo()
        while self.pos < len(self.tokens) and self.tokens[self.pos].tipo == "operador":
            operador = self.consumir("operador").valor
            direita = self.termo()
            esquerda = OperacaoBinaria(esquerda, operador, direita)
        return esquerda

    def expressao_if_while(self):
        self.termo()
        while self.pos < len(self.tokens) and (self.tokens[self.pos].tipo == "operador_logico" or
                                               self.tokens[self.pos].tipo == "operador_relacionais"):
            self.consumir_if_while()
            self.termo()

    def termo(self):
        token = self.tokens[self.pos]
        if token.tipo == "numero":
            self.consumir("numero")
            return Numero(float(token.valor))
        elif token.tipo == "variavel":
            self.consumir("variavel")
            return Variavel(token.valor)
        else:
            raise SyntaxError(f"Erro de sintaxe: termo inválido na linha {self.linha}")

    def consumir(self, tipo_esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos].tipo == tipo_esperado:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado {tipo_esperado}, encontrado {self.tokens[self.pos].tipo} na "
                              f"linha {self.linha}")

    def consumir_if_while(self):
        tipo_esperado = ("operador_logico", "operador_relacionais")
        if self.pos < len(self.tokens) and self.tokens[self.pos].tipo in tipo_esperado:
            token = self.tokens[self.pos]
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Erro de sintaxe: esperado {tipo_esperado}, encontrado {self.tokens[self.pos].tipo} na "
                              f"linha {self.linha}")
